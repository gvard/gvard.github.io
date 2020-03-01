const RANDUSR_URL = 'https://randomuser.me/api/';
const REQRES_URL = 'https://reqres.in/api/products/3';
const SW_URL = 'https://swapi.co/api/people/1/';
const TZ_URL = 'http://api.timezonedb.com/v2.1/get-time-zone?key=7QR5BE7L232Z&format=json&by=zone&zone=Europe/Moscow';
const YANDEX_TIME_URL = 'https://yandex.com/time/sync.json?geo=213';
const CORS_ANYWHERE_URL = 'https://cors-anywhere.herokuapp.com/';
const EXCHANGE_URL = 'https://api.exchangerate-api.com/v4/latest/USD';

function appendUsers(usersArray) {
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
// function parseHttpHeaders(httpHeaders) {
//   return httpHeaders.split("\n")
//    .map(x=>x.split(/: */,2))
//    .filter(x=>x[0])
//    .reduce((ac, x)=>{ac[x[0]] = x[1];return ac;}, {});
// }
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
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
function loadReq(URL, goFunc) {
  let request = createCORSRequest('GET', URL);
  if (!request)
    console.log('CORS not supported');
  console.log('request.readyState 1:', request.readyState);
  request.onload = function() { // onreadystatechange
    console.log("status, headers:", request.status, request.getAllResponseHeaders());
    // console.log("responseText:", request.responseText)
    if (request.status >= 200 && request.status < 400) {
      let res = JSON.parse(request.response);
      console.log('Parsed JSON response:', res);
      goFunc(res);
    } else {
      console.error('Error!')
    }
  };
  request.send();
}
function showRes(res) {
  let q = document.getElementById("sp");
  q.innerHTML = res.data.year;
  q.style.color = res.data.color;
}
function showTime(res) {
  let q = document.getElementById("sp");
  q.innerHTML = res.formatted;
}
function showYandexTime(res) {
  let q = document.getElementById("sp");
  q.innerHTML = new Date(res.time);
}
function showLuke(res) {
  let q = document.getElementById("sp");
  q.innerHTML = 'Имя: ' + res.name + ', рост: ' + res.height + ', вес: ' + res.mass + ', дата рождения: ' + res.height + ', цвет волос: ' + res.hair_color;
}
function showExchangeRate(res) {
  let q = document.getElementById("sp");
  q.innerHTML = res.rates.RUB;
}
function loadUsers(gender, num) {
  let url = RANDUSR_URL + '?results=' + num + '&gender=' + gender + '&email=emeline.leclercq@example.com';
  loadReq(url, appendUsers);
}
function loadReqRes() {
  loadReq(REQRES_URL, showRes);
}
function loadSW() {
  loadReq(SW_URL, showLuke);
}
function loadTZ() {
  loadReq(TZ_URL, showTime);
}
function loadYndexTime() {
  loadReq(CORS_ANYWHERE_URL + YANDEX_TIME_URL, showYandexTime);
}
function exchange() {
  loadReq(EXCHANGE_URL, showExchangeRate);
}