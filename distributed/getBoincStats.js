'use strict';

const retiredCredits = [
{
"project": "MW2",
"stats": 47014.534232481
},
{
"project": "SET",
"stats": 21089.588969897
},
{
"project": "SE2",
"stats": 14677.906245
},
{
"project": "SE3",
"stats": 761.407897141145
},
{
"project": "POG",
"stats": 375980.23
},
{
"project": "POE",
"stats": 324687.64
},
{
"project": "SAT",
"stats": 192600.00
},
{
"project": "AC",
"stats": 37212.00
},
// {
// "project": "GOO",
// "stats": 2407680
// },
// {
// "project": "CON",
// "stats": 21775.65
// },
// {
// "project": "DHE",
// "stats": 6957.00
// },
// {
// "project": "COL",
// "stats": 1343145.61
// },
]
const retiredCreditsSum = 4793581.567344519;
const retiredCreditsSumNoDoubtful = 1014023.3073445191;
// 2023-02-23 Честные кредиты: 9381161.238340221, свальный грех: 13160719.498340223

const BOINC_DATA = {
AS: {
URL: "https://asteroidsathome.net/boinc/",
ID: 28825,
},
EI: {
URL: "https://einsteinathome.org/",
ID: 603616,
},
PG: {
URL: "https://www.primegrid.com/",
ID: 1073864,
},
UN: {
URL: "https://universeathome.pl/universe/",
ID: 3547,
},
MW: {
URL: "https://milkyway.cs.rpi.edu/milkyway/",
ID: 117018, //ID: 148127,
},
GP: {
URL: "https://gpugrid.net/",
ID: 537077,
},
RO: {
URL: "https://boinc.bakerlab.org/rosetta/",
ID: 388192,
},
GE: {
URL: "https://gerasim.boinc.ru/users/",
ID: 7029,
},
CO: {
URL: "http://www.cosmologyathome.org/",
ID: 107296,
},
WU: {
URL: "https://wuprop.boinc-af.org/",
ID: 132056,
},
LHC: {
URL: "https://lhcathome.cern.ch/lhcathome/",
ID: 578977,
},
SI: {
URL: "https://sidock.si/sidock/",
ID: 10462,
},
GA: {
URL: "http://150.254.66.104/gaiaathome/",
ID: 9234,
},
// "SE": {
// "URL": "https://setiathome.berkeley.edu/",
// "ID": 9915793, //"ID": 7813115, //"ID": 9416599,
// },
}

const CORS_ANYWHERE_URL = 'https://cors-anywhere.herokuapp.com/';
const delay = ms => new Promise(res => setTimeout(res, ms));

function createCORSRequest(method, url) {
  const xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, false);
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
function mkReq(elm) {
  const elmToShowInfo = document.getElementById("sp");
  var parsedResults = [];
  const reqName = elm.parentElement.id;
  if (reqName == 'All') {
    for (const proj in BOINC_DATA) {
      const URL = `${CORS_ANYWHERE_URL}${BOINC_DATA[proj].URL}show_user.php?userid=${BOINC_DATA[proj].ID}&format=xml`;
      let request = createCORSRequest('GET', URL);
      request.send(null);
      var parser = new DOMParser();
      const res = parser.parseFromString(request.response, "text/xml");
      const projTotalCredit = res.getElementsByTagName("total_credit")[0].childNodes[0].nodeValue;
      delay(500);
      parsedResults.push({
        project: proj,
        stats: projTotalCredit,
      });
      const curElm = document.getElementById(proj);
      curElm.innerHTML = Math.round(projTotalCredit * 100) / 100;
    }
    let CreditSum = 0;
    for (const z of parsedResults) {
      CreditSum += parseFloat(z.stats);
    }
    elmToShowInfo.innerHTML = `Честные кредиты: ${Math.round((retiredCreditsSumNoDoubtful+CreditSum) * 100) / 100}, свальный грех: ${Math.round((retiredCreditsSum+CreditSum) * 100) / 100}`;
  } else {
    const URL = `${CORS_ANYWHERE_URL}${BOINC_DATA[reqName].URL}show_user.php?userid=${BOINC_DATA[reqName].ID}&format=xml`;
    let request = createCORSRequest('GET', URL);
    request.send(null);
    var parser = new DOMParser();
    const res = parser.parseFromString(request.response, "text/xml");
    const projCredit = res.getElementsByTagName("total_credit")[0].childNodes[0].nodeValue;
    elm.parentElement.innerHTML = projCredit;
  }
}
