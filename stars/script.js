"use strict";
/*jshint esversion: 6 */
const OBJTYPES = {
  sg: "Сверхгигант", mira: "Мирида",
  deltaSct: "Переменная типа дельты Щита",
  agb: "Звезда асимптотической ветви гигантов",
  algol: "Затменная переменная типа Алголя",
  rot: "Быстро вращающаяся звезда"
};
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
  let sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'size')
    sortFunction = getSize;
  doSort(sortFunction, classNam);
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
  } else {
    x = event.clientX + window.scrollX;
    y = event.clientY + window.scrollY;
  }
  x -= 2;
  y += 15;
  if (screen.width - x < 200 / window.devicePixelRatio) {
    x -= 180 / window.devicePixelRatio;
  }
  messageBox.style.left = x + "px";
  messageBox.style.top = y + "px";
  messageBox.style.display = "block";
}