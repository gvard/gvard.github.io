"use strict";
const OBJTYPES = {
  star: "звезда", pla: "планета", neo: "околоземный астероид", co: "ядро кометы", ea: "спутник Земли", mar: "спутник Марса", mab: "астероид основного пояса", dw: "карликовая планета", ju: "спутник Юпитера", sat: "спутник Сатурна", ur: "спутник Урана", ne: "спутник Нептуна", pl: "спутник Плутона", tno: "Транснептуновый объект"
};
function ObjParams() {
  const objs = getDivs('obj');
  let objArr = [];
  let objDct = [];
  let datesObj = {};
  for (let i = 0; i < objs.length; i += 1) {
    const classes = objs[i].className.replace('obj ', '').split(' ');
    const a = objs[i].getElementsByClassName('name')[0].getElementsByTagName("a")[0];
    const objRuName = a.text;
    const img = objs[i].getElementsByClassName('img')[0].getElementsByTagName("img")[0];
    const imgPath = img.src.split('/');
    const size = getSize(objs[i].getElementsByClassName('size')[0].innerText);
    const mass = txtMass(objs[i].getElementsByClassName('mass')[0].innerText);
    const date = objs[i].getElementsByClassName('date')[0].innerText;
    const deltaV = getDeltaV(objs[i].getElementsByClassName('delta-v')[0].innerText);
    if (!datesObj[date.slice(0, -5)])
      datesObj[date.slice(0, -5)] = [];
    datesObj[date.slice(0, -5)].push({ 'year': date.slice(6, 10), 'name': objRuName,  'img': imgPath[imgPath.length - 1], 'url': a.href });
    objDct.push({ 'name': img.alt, 'runame': objRuName, 'size': size, 'mass': mass, 'date': date, 'classes': classes });
    objArr.push([img.alt, objRuName, size, mass, date, deltaV, classes, imgPath[imgPath.length - 1]]);
  }
  console.log(datesObj);
  console.log(objArr);
  console.log(objDct);
}
function getDate(txt) {
  if (!txt) {
    return 0;
  }
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
function getDeltaV(txt) {
  return txt.includes(">") ? parseFloat(txt.substring(txt.indexOf(">") + 1, txt.length)) : parseFloat(txt);
}
function toSort(classNam) {
  let sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'size')
    sortFunction = getSize;
  else if (classNam == 'date')
    sortFunction = getDate;
  else if (classNam == 'delta-v')
    sortFunction = getDeltaV;
  doSort(sortFunction, classNam);
}
function show(divImg) {
  const obj = divImg.parentElement;
  let name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  let size = obj.getElementsByClassName("size")[0].innerText;
  size = mkPar('Радиус: ', size, '&nbsp;км');
  let mass = obj.getElementsByClassName("mass")[0].innerText;
  mass = mkPar('Масса: ', mass, '&nbsp;кг');
  let date = obj.getElementsByClassName("date")[0].innerText;
  date = mkPar('Дата открытия: ', date, '');
  let deltaV = obj.getElementsByClassName("delta-v");
  if (deltaV.length) {
    deltaV = mkPar('Δv: ', deltaV[0].innerText, '&nbsp;км/с');
  } else {
    deltaV = "";
  }
  let type = mkType(obj.className, OBJTYPES);
  type = mkPar('Типы: ', type, '');
  let desc = obj.getElementsByClassName("desc");
  if (desc.length)
    desc = mkPar('', desc[0].innerText, '');
  else
    desc = "";
  const contentToShow = divImg.innerHTML + name + type + size + mass + date + deltaV + desc;
  toShow(contentToShow);
}
function getToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return { daymon: `${day}.${month}`, month: month, year: currentdate.getFullYear() };
}
function findDate() {
  const elems = document.getElementsByClassName('date');
  const today = getToday();
  let objOfDay = [];
  let objOfMonthDiv = document.getElementById('objOfMonth');
  let objOfDayDiv = document.getElementById('objOfDay');
  for (let i = 0; i < elems.length; i += 1) {
    let daymon = elems[i].innerText.slice(0, 5);
    const mon = elems[i].innerText.slice(3, 5);
    const divName = elems[i].parentElement.getElementsByClassName('name')[0];
    const objHtml = `${divName.innerHTML}. Дата открытия: ${elems[i].innerHTML}<br>`;
    if (mon == today.month)
      objOfMonthDiv.innerHTML += objHtml;
    if (today.daymon == daymon) {
      objOfDayDiv.innerHTML += objHtml;
      objOfDay.push(objHtml);
    }
  }
  if (!objOfDay.length)
    objOfDayDiv.style.display = 'none';
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