// scripts here:
// https://www.sitepoint.com/simple-javascript-quiz/
// https://codepen.io/harrysadlermusic/pen/DihjK
function submitQuiz() {
  console.log('submitted');

  // get each answer score
  function answerScore(qName) {
    const radiosNo = document.getElementsByName(qName);

    for (let i = 0, length = radiosNo.length; i < length; i++) {
      if (radiosNo[i].checked) {
      // do something with radiosNo
        var answerValue = Number(radiosNo[i].value);
      }
    }
    // change NaNs to zero
    if (isNaN(answerValue))
      answerValue = 0;
    return answerValue;
  }
  // calc score with answerScore function
  var calcScore = (answerScore('q1') + answerScore('q2') + answerScore('q3') + answerScore('q4'));
  console.log("CalcScore: " + calcScore); // it works!

  // function to return correct answer string
  function correctAnswer(correctStringNo, qNumber) {
    console.log("qNumber: " + qNumber);  // logs 1,2,3,4 after called below
    return ("Правильный ответ &ndash; #" + qNumber + ": &nbsp;<strong>" +
      (document.getElementById(correctStringNo).innerHTML) + "</strong>");
  }

  // print correct answers only if wrong (calls correctAnswer function)
  if (answerScore('q1') === 0) {
    document.getElementById('correctAnswer1').innerHTML = correctAnswer('correctString1', 1);
  }
  if (answerScore('q2') === 0) {
    document.getElementById('correctAnswer2').innerHTML = correctAnswer('correctString2', 2);
  }
  if (answerScore('q3') === 0) {
    document.getElementById('correctAnswer3').innerHTML = correctAnswer('correctString3', 3);
  }
  if (answerScore('q4') === 0) {
    document.getElementById('correctAnswer4').innerHTML = correctAnswer('correctString4', 4);
  }

  // calculate "possible score" integer
  let questionCountArray = document.getElementsByClassName('question');

  let questionCounter = 0;
  for (let i = 0, length = questionCountArray.length; i < length; i++) {
    questionCounter++;
  }

  // show score as "score/possible score"
  let showScore = "Результат: " + calcScore +"/" + questionCounter;
  // if 4/4, "perfect score!"
  if (calcScore === questionCounter) {
    showScore = showScore + "&nbsp; <strong>Отличный результат!</strong>"
  };
  document.getElementById('userScore').innerHTML = showScore;
}

$(document).ready(function() {
  document.getElementById('submitButton').click(function() {
    $(this).classList.add('hide');
  });
});