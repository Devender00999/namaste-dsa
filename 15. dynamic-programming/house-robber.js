var rob = function (nums) {
   let n = nums.length;
   let dp = [nums[0], Math.max(nums[0], nums[1])];
   for (let i = 2; i < n; i++) {
      dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
   }
   return dp[n - 1];
};

var rob = function (nums) {
   let n = nums.length;
   let dp = {};
   function robbing(n) {
      if (n == 0) return nums[0];
      if (n == 1) return Math.max(nums[0], nums[1]);

      if (dp[n] == undefined) {
         dp[n] = Math.max(robbing(n - 2) + nums[n], robbing(n - 1));
      }
      return dp[n];
   }
   return robbing(n - 1);
};

var rob = function (nums) {
   if (nums.length == 1) return nums[0];
   let n = nums.length;
   let dp = [nums[0], Math.max(nums[0], nums[1])];
   for (let i = 2; i < n; i++) {
      let temp = dp[1];
      dp[1] = Math.max(dp[0] + nums[i], dp[1]);
      dp[0] = temp;
   }
   return dp[1];
};
