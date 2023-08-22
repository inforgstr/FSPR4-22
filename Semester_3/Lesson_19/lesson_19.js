// let number = [];

// for (let counter = 0; counter < 10; counter++) {
//     number.push(counter);
// };

// // console.log(numbers);

// // let counterTwo = 4;

// // while (counterTwo < 4) {
// //     console.log(counterTwo);
// //     counterTwo++;
// // }

// // let counterString = "";
// // let i = 0;
// // do {
// //     i++;
// //     counterString = counterString + i;
// // } while (i < 5);

// // console.log(counterString); // 12345
// for (const num of "Dsdlfjklsdf") {
//     console.log(num);
// };

// let dict = {
//     // dictionary in javascript (nearly JAVASCRIPT OBJECT)
// }

const spaceship = {
  telescope: {
    yearBuilt: 2018,
    model: "91031-XLT",
    focalLength: 2032,
  },
  crew: {
    captain: {
      name: "Sandra",
      degree: "Computer Engineering",
      encourageTeam() {
        console.log("We got this!");
      },
      someFunction() {
        console.log("Some function logged into console!");
      },
    },
  },
  engine: {
    model: "Nimbus2000",
  },
  nanoelectronics: {
    computer: {
      terabytes: 100,
      monitors: "HD",
    },
    "back-up": {
      battery: "Lithium",
      terabytes: 50,
    },
  },
};

console.log(spaceship.crew.captain.encourageTeam());


