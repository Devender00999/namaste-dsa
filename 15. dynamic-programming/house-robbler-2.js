var rob = function (nums) {
   if (nums.length == 1) return nums[0];
   let n = nums.length;
   var robHelp = function (start, end) {
      if (nums.length == 1) return nums[0];
      let p1 = (p2 = 0);
      for (let i = start; i <= end; i++) {
         let curr = Math.max(p1 + nums[i], p2);
         p1 = p2;
         p2 = curr;
      }
      return p2;
   };

   return Math.max(robHelp(0, n - 2), robHelp(1, n - 1));
};
