var coinChange = function (coins, amount) {
   let dp = {};
   const solution = (x) => {
      if (x == 0) return 0;
      if (x < 0) return Infinity;
      let min = Infinity;
      if (dp[x] == undefined) {
         for (let i = 0; i < coins.length; i++) {
            let diff = x - coins[i];
            let sol = solution(diff);
            min = Math.min(sol, min);
         }
         dp[x] = min + 1;
      }
      return dp[x];
   };
   const ans = solution(amount);
   return ans == Infinity ? -1 : ans;
};
