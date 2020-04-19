"use strict";
/*jshint esversion: 6 */
const OBJTYPES = {
  gc: "Шаровое звёздное скопление",
};
function toSort(classNam) {
  let sortFunction;
  if (classNam == 'mass')
    sortFunction = getMass;
  else if (classNam == 'size')
    sortFunction = getSize;
  doSort(sortFunction, classNam);
}
function show(divImg) {
  const obj = divImg.parentElement;
  let name = obj.getElementsByClassName("name")[0].getElementsByTagName("a")[0].innerText;
  name = mkPar('<b>', name, '</b>');
  let angular = obj.getElementsByClassName("angular")[0].innerText;
  angular = mkPar('Угловые размеры: ', angular, '&nbsp;');
  let dist = obj.getElementsByClassName("dist")[0].innerText;
  dist = mkPar('Расстояние: ', dist, '&nbsp;kpc');
  let mass = obj.getElementsByClassName("mass")[0].innerHTML;
  mass = mkPar('Масса: ', mass, '&nbsp;M<sub>☉</sub>');
  let age = obj.getElementsByClassName("age")[0].innerText;
  age = mkPar('Возраст: ', age, '&nbsp;Gyr');
  let mag = obj.getElementsByClassName("mag")[0].innerText;
  mag = mkPar('Звездная величина: ', mag, '&nbsp;m');
  let type = mkType(obj.className, OBJTYPES);
  type = mkPar('Типы: ', type, '');
  let desc = obj.getElementsByClassName("desc");
  if (desc.length) {
    desc = mkPar('', desc[0].innerText, '');
  } else {
    desc = "";
  }
  const contentToShow = divImg.innerHTML + name + type + angular + dist + mass + age + mag + desc;
  toShow(contentToShow);
}