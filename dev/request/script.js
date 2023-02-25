'use strict';
const RANDUSR_URL = 'https://randomuser.me/api/';
const TZ_URL = 'http://api.timezonedb.com/v2.1/get-time-zone?key=7QR5BE7L232Z&format=json&by=zone&zone=Europe/Moscow';
const APOD_URL = 'https://api.nasa.gov/planetary/apod?api_key=eZgjB1gdPqQDKOz5gh4hCvJy6A1oq22reiKFD3GI';
const YANDEX_TIME_URL = 'https://yandex.com/time/sync.json?geo=213';
const CORS_ANYWHERE_URL = 'https://cors-anywhere.herokuapp.com/';

function createCORSRequest(method, url) {
  let xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
  xhr.open(method, url);
  } else {
    // Otherwise, CORS is not supported by the browser.
    xhr = null;
  }
  return xhr;
}
function appendUsers(usersArray, _) {
  for (let i = 0; i < usersArray.results.length; i += 1) {
    let user = usersArray.results[i];
    let username = usersArray.results[i].name;
    let email = usersArray.results[i].email;
    let userElement = document.createElement('div');
    userElement.style.display = 'inline-block';
    userElement.style.padding = '15px';
    let image = document.createElement('img');
    image.src = user.picture.large;
    let fullName = username.title + ' ' + username.first + ' ' + username.last;
    image.alt = fullName;
    image.style.display = 'block';
    userElement.appendChild(image);
    userElement.appendChild(document.createTextNode(fullName));
    userElement.appendChild(document.createElement('br'));
    userElement.appendChild(document.createTextNode(email));
    document.body.appendChild(userElement);
  }
  document.body.appendChild(document.createElement('br'));
}
function loadReq(URL, goFunc) {
  let request = createCORSRequest('GET', URL);
  if (!request)
    console.log('CORS not supported');
  console.log('request.readyState 1:', request.readyState);
  request.onload = function() { // onreadystatechange
    console.log("status, headers:", request.status, request.getAllResponseHeaders());
    // console.log("responseText:", request.responseText)
    const elmToShowInfo = document.getElementById("sp");
    if (request.status >= 200 && request.status < 400) {
      const res = JSON.parse(request.response);
      console.log('Parsed JSON response:', res);
      goFunc(res, elmToShowInfo);
    } else {
      elmToShowInfo.innerHTML = 'Error! HTML status code: ' + request.status;
      console.error('Error!');
    }
  };
  request.send();
}
function showReqRes(res, q) {
  q.innerHTML = 'Year: ' + res.data.year + ', name: ' + res.data.name;
  q.style.color = res.data.color;
}
function showTime(res, q) {
  q.innerHTML = res.formatted;
}
function showYandexTime(res, q) {
  q.innerHTML = new Date(res.time);
}
function showLuke(res, q) {
  q.innerHTML = 'Имя: ' + res.name + ', рост: ' + res.height + ', вес: ' + res.mass + ', дата рождения: ' + res.birth_year + ', цвет волос: ' + res.hair_color;
}
function showLatestSpaceXFlight(res, q) {
  const localDateTime = new Date(res.date_unix * 1000);
  q.innerHTML = `Flight number: ${res.flight_number}, название миссии: ${res.name}.<br>
  Дата и время запуска: ${res.date_utc} (UTC), московское время: ${localDateTime}.<br>
  Эмблема:<br><img src="${res.links.patch.small}" alt=""><br>
  <a href="${res.links.reddit.launch}">Подробно на reddit</a>, <a href="${res.links.wikipedia}">на википедии</a>.<br>
  Подробности на английском: ${res.details}`;
}
function showAstros(res, q) {
  let strRepr = ": ";
  for (let i = 0; i < res.people.length; i += 1)
    strRepr += res.people[i].name + ', '
  q.innerHTML = res.number + strRepr.slice(0, -2);
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
function loadUsers(gender, num) {
  const url = RANDUSR_URL + '?results=' + num + '&gender=' + gender + '&email=emeline.leclercq@example.com';
  loadReq(url, appendUsers);
}
function getSummoner(res, q) {
  let image = document.createElement('img');
  const ver = "10.9.1";
  image.src = `http://ddragon.leagueoflegends.com/cdn/${ver}/img/profileicon/${res.profileIconId}.png`;
  q.appendChild(image);
  const reqDate = new Date(res.revisionDate);
  let info = document.createElement('span');
  info.innerHTML = `Имя: ${res.name}; Уровень: ${res.summonerLevel}; revision Date: ${reqDate}`;
  q.appendChild(info);
}
function requestSummoner() {
  const sumName = document.getElementById("summonerName").value;
  const APIKEY = document.getElementById("APIKey").value;
  let URL = CORS_ANYWHERE_URL + `https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/${sumName}?api_key=${APIKEY}`;
  loadReq(URL, getSummoner)
}
function mkReq(reqName) {
  const reqNames = {
    TZ: {URL: TZ_URL, func: showTime},
    yandexTime: {URL: CORS_ANYWHERE_URL + YANDEX_TIME_URL, func: showYandexTime},
    reqRes: {URL: 'https://reqres.in/api/products/3', func: showReqRes},
    starWars: {URL: 'https://swapi.co/api/people/1/', func: showLuke},
    exchange: {URL: 'https://api.exchangerate-api.com/v4/latest/USD', func: function (res, q) { q.innerHTML = res.rates.RUB; }},
    spaceX: {URL: 'https://api.spacexdata.com/v5/launches/latest', func: showLatestSpaceXFlight},
    astros: {URL: 'http://api.open-notify.org/astros.json', func: showAstros},
    apod: {URL: APOD_URL, func: showAPOD}
  };
  loadReq(reqNames[reqName].URL, reqNames[reqName].func);
}