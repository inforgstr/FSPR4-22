// Counting Array Elements (retired)
function count(array) {
  let ans = {};
  for (let element of array) {
    if (Object.keys(ans).includes(element)) {
      ans[element] += 1;
    } else {
      ans[element] = 1;
    };
  }
  return ans;
}


// Who is the killer?
function killer(suspectInfo, dead) {
  let objKeys = Object.keys(suspectInfo);
  for (let key of objKeys) {
    let isKiller = suspectInfo[key].filter(name => dead.includes(name));
    if (isKiller.length === dead.length) {
      return key;
    }
  }
  return false;
}

// Find the odd int
function findOdd(A) {
  let res = {};
  for (let value of A) {
    if (Object.keys(res).includes(String(value))) {
      res[value] += 1;
    } else {
      res[value] = 1;
    };
  }
  for (let key in res) {
    if (res[key] % 2) {
      return Number(key);
    }
  }
}

// N-th Fibonacci
function nthFibo(n) {
  if (n == 1) {
    return 0
  } else if (n < 2) {
    return 1
  }
  return nthFibo(n - 1) + nthFibo(n - 2);
  /*
  Another way:
  let fib1 = 0;
  let fib2 = 1;
  for (let i = 0; i < n; i++) {
    c = fib1 + fib2;
    fib1 = fib2;
    fib2 = c;
  }
  return fib1;
  */
}

// Доп задание
var Router = function () {
  return {
    urls: {},
    bind(endpoint, method, func) {
      this.urls[`${endpoint} ${method}`] = [method, func];
    },
    runRequest(endpoint, method) {
      if (Object.keys(this.urls).includes(`${endpoint} ${method}`)) {
        return this.urls[`${endpoint} ${method}`][1]();
      } else {
        return "Error 404: Not Found";
      }
    }
  }
}

var router = new Router();

// router.bind('/hello', 'GET', function () { return 'hello world'; });
// router.bind('/login', 'GET', function () { return 'Please log-in.'; });
// console.log(router);
// console.log(router.runRequest('/hello', 'GET'));
// console.log(router.runRequest("/login", "GET"));
