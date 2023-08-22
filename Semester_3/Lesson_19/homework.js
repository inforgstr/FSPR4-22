// Mumbling
/**
  * Returns accumulated string with '-' delimiter
  * @param {string} s
  * @return {string}
  */
const accum = s => {
  let data = new Array();
  // Iterate string (s) variable
  for (let count = 0; count < s.length; count++) {
    // Create new String object with default upper case letter
    let c = new String(s[count].toUpperCase());
    if (count >= 1) {
      // Repeating letter by position number
      c += s[count].toLowerCase().repeat(count);
    };
    // add to array
    data.push(c);
  }
  // join array elements with '-' delimiter
  return data.join("-");
}

// console.log(accum("ZpglnRxqenU"));

// Concatenated Sum
/**
  * Returns accumulated string with '-' delimiter
  * @param {number} result
  * @param {number} n
  * @return {boolean}
  */
const checkConcatenatedSum = (result, n) => {
  // Convert result {number} into {string}
  let string = String(result);
  // create instance answer with minimum value
  let ans = 0;

  // check if string starts with '-'
  if (string.startsWith("-")) {
    // Ignoring first string element
    // iterate string by minusing string[i]
    for (let i = 1; i < string.length; i++) {
      ans -= Number(string[i].repeat(n));
    }
  } else {
    // iterate string by plusing string[i]
    for (let i = 0; i < string.length; i++) {
      ans += Number(string[i].repeat(n))
    }
  };
  // check if answer is equal to expected result
  return ans === result;
}

// console.log(checkConcatenatedSum(-7863, 8));

// Playing with Sets:Intersection
/**
  * Returns accumulated string with '-' delimiter
  * @param {set} s1
  * @param {set} s2
  * @return {set}
  */
function inter(s1, s2) {
  // create new instance Set object
  let newSet = new Set();
  // iterate Set with element
  s1.forEach(element => {
    // check two Set objects to intersection
    if (s2.has(element)) {
      // add element to new Set object
      newSet.add(element);
    }
  });
  // return result
  return newSet;
}

// console.log(inter(new Set([2, 3]), new Set([2, 3,])));
