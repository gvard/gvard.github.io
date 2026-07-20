document.addEventListener('DOMContentLoaded', () => {
const grid = document.getElementById('tab');
grid.addEventListener('mouseover', (event) => {
  const imgDiv = event.target.closest('.obj .img');
  if (imgDiv) {
    const baseImg = imgDiv.querySelector('.img img');
    let finalImgUrl;
    const imgData = imgDiv.dataset.b;
    if (!imgData) {
      finalImgUrl = baseImg.getAttribute('src');
    }
    else if (imgData.startsWith('http')) {
      finalImgUrl = imgData;
    }
    else {
      finalImgUrl = `../images/${imgData}`;
    }
  show(event, imgDiv, finalImgUrl);
  }
});
grid.addEventListener('mouseout', (event) => {
  const imgDiv = event.target.closest('.obj .img');
  const relatedTarget = event.relatedTarget ? event.relatedTarget.closest('.obj .img') : null;
  if (imgDiv && imgDiv !== relatedTarget) {
    hide();
  }
});
});
