'use strict';
function WordNumberCase(number) {
  var num = number >= 0 ? number : -number;
  var m = num % 10;
  var result;
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
  var elems = document.getElementsByClassName('wrap');
  for (var i = 0; i < elems.length; i += 1) {
    elems[i].style.display = 'block';
  }
}
function getToday() {
  var currentdate = new Date();
  var day = ("0" + currentdate.getDate()).slice(-2);
  var month = ("0" + (currentdate.getMonth() + 1)).slice(-2);
  return { daymon: day + "." + month, month: month, year: currentdate.getFullYear() };
}
function ago(elem, year, fullyear) {
  var yearsAgo = elem.parentElement.getElementsByClassName('ago')[0];
  var yr = fullyear - year;
  if (yr)
    yearsAgo.innerText = yr + " " + WordNumberCase(yr) + " ";
  else
    yearsAgo.innerText = "";
}
function carousel() {
  var slideIndex = 0;
  var elems = document.getElementsByClassName("date");
  var today = getToday();
  var toShow = [];
  for (var i = 0; i < elems.length; i += 1) {
    var mon = elems[i].innerText.slice(3, 5);
    var year = parseInt(elems[i].innerText.slice(6, 10), 10);
    if (mon == today.month)
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
    document.body.innerHTML = "<h1>Нет дат за текущий месяц</h1>";
  setTimeout(carousel, 6000);
}
function findDate() {
  var elems = document.getElementsByClassName('date');
  var gyear = parseInt(document.getElementById("year").value, 10);
  var gdaymon = document.getElementById("daymon").value;
  var today = getToday();
  var checkBox = document.getElementById("onlyMonth");
  if (checkBox.checked == true) {
    var month = today.month;
    console.log("Show events occured in month number", month);
  }
  if (!gdaymon)
    gdaymon = today.daymon;
  for (var i = 0; i < elems.length; i += 1) {
    var daymon = elems[i].innerText.slice(0, 5);
    var mon = elems[i].innerText.slice(3, 5);
    var year = parseInt(elems[i].innerText.slice(6, 10), 10);
    ago(elems[i], year, today.year);
    var vis = 'none';
    if ((checkBox.checked && mon == today.month) ||
      (!checkBox.checked && gyear && gdaymon == daymon && gyear == year) ||
      (!checkBox.checked && !gyear && gdaymon == daymon))
      vis = 'block';
    elems[i].parentElement.style.display = vis;
  }
}
function makeArray() {
  var arr = [];
  var elems = document.getElementsByClassName('date');
  for (var i = 0; i < elems.length; i += 1) {
    var date = elems[i].innerText;
    var desc = elems[i].parentElement.querySelector('.desc');
    var img = desc.querySelector('img');
    arr.push(["", date, desc.innerText.trim(), [img.src], ['tmp']]);
  }
  console.log(arr);
}
