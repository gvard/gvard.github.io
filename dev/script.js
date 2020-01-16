"use strict";
/*jshint esversion: 6 */
function calc() {
  const a = parseFloat(document.querySelector('#val1').value);
  const b = parseFloat(document.querySelector('#val2').value);
  const act = document.querySelector('#operator').value;
  let result;
  if (act == 'add')
    result = a + b;
  else if (act == 'min')
    result = a - b;
  else if (act == 'mul')
    result = a * b;
  else if (act == 'div')
    result = a / b;
  document.querySelector('#result').innerHTML = result;
  console.log('Числа:', a, b);
  console.log('Результат:', result);
}
function showHidePar(mode) {
  var elems = document.querySelectorAll("p");
  for (let i = 0; i < elems.length; i++)
    elems[i].style.display = mode;
}
function changeDirection(checkBox) {
  var flexContainer = document.getElementById('flex-container');
  if (checkBox.checked)
    flexContainer.style.flexDirection = 'column';
  else
    flexContainer.style.flexDirection = 'row';
}
