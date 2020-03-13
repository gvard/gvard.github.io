'use strict';
/*jshint esversion: 6 */
const OBJTYPES = {
  sg: "Сверхгигант", mira: "Мирида",
  deltaSct: "Переменная типа дельты Щита",
  agb: "Звезда асимптотической ветви гигантов",
  algol: "Затменная переменная типа Алголя",
  rot: "Быстро вращающаяся звезда"
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
  if (!txt)
    return 0;
  return Number(txt.slice(6, 10));
}
function showHideByDate(mode) {
  const elems = getDivs('date');
  const yearForSort = parseInt(document.getElementById('year').value, 10);
  let j = 0;
  for (let i = 0; i < elems.length; i += 1) {
    if (elems[i].innerText && getDate(elems[i].innerText) > yearForSort) {
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
function txtMass(txt) {
  return txt.includes("±") ? txt.substring(0, txt.indexOf("±")) + txt.substring(txt.indexOf("E")) : txt;
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
function ObjParams() {
  const objs = getDivs('obj');
  let objArr = [];
  let objDct = [];
  for (let i = 0; i < objs.length; i += 1) {
    const classes = objs[i].className.replace('obj ', '').split(' ');
    const a = objs[i].getElementsByClassName('name')[0].getElementsByTagName("a")[0];
    const objRuName = a.text;
    const img = objs[i].getElementsByClassName('img')[0].getElementsByTagName("img")[0];
    const imgPath = img.src.split('/');
    const size = getSize(objs[i].getElementsByClassName('size')[0].innerText);
    const mass = txtMass(objs[i].getElementsByClassName('mass')[0].innerText);
    objDct.push({ 'name': img.alt, 'runame': objRuName, 'size': size, 'mass': mass, 'classes': classes });
    objArr.push([img.alt, objRuName, size, mass, classes, imgPath[imgPath.length - 1]]);
  }
  console.log(objArr);
  console.log(objDct);
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
  let mag = obj.getElementsByClassName("mag")[0].innerText;
  mag = mkPar('Звездная величина (V): ', mag, '<sup>m</sup>');
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
  return name + type + angular + size + mass + spClass + temp + mag + desc;
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
  for (let i = 0; i < elems.length; i += 1) {
    j += 1;
    total += getSize(elems[i].innerText);
    console.log(`For ${j} elements sum of sizes is ${total} km`);
  }
}
