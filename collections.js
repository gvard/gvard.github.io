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
const txtMass = txt => txt.includes("±") ? txt.substring(0, txt.indexOf("±")) + txt.substring(txt.indexOf("E")) : txt;
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
    if(a.getElementsByClassName(classNam)[0] != null) {
      var aord = sortFunction(a.getElementsByClassName(classNam)[0].innerText);
    } else {var aord = 0;}
    if(b.getElementsByClassName(classNam)[0] != null) {
      var bord = sortFunction(b.getElementsByClassName(classNam)[0].innerText);
    } else {var bord = 0;}
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
function mkType(className, OBJTYPES) {
  let type = "";
  for (let objClassNam of className.split(" ")) {
    if (objClassNam in OBJTYPES) {
      type += OBJTYPES[objClassNam] + ", ";
    }
  }
  return type.replace(/,\s*$/, "");
}
function uncheckAll(isChecked){
  let inputs = document.getElementById('props').getElementsByTagName("input");
  for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].type == 'checkbox') {
      inputs[i].checked = isChecked;
    }
  }
  showHideThis(document.getElementsByName(".obj")[0])
}
function toShow(contentToShow) {
  let contents = document.getElementById('contents');
  contents.innerHTML = contentToShow;
  let messageBox = document.getElementById('messageBox');
  let x, y;
  if (window.event) {
    x = window.event.clientX + document.documentElement.scrollLeft +
      document.body.scrollLeft;
    y = window.event.clientY + document.documentElement.scrollTop +
      document.body.scrollTop;
  } else {
    x = event.clientX + window.scrollX;
    y = event.clientY + window.scrollY;
  }
  messageBox.style.display = "block";
  x -= 5 / window.devicePixelRatio;
  y += 5 / window.devicePixelRatio;
  let xOff = messageBox.offsetWidth;
  if ((x - xOff) >= 0 && (x + xOff) >= screen.width)
    x -= xOff;
  messageBox.style.left = x + "px";
  messageBox.style.top = y + "px";
}