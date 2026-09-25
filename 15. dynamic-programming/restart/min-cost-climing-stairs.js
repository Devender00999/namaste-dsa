var minCostClimbingStairs = function (cost) {
   const dp = {};
   function climb(i) {
      if (i == 0 || i == 1) return 0;
      if (dp[i] == undefined) {
         dp[i] = Math.min(
            climb(i - 1) + cost[i - 1],
            climb(i - 2) + cost[i - 2],
         );
      }
      return dp[i];
   }
   return climb(cost.length);
};

function minClimbStairs() {
   const dp = [0, 0];
   for (let i = 2; i < cost.length; i++) {
      dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
   }
   return dp[i];
}
