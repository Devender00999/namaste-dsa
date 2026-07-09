// bottom up approach
var minCostClimbingStairs = function (cost) {
   let dp = {};
   var climbStairs = function (n) {
      let dp = [0, 0];
      for (let i = 2; i <= n; i++) {
         dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
      }
      return dp[n];
   };

   return climbStairs(cost.length);
};

// top down approach
var minCostClimbingStairs = function (cost) {
   let dp = {};
   function climbStairs(i) {
      if (i == 1 || i == 0) return 0;
      if (dp[i] === undefined) {
         let left = climbStairs(i - 1) + cost[i - 1];
         let right = climbStairs(i - 2) + cost[i - 2];
         dp[i] = Math.min(left, right);
      }
      return dp[i];
   }

   return climbStairs(cost.length);
};
