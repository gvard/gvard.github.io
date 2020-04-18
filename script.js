function WordNumberCase(number) {
  const num = number >= 0 ? number : -number;
  let m = num % 10;
  let result;
  switch (m) {
    case 1:
      result = "год";
      break;
    case 2:
    case 3:
    case 4:
      result = "года";
      break;
    default:
      result = "лет";
      break;
  }
  if (m >= 1 && m <= 4) {
    m = num % 100;
    if (m >= 11 && m <= 14)
      result = "лет";
  }
  return result;
}
function createCORSRequest(method, url) {
  let xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    xhr = new XDomainRequest();
  xhr.open(method, url);
  } else {
    xhr = null;
  }
  return xhr;
}
function loadReq(URL, goFunc) {
  let request = createCORSRequest('GET', URL);
  request.responseType = 'json';
  request.send();
  request.onload = function() {
    const elmToShowInfo = document.getElementById("sp");
    goFunc(request.response, elmToShowInfo);
  };
}
function showAPOD(res, q) {
  let media = "";
  if (res.media_type === "video") {
    media = '<iframe width="560" height="315" src="' + res.url + '" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
  } else {
    media = '<a href="' + res.hdurl + '"><img alt="" src="' + res.url + '"></a>';
  }
  q.innerHTML = '<br><b>' + res.date + ', ' + res.title + '</b><br>' + media + '<br>' + res.explanation;
}
function mkReq(reqName) {
  const reqNames = {
    apod: {
      URL: 'https://api.nasa.gov/planetary/apod?api_key=eZgjB1gdPqQDKOz5gh4hCvJy6A1oq22reiKFD3GI',
      func: showAPOD
    }
  };
  loadReq(reqNames[reqName].URL, reqNames[reqName].func);
}
function getDates(dateObj) {
  const day = ("0" + dateObj.getDate()).slice(-2);
  const month = ("0" + (dateObj.getMonth() + 1)).slice(-2);
  return { daymon: day + "." + month, month: month, year: dateObj.getFullYear() };
}
function appendContent(daymon, deltaYr, datada, div) {
  const h2 =  document.createElement('h2');
  h2.innerText = daymon + "." + datada.year + ": " + datada.slug;
  div.appendChild(h2);
  const img = document.createElement('img');
  img.src = datada.img;
  div.appendChild(img);
  const desc = document.createElement('div');
  if (!datada.desc)
    datada.desc = "назад";
  desc.innerText = deltaYr + " " + WordNumberCase(deltaYr) + " " + datada.desc;
  div.appendChild(desc);
}
function showDates(res, q) {
  const deltaDays = 28;
  q.innerHTML = "Годовщины на ближайшие " + deltaDays + " дней:";
  const div = document.createElement('div');
  q.appendChild(div);
  const currentDate = new Date();
  for (let i = 0; i < deltaDays; i += 1) {
    const curDate = new Date(currentDate);
    curDate.setDate(curDate.getDate() + i);
    const data = getDates(curDate);
    if (data.daymon in res) {
      for (let datada of res[data.daymon]) {
        let deltaYr = currentDate.getFullYear() - datada.year;
        appendContent(data.daymon, deltaYr, datada, div);
      }
    }
  }
}
function loadDates() {
  loadReq('https://gvard.github.io/dates/astrocosm.json', showDates);
}