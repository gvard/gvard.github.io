'use strict';
var OBJTYPES = {
  star: "звезда", pla: "планета", neo: "околоземный астероид", co: "ядро кометы", ea: "спутник Земли", mar: "спутник Марса", mab: "астероид основного пояса", dw: "карликовая планета", ju: "спутник Юпитера", sat: "спутник Сатурна", ur: "спутник Урана", ne: "спутник Нептуна", pl: "спутник Плутона", tno: "Транснептуновый объект"
};
function logger(mode, len) {
  var displayMode = '';
  if (mode == 'none')
    displayMode = 'Hide';
  else if (mode.indexOf('block') != -1)
    displayMode = 'Show';
  console.log(displayMode, len, 'objects');
}
function showHideThis(checkBox) {
  var elems = document.querySelectorAll(checkBox.name);
  var mode = 'none';
  if (checkBox.checked)
    mode = 'block';
  for (var i = 0; i < elems.length; i += 1)
    elems[i].style.display = mode;
  logger(mode, elems.length);
}
function getDivs(classNam) {
  var mainTab = document.getElementsByClassName('tab main')[0];
  return mainTab.getElementsByClassName(classNam);
}
function getDate(txt) {
  if (!txt)
    return 0;
  return Number(txt.slice(6, 10));
}
function showHideByDate(mode) {
  var elems = getDivs('date');
  var yearForSort = parseInt(document.getElementById('year').value, 10);
  var j = 0;
  for (var i = 0; i < elems.length; i += 1) {
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
function getDeltaV(txt) {
  return txt.includes(">") ? parseFloat(txt.substring(txt.indexOf(">") + 1, txt.length)) : parseFloat(txt);
}
function getSize(txt) {
  var num = 0;
  if (txt.includes("±"))
    num = parseFloat(txt.substring(0, txt.indexOf("±")));
  else if (txt.includes("−"))
    num = parseFloat(txt.substring(0, txt.indexOf("−")));
  else
    num = parseFloat(txt);
  return Number(num);
}
function ObjParams() {
  var objs = getDivs('obj');
  var objArr = [];
  var objDct = [];
  for (var i = 0; i < objs.length; i += 1) {
    var classes = objs[i].className.replace('obj ', '').split(' ');
    var a = objs[i].querySelector('.name').getElementsByTagName("a")[0];
    var img = objs[i].querySelector('.img').getElementsByTagName("img")[0];
    var imgPath = img.src.split('/');
    var date = objs[i].querySelector('.date').innerText;
    var size = getSize(objs[i].querySelector('.size').innerText);
    var mass = txtMass(objs[i].querySelector('.mass').innerText);
    var objRuName = a.text;
    // let objName = a.href.split("/");
    // if (objName.length == 6)
    //   objName = objName[objName.length - 2] + "/" + objName[objName.length - 1];
    // else
    //   objName = objName[objName.length - 1];
    objDct.push({ 'name': img.alt, 'runame': objRuName, 'size': size, 'mass': mass, 'date': date, 'classes': classes });
    objArr.push([img.alt, objRuName, size, mass, date, classes, imgPath[imgPath.length - 1]]);
  }
  console.log(objArr);
  console.log(objDct);
}
function toSort(classNam) {
  var objToSort = getDivs('obj');
  var ArrToSort = Array.prototype.slice.call(objToSort, 0);
  var sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'date')
    sortFunction = getDate;
  else if (classNam == 'size')
    sortFunction = getSize;
  else if (classNam == 'delta-v')
    sortFunction = getDeltaV;
  ArrToSort.sort(function (a, b) {
    var aord = sortFunction(a.getElementsByClassName(classNam)[0].innerText);
    var bord = sortFunction(b.getElementsByClassName(classNam)[0].innerText);
    return (aord > bord) ? 1 : -1;
  });
  var parent = document.getElementsByClassName('main')[0];
  parent.innerHTML = "";
  for (var i = 0, l = ArrToSort.length; i < l; i += 1)
    parent.appendChild(ArrToSort[i]);
}
function hide() {
  var messageBox = document.getElementById('messageBox');
  messageBox.style.display = 'none';
}
function mkPar(before, txt, after) {
  return (!txt) ? '' : "<p>" + before + txt + after + "</p>";
}
function mkContents(obj) {
  var name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  var size = obj.getElementsByClassName("size")[0].innerText;
  size = mkPar('Радиус: ', size, '&nbsp;км');
  var mass = obj.getElementsByClassName("mass")[0].innerText;
  mass = mkPar('Масса: ', mass, '&nbsp;кг');
  var date = obj.getElementsByClassName("date")[0].innerText;
  date = mkPar('Дата открытия: ', date, '');
  var type = "";
  for (var _i = 0, _a = obj.className.split(" "); _i < _a.length; _i++) {
    var objClassNam = _a[_i];
    if (objClassNam in OBJTYPES)
      type = OBJTYPES[objClassNam];
  }
  type = mkPar('Тип: ', type, '');
  var deltaV = obj.getElementsByClassName("delta-v");
  if (deltaV.length)
    deltaV = mkPar('Δv: ', deltaV[0].innerText, '&nbsp;км/с');
  else
    deltaV = "";
  var desc = obj.getElementsByClassName("desc");
  if (desc.length)
    desc = mkPar('', desc[0].innerText, '');
  else
    desc = "";
  return name + type + size + mass + date + deltaV + desc;
}
function show(divImg) {
  var obj = divImg.parentElement;
  var contents = document.getElementById('contents');
  contents.innerHTML = "" + divImg.innerHTML + mkContents(obj);
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
  var elems = document.getElementsByClassName(classNam);
  var total = 0;
  var j = 0;
  for (var i = 0; i < elems.length; i += 1) {
    j += 1;
    total += getSize(elems[i].innerText);
    console.log("For " + j + " elements sum of sizes is " + total + " km");
  }
}
function getToday() {
  var currentdate = new Date();
  var day = ("0" + currentdate.getDate()).slice(-2);
  var month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return { daymon: day + "." + month, month: month, year: currentdate.getFullYear() };
}
/**
 * Find objects with discovery dates which equals current day and month values.
 */
function findDate() {
  var elems = document.getElementsByClassName('date');
  var today = getToday();
  var objOfDay = [];
  var objOfMonthDiv = document.getElementById('objOfMonth');
  var objOfDayDiv = document.getElementById('objOfDay');
  for (var i = 0; i < elems.length; i += 1) {
    var daymon = elems[i].innerText.slice(0, 5);
    var mon = elems[i].innerText.slice(3, 5);
    var divName = elems[i].parentElement.getElementsByClassName('name')[0];
    var objHtml = divName.innerHTML + ". \u0414\u0430\u0442\u0430 \u043E\u0442\u043A\u0440\u044B\u0442\u0438\u044F: " + elems[i].innerHTML + "<br>";
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
