// let name = "behruz";
// this.a = 12;

// // console.log(this);


// const goat = {
//   dietType: "herbivore",
//   makeSound() {
//     console.log(this.dietType);
//   },
//   // Arrow functions are non-sensetive.
//   // Arrow functions scope always on global level.
//   diet: () => {
//     // console.log(this.dietType); undefined
//     console.log(this.a);
//   },
// };

// goat.diet();
// goat.makeSound();

// const bankAccount = {
//   _amount: 100,
// };

// bankAccount._amount = 1000000;
// console.log(bankAccount);

// const robot = {
//   _energyLevel: 100,
//   rechange() {
//     this._energyLevel += 30;
//     console.log(`Recharched! Energy is currently at ${this._energyLevel}%.`);
//   },
// }

// robot._energyLevel = "high";
// robot.rechange();
// console.log(robot._energyLevel);

// const person = {
//   _firstName: "John",
//   _lastName: "Doe",
//   _age: 37,
//   // fullName: "Fracisco Buele" // не делать
//   get fullName() {
//     if (this._firstName && this._lastName) {
//       return `${this._firstName} ${this._lastName}`;
//     } else {
//       return "Missing a first name or a last name.";
//     };
//   },
//   set age(newAge) {
//     if (typeof newAge === "number") {
//       this._age = newAge;
//     } else {
//       console.log("You must assign a number to age.");
//     };
//   },
//   get age() {
//     if (this._age) {
//       return this._age;
//     } else {
//       return "Age is empty or is 0.";
//     }
//   },
// }

// person.age = "40";
// console.log(person.fullName);
// console.log(person.age);


// var Router = function () {
//   return {
//     urls: {},
//     bind(endpoint, method, func) {
//       this.urls[`${endpoint} ${method}`] = [method, func];
//     },
//     runRequest(endpoint, method) {
//       if (Object.keys(this.urls).includes(`${endpoint} ${method}`)) {
//         return this.urls[`${endpoint} ${method}`][1]();
//       } else {
//         return "Error 404: Not Found";
//       }
//     }
//   }
// }

// var router = new Router();

// router.bind('/hello', 'GET', function () { return 'hello world'; });
// router.bind('/login', 'GET', function () { return 'Please log-in.'; });
// console.log(router);
// console.log(router.runRequest('/hello', 'GET'));
// console.log(router.runRequest("/login", "GET"));


let menu = {
  _meal: "Meal",
  _price: 10,
  get meal() {
    if (this._meal && typeof this._meal === "string") {
      return this._meal;
    } else {
      return "Value of meal is not valid."
    }
  },
  set meal(newValue) {
    if (typeof newValue === "string" && newValue) {
      this._meal = newValue;
    } else {
      console.log("Please, set valid value of meal.");
    }
  },
  get price() {
    if (typeof this._price === "number" && this._price) {
      return this._price;
    } else {
      return "Value of price is not valid."
    }
  },
  set price(newPrice) {
    if (typeof this._price === "number" && newPrice) {
      this._price = newPrice;
    } else {
      console.log("Please, set valid value of price.");
    }
  }
};

console.log(menu.meal);
menu.meal = "Another meal";
menu.price = 30.2;
console.log(menu.meal);

const count = (array) => {
  newObj = {};
  for (let i = 0; i < array.length; i++) {
    if (Object.keys(newObj).includes(array[i])) {
      newObj[array[i]] += 1;
    } else {
      newObj[array[i]] = 1;
    }
  }
  return newObj;
};

console.log(count(["james", "james", "john"]));
