'use strict';
function copyCode(textId) {
  const copiedText = document.getElementById(textId).innerText;
  let txtAr = document.createElement("textArea");
  txtAr.style.position = 'fixed';
  txtAr.style.top = 0;
  txtAr.style.left = 0;
  txtAr.style.width = '0.1em';
  txtAr.style.height = '0.1em';
  txtAr.style.padding = 0;
  txtAr.style.border = 'none';
  txtAr.style.outline = 'none';
  txtAr.style.boxShadow = 'none';
  txtAr.style.background = 'transparent';
  txtAr.value = copiedText;
  document.body.appendChild(txtAr);
  txtAr.focus();
  txtAr.select();
  document.execCommand("copy");
  document.body.removeChild(txtAr);
}