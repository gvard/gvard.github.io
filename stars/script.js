'use strict';
/*jshint esversion: 6 */
const OBJTYPES = {
  star: "звезда"
};
function logger(mode, len) {
  let displayMode = '';
  if (mode == 'none') {
    displayMode = 'Hide';
  }
  else if (mode.includes('block')) {
    displayMode = 'Show';
  }
  console.log(displayMode, len, 'objects');
}
function showHideThis(checkBox) {
  const elems = document.querySelectorAll(checkBox.name);
  let mode = 'none';
  if (checkBox.checked) {
    mode = 'block';
  }
  for (let i = 0; i < elems.length; i += 1) {
    elems[i].style.display = mode;
  }
  logger(mode, elems.length);
}
function getDivs(classNam) {
  const mainTab = document.getElementById('tab');
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
}
function showHideByDate(mode) {
  const elems = getDivs('date');
  const yearForSort = parseInt(document.getElementById('year').value);
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
  if (!txt)
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
  let sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'size')
    sortFunction = getSize;
  ArrToSort.sort(function (a, b) {
    let aord = sortFunction(a.getElementsByClassName(classNam)[0].innerText);
    let bord = sortFunction(b.getElementsByClassName(classNam)[0].innerText);
    return (aord > bord) ? 1 : -1;
  });
  let parent = document.getElementById('tab');
  parent.innerHTML = "";
  for (let i = 0, l = ArrToSort.length; i < l; i += 1)
    parent.appendChild(ArrToSort[i]);
}
function hide() {
  let messageBox = document.getElementById('messageBox');
  messageBox.style.display = 'none';
}
function mkPar(before, txt, after) {
  return (!txt) ? '' : `<p>${before}${txt}${after}</p>`;
}
function mkContents(obj) {
  let name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  let angular = obj.getElementsByClassName("angular")[0].innerText;
  angular = mkPar('Угловые размеры: ', angular, '&nbsp;mas');
  let size = obj.getElementsByClassName("size")[0].innerText;
  size = mkPar('Радиус: ', size, '&nbsp;R<sub>☉</sub>');
  let mass = obj.getElementsByClassName("mass")[0].innerText;
  mass = mkPar('Масса: ', mass, '&nbsp;M<sub>☉</sub>');
  let spClass = obj.getElementsByClassName("class")[0].innerText;
  spClass = mkPar('Спектральный класс: ', spClass, '');
  let temp = obj.getElementsByClassName("temp")[0].innerText;
  temp = mkPar('Температура: ', temp, '&nbsp;K');

  let type = "";
  for (let objClassNam of obj.className.split(" "))
    if (objClassNam in OBJTYPES)
      type = OBJTYPES[objClassNam];
  type = mkPar('Тип: ', type, '');
  let desc = obj.getElementsByClassName("desc");
  if (desc.length)
    desc = mkPar('', desc[0].innerText, '');
  else
    desc = "";
  return name + type + angular + size + mass + spClass + temp + desc;
}

function show(divImg) {
  const obj = divImg.parentElement;
  let contents = document.getElementById('contents');
  contents.innerHTML = `${divImg.innerHTML}${mkContents(obj)}`;
  let messageBox = document.getElementById('messageBox');
  let x, y;
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
