// reverse string
function reverseStr(string) {
    let newStr = "";
    for (let i = string.length - 1; i >= 0; i--) {
        newStr += string[i];
    };
    return newStr;
};

// disemvowel trolls
function disemvowel(str) {
    let newString = "";
    let vowels = "AEIOUaeiou";
    for (let char of str) {
        if (!vowels.includes(char)) {
            newString += char;
        };
    };
    return newString;
};

// square sequence 
function squares(x, n) {
    let array = [];
    for (let i=1; i <= n; i++) {
        array.push(x);
        x **= 2;
    };
    return array;
};
console.log(squares(2, 5));
