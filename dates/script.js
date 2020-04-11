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
function getToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return { daymon: `${day}.${month}`, month: month, year: currentdate.getFullYear() };
}
const setAgo = (elmAgo, yr) => { if (yr) elmAgo.innerText = `${yr} ${WordNumberCase(yr)} `;};
function showByTag() {
  const elems = document.getElementsByClassName('wrap');
  const tagVal = document.getElementById("tag").value;
  const today = getToday();
  let j = 0;
  for (let i = 0; i < elems.length; i += 1) {
    let vis = 'none';
    if (elems[i].classList.contains(tagVal)) {
      const elmDate = elems[i].getElementsByClassName('date')[0];
      const year = parseInt(elmDate.innerText.slice(6, 10), 10);
      const elmAgo = elmDate.parentElement.getElementsByClassName('ago')[0];
      setAgo(elmAgo, today.year - year);
      vis = 'block';
      j += 1;
    }
    elems[i].style.display = vis;
  }
  console.log("Select", j, "events");
}
function carousel() {
  const elems = document.getElementsByClassName("date");
  const tmout = document.getElementById("tmout");
  const today = getToday();
  let toShow = [];
  for (let i = 0; i < elems.length; i += 1) {
    const year = parseInt(elems[i].innerText.slice(6, 10), 10);
    const elmAgo = elems[i].parentElement.getElementsByClassName('ago')[0];
    setAgo(elmAgo, today.year - year);
    toShow.push(elems[i]);
    elems[i].parentElement.style.display = "none";
  }
  slideIndex += 1;
  if (slideIndex > elems.length)
    slideIndex = 1;
  if (toShow.length != 0)
    toShow[slideIndex - 1].parentElement.style.display = "block";
  else
    document.body.innerHTML = "<h1>Нет дат в текущем наборе событий</h1>";
  setTimeout(carousel, tmout.value);
}
function findDates() {
  const elems = document.getElementsByClassName('date');
  const gyear = document.getElementById("year");
  const gdaymon = document.getElementById("daymon");
  const today = getToday();
  const chckToday = document.getElementById("today");
  const chckYr = document.getElementById("thisYear");
  if (chckToday.checked) gdaymon.value = today.daymon;
  if (chckYr.checked) gyear.value = today.year;
  let j = 0;
  for (let i = 0; i < elems.length; i += 1) {
    let daymon = elems[i].innerText.slice(0, 5);
    let mon = elems[i].innerText.slice(3, 5);
    let year = parseInt(elems[i].innerText.slice(6, 10), 10);
    let vis = 'none';
    if ((gdaymon.value.indexOf(".") == -1 && mon == gdaymon.value) ||
      (gyear.value == year && gdaymon.value == daymon) ||
      (!gyear.value && gdaymon.value == daymon) ||
      (gyear.value == year && !gdaymon.value) ||
      (!gyear.value && !gdaymon.value))
      {
        const elmAgo = elems[i].parentElement.getElementsByClassName('ago')[0];
        setAgo(elmAgo, today.year - year);
        vis = 'block';
        j += 1;
      }
    elems[i].parentElement.style.display = vis;
  }
  console.log("Select", j, "events");
}
function makeArray() {
  let arr = [];
  const elems = document.getElementsByClassName('date');
  for (let i = 0; i < elems.length; i += 1) {
    let slug = elems[i].parentElement.querySelector('.slug').innerText;
    let tags = elems[i].parentElement.querySelector('.tags').innerText.substring(6,).split(/\s*,\s*/);
    let date = elems[i].innerText;
    let desc = elems[i].parentElement.querySelector('.desc');
    let descContent = desc.innerHTML.trim().substring(29,).slice(0, -4);
    let img = elems[i].parentElement.querySelector('.img').getElementsByTagName('img')[0];
    if (img.src.indexOf('http') != -1) {
      arr.push([slug, date, descContent, [img.src], [], tags]);
    } else {
      arr.push([slug, date, descContent, [], [img.src.substring(img.src.lastIndexOf('/')+1)], tags]);
    }
  }
  console.log(arr);
}
var slideIndex = 0;
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('caro').addEventListener('click', function() {
    document.getElementsByClassName('right')[0].style.display = 'none';
    document.getElementById('head').style.display = 'none';
    document.getElementsByClassName('left')[0].style.width = '100%';
    carousel();
  });
});