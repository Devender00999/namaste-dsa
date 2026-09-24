var climbStairs = function (n) {
   let dp = [0, 1, 2];
   for (let i = 3; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
   }
   return dp[n];
};

let dp = {};
var climbingStairs = function (n) {
   if (n <= 2) return n;
   if (!dp[n]) {
      dp[n] = climbingStairs(n - 1) + climbingStairs(n - 2);
   }

   return dp[n];
};

// console.log(climbStairs(13));

var climbStairs = function (n) {
   const dp = {};
   function climb(i) {
      if (i == n) return 1;
      if (i > n) return 0;
      if (!dp[i]) {
         dp[i] = climb(i + 1) + climb(i + 2);
      }
      return dp[i];
   }
   return climb(0);
};

console.log(climbingStairs(200));
console.log(climbStairs(200));
