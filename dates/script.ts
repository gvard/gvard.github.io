'use strict';
/*jshint esversion: 6 */
function WordNumberCase(number) {
  const num = number >= 0 ? number : -number;
  let m = num % 10;
  let result: string;
  switch (m) {
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
  return result;
}
function showAll() {
  const elems = document.getElementsByClassName('wrap');
  for (let i = 0; i < elems.length; i += 1) {
    (<HTMLElement> elems[i]).style.display = 'block';
    // console.log(elems[i].getElementsByClassName('date')[0].innerText);
  }
}
function getToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return { daymon: `${day}.${month}`, month: month, year: currentdate.getFullYear() };
}
function getStrToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = currentdate.getMonth() + 1;
  let monthName = { 1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая",
  6: "июня", 7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря" }[month];
  return `${day} ${monthName} ${currentdate.getFullYear()}`;
}
function mkHeader() {
  let header = document.getElementById('header');
  header.innerHTML = getStrToday();
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
  let slideIndex = 0;
  let elems = document.getElementsByClassName("date");
  const today = getToday();
  let toShow = [];
  for (let i = 0; i < elems.length; i += 1) {
    // let daymon = elems[i].innerText.slice(0, 5);
    let mon = (<HTMLElement> elems[i]).innerText.slice(3, 5);
    let year = parseInt((<HTMLElement> elems[i]).innerText.slice(6, 10), 10);
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
    toShow[slideIndex - 1].parentElement.style.display = "block";
  else
    document.body.innerHTML = "<h1>Нет дат за текущий месяц</h1>";
  setTimeout(carousel, 6000);
}
function findDate() {
  const elems = document.getElementsByClassName('date');
  let gyear = parseInt((<HTMLInputElement> document.getElementById("year")).value, 10);
  let gdaymon = (<HTMLInputElement> document.getElementById("daymon")).value;
  const today = getToday();
  const checkBox = <HTMLInputElement> document.getElementById("onlyMonth");
  if (checkBox.checked == true) {
    const month = today.month;
    console.log("Show events occured in month number", month);
  }
  if (!gdaymon)
    gdaymon = today.daymon;
  for (let i = 0; i < elems.length; i += 1) {
    let daymon = (<HTMLElement> elems[i]).innerText.slice(0, 5);
    let mon = (<HTMLElement> elems[i]).innerText.slice(3, 5);
    let year = parseInt((<HTMLElement> elems[i]).innerText.slice(6, 10), 10);
    ago(elems[i], year, today.year);
    let vis = 'none';
    if ((checkBox.checked && mon == today.month) ||
        (!checkBox.checked && gyear && gdaymon == daymon && gyear == year) ||
        (!checkBox.checked && !gyear && gdaymon == daymon))
      vis = 'block';
    elems[i].parentElement.style.display = vis;
  }
}
function makeArray() {
  let arr = [];
  const elems = document.getElementsByClassName('date');
  for (let i = 0; i < elems.length; i += 1) {
    let date = (<HTMLElement> elems[i]).innerText;
    let desc = elems[i].parentElement.querySelector('.desc');
    let img = desc.querySelector('img');
    arr.push(["", date, (<HTMLElement> desc).innerText.trim(), [img.src], ['tmp']]);
  }
  console.log(arr);
}
