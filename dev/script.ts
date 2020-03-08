'use strict';
/*jshint esversion: 6 */
function calc() {
  const a = parseFloat((<HTMLInputElement> document.getElementById('val1')).value);
  const b = parseFloat((<HTMLInputElement> document.getElementById('val2')).value);
  const act = (<HTMLInputElement> document.getElementById('operator')).value;
  let result;
  if (act == 'add')
    result = a + b;
  else if (act == 'min')
    result = a - b;
  else if (act == 'mul')
    result = a * b;
  else if (act == 'div')
    result = a / b;
  document.getElementById('result').innerHTML = result;
  console.log('Числа:', a, b);
  console.log('Результат:', result);
}
function showHidePar(mode: string) {
  const elems = document.querySelectorAll("p");
  for (let i = 0; i < elems.length; i += 1)
    elems[i].style.display = mode;
}
function changeDirection(checkBox) {
  let flexContainer = document.getElementById('flexContainer');
  if (checkBox.checked)
    flexContainer.style.flexDirection = 'column';
  else
    flexContainer.style.flexDirection = 'row';
}
