// function userInfo(name, psw = "secret") {
//   let stars = "*".repeat(psw.length);
//   return `Your name is ${name} with password: ${stars}`;
// }

// console.log(userInfo());

// // Functions expressions
// (function (day) {
//   return day === "Wednesday";
// });

// const isWednesday = function (day) {
//   return day === "Wednesday";
// };

// console.log(isWednesday("Wednesday"));

// // Arrow Functions 
// const rectangleArea = (width, height) => {
//   let area = width * height;
//   return area;
// };

// // const dummy = (singleParam) => singleParam + 2;
// const dummy = (signleParam) => {
//   if (signleParam) {
//     return true;
//   };
// };

// console.log(dummy(12));

let first = "paper";
let second = "scissors";

function rpsGame(first, second) {
  let sP = ["scissors", "paper"];
  let rS = ["rock", "scissors"];
  let pR = ["rock", "paper"];
  let draw = first === second;
  if (sP.includes(first) && sP.includes(second) && !draw) {
    if (first === "scissors") {
      winner = "First player won!";
    } else if (second === "scissors") {
      winner = "Second player won!";
    };

    ans = `Scissors cut paper. ${winner}`;
  } else if (rS.includes(first) && rS.includes(second) && !draw) {
    if (first === "scissors") {
      winner = "First player won!";
    } else if (second === "scissors") {
      winner = "Second player won!";
    };

    ans = `Rock destroys scissors.${winner}`;
  } else if (pR.includes(first) && pR.includes(second) && !draw) {
    if (first === "scissors") {
      winner = "First player won!";
    } else if (second === "scissors") {
      winner = "Second player won!";
    };

    ans = `Paper covers rock.${winner}`;
  } else {
    ans = "If there's a tie, then the game ends in a draw."
  };
  return ans;
}

console.log(rpsGame(first, second));

var name = "Behruz";
let last_name = "Something";
const age = 12;

if (true) {
  let last_name = "test_2"
  const age = 32;
  console.log(last_name, age);
};

console.log(last_name, age);


