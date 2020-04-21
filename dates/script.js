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
function getSlidesByDate() {
  let toShow = [];
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
    if ((gdaymon.value.indexOf(".") == -1 && mon == gdaymon.value) ||
      (gyear.value == year && gdaymon.value == daymon) ||
      (!gyear.value && gdaymon.value == daymon) ||
      (gyear.value == year && !gdaymon.value) ||
      (!gyear.value && !gdaymon.value))
      {
        const elmAgo = elems[i].parentElement.getElementsByClassName('ago')[0];
        setAgo(elmAgo, today.year - year);
        j += 1;
        toShow.push(elems[i].parentElement);
      }
  }
  console.log("Select", j, "events");
  return toShow;
}
function getSlidesByTag(tag) {
  const today = getToday();
  let toShow = [];
  if (!tag) tag = 'wrap';
  const elems = document.getElementsByClassName(tag);
  console.log("Всего слайдов:", elems.length);
  for (let i = 0; i < elems.length; i += 1) {
    const year = parseInt(elems[i].getElementsByClassName("date")[0].innerText.slice(6, 10), 10);
    const elmAgo = elems[i].getElementsByClassName('ago')[0];
    setAgo(elmAgo, today.year - year);
    toShow.push(elems[i]);
  }
  return toShow;
}
const hideAll = () => {document.querySelectorAll('.wrap').forEach(el => el.style.display = 'none');};
const showAll = elems => { elems.forEach(el => el.style.display = 'block');};
function showByTag(tag) {
  hideAll();
  document.getElementById('head').style.display = 'none';
  if (!tag)
    tag = document.getElementById("tag").value;
  const elems = getSlidesByTag(tag);
  showAll(elems);
}
function showByDate() {
  hideAll();
  document.getElementById('head').style.display = 'none';
  const elems = getSlidesByDate();
  console.log(elems.length);
  showAll(elems);
}
function setSlideStyle() {
  document.getElementsByClassName('right')[0].style.display = 'none';
  document.getElementById('head').style.display = 'none';
  document.getElementsByClassName('left')[0].style.width = '100%';
}
function runSlides(elems) {
  let slideIndex = 0;
  const tmout = document.getElementById("tmout").value;
  elems[slideIndex].style.display = 'block';
  setInterval(function() {
    elems[slideIndex].style.display = 'none';
    slideIndex = (slideIndex + 1) % elems.length;
    elems[slideIndex].style.display = 'block';
  }, tmout);
}
function slidesByDate() {
  hideAll();
  setSlideStyle();
  const elems = getSlidesByDate();
  runSlides(elems);
}
function slidesByTag(tag) {
  hideAll();
  setSlideStyle();
  if (!tag)
    tag = document.getElementById("tag").value;
  const elems = getSlidesByTag(tag);
  runSlides(elems);
}
function makeArray() {
  let arr = [];
  let datesObj = {};
  const elems = document.getElementsByClassName('date');
  for (let i = 0; i < elems.length; i += 1) {
    let slug = elems[i].parentElement.querySelector('.slug').innerText;
    let tags = elems[i].parentElement.className.substring(5,);
    let date = elems[i].innerText;
    let desc = elems[i].parentElement.querySelector('.desc');
    let descContent = desc.innerText.trim();
    let img = elems[i].parentElement.querySelector('.img').getElementsByTagName('img')[0];
    if (!datesObj[date.slice(0, -5)])
      datesObj[date.slice(0, -5)] = [];
    datesObj[date.slice(0, -5)].push({ 'year': date.slice(6, 10), 'slug': slug, 'tags': tags, 'img': img.src, 'desc': descContent });
    if (img.src.indexOf('http') != -1) {
      arr.push([slug, date, descContent, [img.src], [], tags]);
    } else {
      arr.push([slug, date, descContent, [], [img.src.substring(img.src.lastIndexOf('/')+1)], tags]);
    }
  }
  console.log(datesObj);
}
function mergeDataSets(data, dataToAdd) {
  for (let daymon in dataToAdd) {
    if (daymon in data) {
      for (let dat of dataToAdd[daymon])
      data[daymon].push(dat);
    } else {
      data[daymon] = dataToAdd[daymon];
    }
  }
  console.log(data);
}