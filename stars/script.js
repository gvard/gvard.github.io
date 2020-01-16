'use strict';
/*jshint esversion: 6 */
const OBJTYPES = {
  star: "звезда"
};
function logger(mode, len) {
  let displayMode = '';
  if (mode == 'none')
    displayMode = 'Hide';
  else if (mode.includes('block'))
    displayMode = 'Show';
  console.log(`${displayMode} ${len} objects`);
}
function showHideThis(mode, classNam) {
  const elems = document.querySelectorAll(classNam);
  for (let i = 0; i < elems.length; i++)
    elems[i].style.display = mode;
  logger(mode, elems.length);
}
function getDivs(classNam) {
  let mainTab = document.getElementsByClassName('tab main')[0];
  return mainTab.getElementsByClassName(classNam);
}
function getDate(txt) {
  if (txt == 'None')
    return 0;
  return Number(txt.slice(6, 10));
}
function findDate() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  const today = `${day}.${month}`;
  const elems = document.getElementsByClassName('date');
  for (let i = 0; i < elems.length; i++) {
    let daymon = elems[i].innerText.slice(0, 5);
    if (today == daymon) {
      console.log(today, daymon);
    }
  }
// document.write(datetime);

}
function showHideByDate(mode) {
  const elems = getDivs('date');
  const yearForSort = parseInt(document.querySelector('#year').value);
  let j = 0;
  for (let i = 0; i < elems.length; i++) {
    if (elems[i].innerText != 'None' && getDate(elems[i].innerText) > yearForSort) {
      elems[i].parentElement.style.display = mode;
      j += 1;
    }
  }
  logger(mode, j);
}
function getMass(txt) {
  if (txt == 'None')
    return 0;
  return txt.includes("±") ? Number(txt.substring(0, txt.indexOf("±")) + txt.substring(txt.indexOf("E"))) : Number(txt);
}
function getSize(txt) {
  let num = 0;
  if (txt.includes("±"))
    num = parseFloat(txt.substring(0, txt.indexOf("±")));
  else if (txt.includes("−"))
    num = parseFloat(txt.substring(0, txt.indexOf("−")));
  else
    num = parseFloat(txt);
  return Number(num);
}
function getNames() {
  let objToSort = getDivs('obj');
  let objArr = [];
  for (let i = 0; i < objToSort.length; i++) {
    let a = objToSort[i].getElementsByClassName('desc')[0].getElementsByTagName("a")[0].href.split("/");
    objArr.push(a[a.length - 1]);
  }
  console.log(objArr);
}
function toSort(classNam) {
  let objToSort = getDivs('obj');
  let ArrToSort = Array.prototype.slice.call(objToSort, 0);
  var sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'date')
    sortFunction = getDate;
  else if (classNam == 'size')
    sortFunction = getSize;
  ArrToSort.sort(function(a, b) {
    let aord = sortFunction(a.getElementsByClassName(classNam)[0].innerText);
    let bord = sortFunction(b.getElementsByClassName(classNam)[0].innerText);
    return (aord > bord) ? 1 : -1;
  });
  var parent = document.getElementsByClassName('main')[0];
  parent.innerHTML = "";
  for (let i = 0, l = ArrToSort.length; i < l; i += 1)
    parent.appendChild(ArrToSort[i]);
}
function hide() {
  var messageBox = document.getElementById('messageBox');
  messageBox.style.display = 'none';
}
function mkPar(before, txt, after) {
  return (!txt) ? '' : `<p>${before}${txt}${after}</p>`;
}
function mkContents(obj) {
  let name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  let size = obj.getElementsByClassName("size")[0].innerText;
  size = mkPar('Радиус: ', size, '&nbsp;км');
  let mass = obj.getElementsByClassName("mass")[0].innerText;
  mass = mkPar('Масса: ', mass, '&nbsp;кг');
  let date = obj.getElementsByClassName("date")[0].innerText;
  date = mkPar('Дата открытия: ', date, '');
  let type = "";
  for (let objClassNam of obj.className.split(" "))
    if (objClassNam in OBJTYPES)
      type = OBJTYPES[objClassNam];
  type = mkPar('Тип: ', type, '');
  let deltaV = obj.getElementsByClassName("delta-v");
  if (deltaV.length) {
    deltaV = deltaV[0].innerText;
    deltaV = mkPar('Δv: ', deltaV, '&nbsp;км/с');
  }
  else {
    deltaV = "";
  }
  return `${name}${type}${size}${mass}${date}${deltaV}`;
}
function show(divImg) {
  const obj = divImg.parentElement;
  var contents = document.getElementById('contents');
  contents.innerHTML = `${divImg.innerHTML}${mkContents(obj)}`;
  var messageBox = document.getElementById('messageBox');
  var x, y;
  if (window.event) {
    x = window.event.clientX + document.documentElement.scrollLeft +
        document.body.scrollLeft;
    y = window.event.clientY + document.documentElement.scrollTop +
        document.body.scrollTop;
  }
  else {
    x = event.clientX + window.scrollX;
    y = event.clientY + window.scrollY;
  }
  x -= 2;
  y += 15;
  if (screen.width - x < 200 / window.devicePixelRatio)
    x -= 180 / window.devicePixelRatio;
  messageBox.style.left = x + "px";
  messageBox.style.top = y + "px";
  messageBox.style.display = "block";
}
function calcSum(classNam) {
  const elems = document.getElementsByClassName(classNam);
  let total = 0;
  let j = 0;
  for (let i = 0; i < elems.length; i++) {
    j += 1;
    total += getSize(elems[i].innerText);
    console.log(`For ${j} elements sum of sizes is ${total} km`);
  }
}
