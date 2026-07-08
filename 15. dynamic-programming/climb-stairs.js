// Top down approach
let store = {};
var climbStairs = function (n) {
   if (n <= 2) return n;
   if (!store[n]) {
      store[n] = climbStairs(n - 1) + climbStairs(n - 2);
   }
   return store[n];
};

// bottom up approach
var climbStairs = function (n) {
   let dp = [0, 1, 2];
   for (let i = 3; i <= n; i++) {
      dp.push(dp[i - 1] + dp[i - 2]);
   }
   return dp[n];
};
