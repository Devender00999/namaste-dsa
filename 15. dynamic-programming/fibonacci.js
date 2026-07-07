let result = {};
function fibonacciNumberDP(n) {
   if (n <= 1) return n;
   let res1, res2;
   if (result[n - 1]) {
      res1 = result[n - 1];
   } else {
      res1 = fibonacciNumberDP(n - 1);
      result[n - 1] = res1;
   }
   if (result[n - 2]) {
      res2 = result[n - 2];
   } else {
      res2 = fibonacciNumberDP(n - 2);
      result[n - 2] = res2;
   }
   return res1 + res2;
}

function fibonacciNumber(n) {
   if (n <= 1) return n;
   return fibonacciNumber(n - 1) + fibonacciNumber(n - 2);
}

function fib(n) {
   if (n <= 1) return n;

   if (!result[n]) {
      result[n] = fib(n - 1) + fib(n - 2);
   }

   return result[n];
}

function fib(n) {
   let a = 0,
      b = 1;
   if (n <= 1) return n;
   let result = 0;

   for (let i = 1; i < n; i++) {
      result = a + b;
      a = b;
      b = result;
   }

   return result;
}

function fib(n) {
   let a = 0,
      b = 1;
   let dp = [0, 1];
   let result = 0;

   for (let i = 2; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
   }

   return dp[n];
}

console.log(fibonacciNumberDP(1000));
console.log(fibonacciNumber(1000));
