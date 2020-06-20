'use strict';
function getStrToday() {
  const currentdate = new Date();
  const day = ("0" + currentdate.getDate()).slice(-2);
  const month = currentdate.getMonth() + 1;
  let monthName = { 1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая",
    6: "июня", 7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря" }[month];
  return `${day} ${monthName} ${currentdate.getFullYear()}`;
}
const mkHeader = () => document.getElementById('header').innerHTML = getStrToday()