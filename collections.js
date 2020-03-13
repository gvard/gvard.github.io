"use strict";
function logger(mode, len) {
  let displayMode = '';
  if (mode == 'none') {
    displayMode = 'Hide';
  } else if (mode.includes('block')) {
    displayMode = 'Show';
  }
  console.log(displayMode, len, 'objects');
}
function showHideThis(checkBox) {
  const elems = document.querySelectorAll(checkBox.name);
  let mode = 'none';
  if (checkBox.checked) {
    mode = 'block';
  }
  for (let i = 0; i < elems.length; i += 1) {
    elems[i].style.display = mode;
  }
  logger(mode, elems.length);
}
function getDivs(classNam) {
  const mainTab = document.getElementById('tab');
  return mainTab.getElementsByClassName(classNam);
}
function getMass(txt) {
  if (!txt) {
    return 0;
  }
  return txt.includes("±") ? Number(txt.substring(0, txt.indexOf("±")) + txt.substring(txt.indexOf("E"))) : Number(txt);
}
const txtMass = (txt) => txt.includes("±") ? txt.substring(0, txt.indexOf("±")) + txt.substring(txt.indexOf("E")) : txt;
function getSize(txt) {
  let num = 0;
  if (txt.includes("±")) {
    num = parseFloat(txt.substring(0, txt.indexOf("±")));
  } else if (txt.includes("−")) {
    num = parseFloat(txt.substring(0, txt.indexOf("−")));
  } else {
    num = parseFloat(txt);
  }
  return Number(num);
}
function doSort(sortFunction, classNam) {
  const objToSort = getDivs('obj');
  let ArrToSort = Array.prototype.slice.call(objToSort, 0);
  ArrToSort.sort((a, b) => {
    let aord = sortFunction(a.getElementsByClassName(classNam)[0].innerText);
    let bord = sortFunction(b.getElementsByClassName(classNam)[0].innerText);
    return (aord > bord) ? 1 : -1;
  });
  let parent = document.getElementById('tab');
  parent.innerHTML = "";
  for (let i = 0, l = ArrToSort.length; i < l; i += 1)
    parent.appendChild(ArrToSort[i]);
}
function hide() {
  let messageBox = document.getElementById('messageBox');
  messageBox.style.display = 'none';
}
const mkPar = (before, txt, after) => (!txt) ? '' : `<p>${before}${txt}${after}</p>`;