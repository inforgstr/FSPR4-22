
// const data = [("Monday", 10), "Tuesday 8", "Wednesday 7", "Thursday 12", "Friday 10", "Saturday 7", "Sunday 10"];

// const sleepCounter = () => {
//     let day = prompt("Enter day: ");
// }

let sleepData = [
    ["Thursday", 5],
    ["Saturday", 5],
    ["Sunday", 8],
];

const sleepCounter = () => {
    let day = prompt("Day: ");
    let hours = parseInt(prompt("Sleepping hours: "));
    sleepData.push([day, hours]);
};

const avarageSleepHour = (sleepData) => {
    let sum = 0;
    for (const sleep of sleepData) {
        sum += sleep[1];
        console.log(sum);
    }

    return sum / sleepData.length;
};

alert(avarageSleepHour(sleepData));
