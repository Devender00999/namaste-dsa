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

console.log(climbStairs(13));
console.log(climbingStairs(13));
