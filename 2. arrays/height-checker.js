var heightChecker = function (heights) {
   let sorted = [...heights];
   sorted.sort((a, b) => a - b);
   let ans = 0;
   for (let i = 0; i < heights.length; i++) {
      if (sorted[i] != heights[i]) {
         ans += 1;
      }
   }
   return ans;
};
