"use strict";
/*jshint esversion: 6 */
const OBJTYPES = {
  giant: "Гигант",
  subgiant: "Субгигант",
  hypergiant: "Гипергигант",
  sg: "Сверхгигант", mira: "Мирида",
  agb: "Звезда асимптотической ветви гигантов",
  deltaSct: "Переменная типа дельты Щита",
  algol: "Затменная переменная типа Алголя",
  betaLyr: "Затменная переменная типа β Лиры",
  RSCVn: "Переменная типа RS CVn",
  SRb: "Полуправильная переменная SRb",
  SRc: "Полуправильная переменная SRc",
  Lb: "Медленная неправильная переменная Lb",
  Lc: "Медленная неправильная переменная Lc",
  Be: "Be-звезда",
  rot: "Быстро вращающаяся звезда",
  SB1: "Спектрально-двойная звёзда SB1",
  nova: "Новая"
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
function show(divImg, imgPth) {
  const obj = divImg.parentElement;
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
  let type = mkType(obj.className, OBJTYPES);
  type = mkPar('Типы: ', type, '');
  let desc = obj.getElementsByClassName("desc");
  if (desc.length) {
    desc = mkPar('', desc[0].innerText, '');
  } else {
    desc = "";
  }
  if (!imgPth) {
    imgPth = divImg.getElementsByTagName('img')[0].src;
  }
  const contentToShow = `<img src="${imgPth}"><h2>${name}</h2>` + type + angular + size + mass + spClass + temp + mag + desc;
  toShow(contentToShow);
}
