'use strict';
/*jshint esversion: 6 */
const OBJTYPES = {
  star: "звезда", pla: "планета", neo: "околоземный астероид", co: "ядро кометы", ea: "спутник Земли", mar: "спутник Марса", mab: "астероид основного пояса", dw: "карликовая планета", ju: "спутник Юпитера", sat: "спутник Сатурна", ur: "спутник Урана", ne: "спутник Нептуна", pl: "спутник Плутона", tno: "Транснептуновый объект"
};
function logger(mode: string, len: number) {
  let displayMode: string = '';
  if (mode == 'none')
    displayMode = 'Hide';
  else if (mode.includes('block'))
    displayMode = 'Show';
  console.log(displayMode, len, 'objects');
}
function showHideThis(checkBox) {
  const elems = document.querySelectorAll(checkBox.name);
  let mode: string = 'none';
  if (checkBox.checked)
    mode = 'block';
  for (let i = 0; i < elems.length; i += 1)
    elems[i].style.display = mode;
  logger(mode, elems.length);
}
function getDivs(classNam: string) {
  const mainTab = document.getElementById('tab');
  return mainTab.getElementsByClassName(classNam);
}
function getDate(txt) {
  if (!txt)
    return 0;
  return Number(txt.slice(6, 10));
}
function showHideByDate(mode: string) {
  const elems = getDivs('date');
  const yearForSort = parseInt((<HTMLInputElement> document.getElementById('year')).value, 10);
  let j = 0;
  for (let i = 0; i < elems.length; i += 1) {
    if ((<HTMLElement>elems[i]).innerText && getDate((<HTMLElement> elems[i]).innerText) > yearForSort) {
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
function getDeltaV(txt) {
  return txt.includes(">") ? parseFloat(txt.substring(txt.indexOf(">")+1, txt.length)) : parseFloat(txt);
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
    const classes = objs[i].className.replace('obj ','').split(' ');
    const a = objs[i].querySelector('.name').getElementsByTagName("a")[0];
    const img = objs[i].querySelector('.img').getElementsByTagName("img")[0];
    const imgPath = img.src.split('/'); 
    const date = (<HTMLElement> objs[i].querySelector('.date')).innerText;
    const size = getSize((<HTMLElement> objs[i].querySelector('.size')).innerText);
    const mass = txtMass((<HTMLElement> objs[i].querySelector('.mass')).innerText);
    const objRuName = a.text;
    // let objName = a.href.split("/");
    // if (objName.length == 6)
    //   objName = objName[objName.length - 2] + "/" + objName[objName.length - 1];
    // else
    //   objName = objName[objName.length - 1];
    objDct.push({'name': img.alt, 'runame': objRuName, 'size': size, 'mass': mass, 'date': date, 'classes': classes});
    objArr.push([img.alt, objRuName, size, mass, date, classes, imgPath[imgPath.length - 1]]);
  }
  console.log(objArr);
  console.log(objDct);
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
  else if (classNam == 'delta-v')
    sortFunction = getDeltaV;
  ArrToSort.sort(function(a, b) {
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
  if (deltaV.length)
    deltaV = mkPar('Δv: ', deltaV[0].innerText, '&nbsp;км/с');
  else
    deltaV = "";
  let desc = obj.getElementsByClassName("desc");
  if (desc.length)
    desc = mkPar('', desc[0].innerText, '');
  else
    desc = "";
  return name + type + size + mass + date + deltaV + desc;
}
function show(divImg) {
  const obj = divImg.parentElement;
  let contents = document.getElementById('contents');
  contents.innerHTML = `${divImg.innerHTML}${mkContents(obj)}`;
  var messageBox = document.getElementById('messageBox');
  let x, y;
  if (window.event) {
    x = (<any>window).event.clientX + document.documentElement.scrollLeft +
        document.body.scrollLeft;
    y = (<any>window).event.clientY + document.documentElement.scrollTop +
        document.body.scrollTop;
  }
  else {
    x =  (<any> event).clientX + window.scrollX;
    y =  (<any> event).clientY + window.scrollY;
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
    total += getSize((<HTMLElement> elems[i]).innerText);
    console.log(`For ${j} elements sum of sizes is ${total} km`);
  }
}
function getToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return {daymon: `${day}.${month}`, month: month, year: currentdate.getFullYear()};
}
/**
 * Find objects with discovery dates which equals current day and month values.
 */
function findDate() {
  const elems = document.getElementsByClassName('date');
  const today = getToday();
  let objOfDay = [];
  let objOfMonthDiv = document.getElementById('objOfMonth');
  let objOfDayDiv = document.getElementById('objOfDay');
  for (let i = 0; i < elems.length; i += 1) {
    let daymon = (<HTMLElement> elems[i]).innerText.slice(0, 5);
    const mon = (<HTMLElement> elems[i]).innerText.slice(3, 5);
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