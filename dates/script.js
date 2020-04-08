'use strict';
function WordNumberCase(number) {
  const num = number >= 0 ? number : -number;
  let m = num % 10;
  let result;
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
    elems[i].style.display = 'block';
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
  // let slideIndex = 0;
  let elems = document.getElementsByClassName("date");
  const today = getToday();
  let toShow = [];
  for (let i = 0; i < elems.length; i += 1) {
    // let mon = elems[i].innerText.slice(3, 5);
    let year = parseInt(elems[i].innerText.slice(6, 10), 10);
    toShow.push(elems[i]);
    ago(elems[i], year, today.year);
    elems[i].parentElement.style.display = "none";
  }
  slideIndex += 1;
  if (slideIndex > elems.length)
    slideIndex = 1;
  if (toShow.length != 0)
    toShow[slideIndex - 1].parentElement.style.display = "block";
  else
    document.body.innerHTML = "<h1>Нет дат в текущем наборе событий</h1>";
  setTimeout(carousel, 3500);
}
function findDate() {
  const elems = document.getElementsByClassName('date');
  let gyear = parseInt(document.getElementById("year").value, 10);
  let gdaymon = document.getElementById("daymon").value;
  const today = getToday();
  const checkBox = document.getElementById("onlyMonth");
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
function makeArray() {
  let arr = [];
  const elems = document.getElementsByClassName('date');
  for (let i = 0; i < elems.length; i += 1) {
    let slug = elems[i].parentElement.querySelector('.slug').innerText;
    let tags = elems[i].parentElement.querySelector('.tags').innerText.substring(6,).split(/\s*,\s*/);
    let date = elems[i].innerText;
    let desc = elems[i].parentElement.querySelector('.desc');
    let descContent = desc.innerHTML.trim();
    let img = elems[i].parentElement.querySelector('.img').getElementsByTagName('img')[0];
    console.log(img.src);
    if (img.src.indexOf('http') != -1) {
      arr.push([slug, date, descContent, [img.src], [], [tags]]);
    } else {
      arr.push([slug, date, descContent, [], [img.src], [tags]]);
    }
  }
  console.log(arr);
}
