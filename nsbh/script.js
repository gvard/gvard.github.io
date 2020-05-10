"use strict";
/*jshint esversion: 6 */
const OBJTYPES = {
  bh: "Кандидат в черные дыры",
};
function toSort(classNam) {
  let sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  doSort(sortFunction, classNam);
}
function show(divImg) {
  const obj = divImg.parentElement;
  let name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  let dist = obj.getElementsByClassName("dist")[0].innerText;
  dist = mkPar('Расстояние: ', dist, '&nbsp;пк');
  let mass = obj.getElementsByClassName("mass")[0].innerText;
  mass = mkPar('Масса: ', mass, '&nbsp;M<sub>☉</sub>');
  let type = mkType(obj.className, OBJTYPES);
  type = mkPar('Типы: ', type, '');
  let desc = obj.getElementsByClassName("desc");
  if (desc.length) {
    desc = mkPar('', desc[0].innerText, '');
  } else {
    desc = "";
  }
  const contentToShow = divImg.innerHTML + name + type + dist + mass + desc;
  toShow(contentToShow);
}