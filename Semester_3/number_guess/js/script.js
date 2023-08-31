let userGuessed = document.getElementById("user-input");
let btnPlus = document.querySelector(".user-side .plus");
let btnMinus = document.querySelector(".user-side .minus");
let userScore = document.querySelector(".user-side .side-score span");
let computerScore = document.querySelector(".computer-side .side-score span");
let btnMakeSubmit = document.querySelector(".user-side button");
let TargetNum = document.querySelector(".main__head p span");
let NextRoundBtn = document.querySelector(".btn-next-round button");
let numRounds = 1;

let data = {};

btnPlus.addEventListener("click", () => {
  if (!userGuessed.value) {
    userGuessed.value = 0;
  } else {
    userGuessed.value < 10
      ? (userGuessed.value = parseInt(userGuessed.value) + 1)
      : false;
  }
});

btnMinus.addEventListener("click", () => {
  if (!userGuessed.value) {
    userGuessed.value = 0;
  } else {
    userGuessed.value > 0
      ? (userGuessed.value = parseInt(userGuessed.value) - 1)
      : false;
  }
});

userGuessed.addEventListener("input", function () {
  if (
    this.value < 0 ||
    this.value > 10 ||
    String(this.value).match(/[a-z,.\/\\<>?;':"\[\]{}!@#$%^&*()]+/gi) ||
    this.value.length > 2
  ) {
    this.value = 0;
  }
});

const numberGuess = (userNum, btnGuess) => {
  let userWinBlock = document.querySelector(".user-side");
  let computerWinBlock = document.querySelector(".computer-side");
  let userElementTag = document.createElement("div");
  let computerElementTag = document.createElement("div");
  userElementTag.className = "user-winner";
  computerElementTag.className = "computer-winner";
  btnGuess.className = "active";
  NextRoundBtn.className = "non-active";

  btnGuess.addEventListener("click", () => {
    if (btnGuess.className === "active") {
      let answer = Math.random() * 10;
      let computerNum = Math.ceil(Math.random() * 10);
      let userTarget =
        parseInt(userNum.value) - answer >= 0
          ? parseInt(userNum.value) - answer
          : answer - parseInt(userNum.value);
      let computerTarget =
        computerNum - answer >= 0 ? computerNum - answer : answer - computerNum;
      let userElement = document.querySelector(".user-winner");
      let computerElement = document.querySelector(".computer-winner");
      let computerImg = document.querySelector(".computer-side img");

      TargetNum.innerHTML = answer;
      computerImg.remove();
      let computerGuessElement = document.createElement("div");
      computerGuessElement.className =
        computerNum < 10 ? "computer-answer" : "computer-answer-large";
      computerGuessElement.innerHTML = computerNum;
      document.querySelector(".computer-side").append(computerGuessElement);
      if (userNum.value.match(/^\d{0,2}$/g) && 10 >= userNum.value >= 0) {
        if (
          userTarget <= computerTarget ||
          parseInt(userNum.value) === Math.ceil(answer)
        ) {
          if (computerElement) {
            computerElement.remove();
          }
          userScore.innerHTML = parseInt(userScore.innerHTML) + 1;
          btnGuess.innerHTML = "You Won!!!";
          data.winner = "User";
          data.gnumber = parseInt(userNum.value);
          data.tnumber = answer;
          data.ognumber = computerNum;
        } else {
          if (userElement) {
            userElement.remove();
          }
          computerScore.innerHTML = parseInt(computerScore.innerHTML) + 1;
          computerElementTag.textContent = "Computer Won!!!";
          computerWinBlock.append(computerElementTag);
          data.winner = "Computer";
          data.gnumber = computerNum;
          data.tnumber = answer;
          data.ognumber = parseInt(userNum.value);
        }
      } else {
        userElementTag.textContent =
          "Please, enter a valid number from 0 to 10!";
        userWinBlock.append(userElementTag);
      }
      historyAdd(numRounds, data);
      btnGuess.className = "non-active";
      NextRoundBtn.className = "active";
    }
  });
};

const nextRound = (userBtn, roundBtn) => {
  let roundNum = document.querySelector(".main__head h1 span");

  roundBtn.addEventListener("click", () => {
    document.querySelector("#user-input").value = 0;
    if (roundBtn.className === "active") {
      let userElement = document.querySelector(".user-winner");
      let computerElement = document.querySelector(".computer-winner");
      console.log(computerElement);
      let imgContent = "<img src='./img/question_mark.svg' width='200'>";
      let img = document.createElement("div");

      userBtn.innerHTML = "Make a Guess";
      let computerAnswer = document.querySelector(".computer-answer");
      computerAnswer
        ? computerAnswer.remove()
        : document.querySelector(".computer-answer-large").remove();
      img.innerHTML = imgContent;
      document.querySelector(".computer-side").append(img);
      TargetNum.innerHTML = "?";
      numRounds += 1;
      roundNum.innerHTML = parseInt(roundNum.innerHTML) + 1;
      roundBtn.className = "non-active";
      userBtn.className = "active";

      if (userElement) {
        userElement.remove();
      } else if (computerElement) {
        computerElement.remove();
      }
    }
  });
};

const historyAdd = (roundNum, data) => {
  let curDate = new Date();
  let element = document.createElement("tr");
  let content = `
    <th>${roundNum}</th>
    <th>${data.winner}</th>
    <th>${data.gnumber}</th>
    <th>${data.tnumber}</th>
    <th>${data.ognumber}</th>
    <th>${curDate.getFullYear()}: 
    ${curDate.toLocaleString("default", { weekday: "short" })}, 
    ${curDate.toLocaleString("default", { month: "short" })} 
    ${curDate.getDate()} ${curDate.getHours()}:${curDate.getMinutes()}</th>`;
  element.innerHTML = content;
  document.querySelector(".history table tbody").append(element);
};

nextRound(btnMakeSubmit, NextRoundBtn);
numberGuess(userGuessed, btnMakeSubmit);

let historyHeader = document.querySelector(".history header h1");
window.addEventListener("scroll", function () {
  if (window.scrollY >= 500) {
    historyHeader.style.animationName = "animateHeader";
  } else if (window.scrollY < 500) {
    historyHeader.style.animationName = "animateReverseHeader";
  }
});
