"use strict";
/*jshint esversion: 6 */
const OBJTYPES = {
  dE: "Карликовая эллиптическая галактика",
  SBm: "Магелланова спиральная галактика с баром",
  SB: "Спиральная галактика с баром",
  SA: "Спиральная галактика без бара",
  Im: "Неправильная галактика",
  IB: "Неправильная галактика с баром",
  MWsat: "Галактика - спутник Млечного пути",
  M31sat: "Галактика - спутник M31"
};
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
  angular = mkPar('Угловые размеры: ', angular, '&nbsp;');
  let size = obj.getElementsByClassName("size")[0].innerText;
  size = mkPar('Диаметр: ', size, '&nbsp;kpc');
  let mass = obj.getElementsByClassName("mass")[0].innerHTML;
  mass = mkPar('Масса: ', mass, '&nbsp;M<sub>☉</sub>');
  let gType = obj.getElementsByClassName("class")[0].innerText;
  gType = mkPar('Морфологический тип: ', gType, '');
  let dist = obj.getElementsByClassName("dist")[0].innerText;
  dist = mkPar('Расстояние: ', dist, '&nbsp;kpc');
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
  const contentToShow = `<img src="${imgPth}"><h2>${name}</h2>` + type + angular + size + mass + gType + dist + desc;
  toShow(contentToShow);
}