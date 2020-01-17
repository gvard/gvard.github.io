'use strict';
/*jshint esversion: 6 */
function WordNumberCase(number) {
  var result;
  var num = number >= 0 ? number : -number;
  var m = num % 10;
  switch(m) {
    case 1:
      result = "год";
      break;
    case 2:
    case 3:
    case 4:
      result = "года";
      break;
    default:
      result = "лет";
      break;
  }
  if (m >= 1 && m <= 4) {
    m = num % 100;
    if (m >= 11 && m <= 14)
      result = "лет";
  }
  // `${number} ${result}`;
  return result;
}
function showAll() {
  const elems = document.getElementsByClassName('wrap');
  for (let i = 0; i < elems.length; i += 1) {
    elems[i].style.display = 'block';
    // console.log(elems[i].getElementsByClassName('date')[0].innerText);
  }
}
function getToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return {daymon: `${day}.${month}`, month: month, year: currentdate.getFullYear()};
}
function ago(elem, year, fullyear) {
  let yearsAgo = elem.parentElement.getElementsByClassName('ago')[0];
  const yr = fullyear - year;
  if (yr)
    yearsAgo.innerText = `${yr} ${WordNumberCase(yr)} `;
  else
    yearsAgo.innerText = ``;
}
function carousel() {
  var slideIndex = 0;
  var elems = document.getElementsByClassName("date");
  const today = getToday();
  var toShow = [];
  for (let i = 0; i < elems.length; i += 1) {
    // let daymon = elems[i].innerText.slice(0, 5);
    let mon = elems[i].innerText.slice(3, 5);
    let year = parseInt(elems[i].innerText.slice(6, 10), 10);
    if (mon == today.month)
      toShow.push(elems[i]);
    ago(elems[i], year, today.year);
    elems[i].parentElement.style.display = "none";
  }
  slideIndex += 1;
  // let mon = elems[slideIndex].innerText.slice(3, 5);
  if (slideIndex > elems.length)
    slideIndex = 1;
  if (toShow.length != 0)
    toShow[slideIndex-1].parentElement.style.display = "block"; 
  else
    document.body.innerHTML = "<h1>Нет дат за текущий месяц</h1>"
  setTimeout(carousel, 6000); 
}
function findDate() {
  const elems = document.getElementsByClassName('date');
  let gyear = parseInt(document.getElementById("year").value, 10);
  let gdaymon = document.getElementById("daymon").value;
  const today = getToday();
  var checkBox = document.getElementById("onlyMonth");
  if (checkBox.checked == true) {
    const month = today.month;
    console.log("Show events occured in month number", month);
  }
  if (!gdaymon)
    gdaymon = today.daymon;
  for (let i = 0; i < elems.length; i += 1) {
    let daymon = elems[i].innerText.slice(0, 5);
    let mon = elems[i].innerText.slice(3, 5);
    let year = parseInt(elems[i].innerText.slice(6, 10), 10);
    ago(elems[i], year, today.year);
    let vis = 'none';
    if ((checkBox.checked && mon == today.month) ||
        (!checkBox.checked && gyear && gdaymon == daymon && gyear == year) ||
        (!checkBox.checked && !gyear && gdaymon == daymon))
      vis = 'block';
    elems[i].parentElement.style.display = vis;
  }
}