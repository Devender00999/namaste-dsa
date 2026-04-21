var subsetsWithDup = function (nums) {
   const ans = [];
   const unique = {};
   nums.sort((a, b) => a - b);
   const backtrack = (path, start) => {
      ans.push([...path]);

      for (let i = start; i < nums.length; i++) {
         if (i > start && nums[i] === nums[i - 1]) continue;
         path.push(nums[i]);
         backtrack(path, i + 1);
         path.pop(nums[i]);
      }
   };
   backtrack([], 0);
   return ans;
};
