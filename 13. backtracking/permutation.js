var permute = function (nums) {
   const ans = [];
   const backtrack = (path) => {
      if (path.length == nums.length) {
         ans.push([...path]);
      }
      for (let i = 0; i < nums.length; i++) {
         if (!path.includes(nums[i])) {
            path.push(nums[i]);
            backtrack(path);
            path.pop();
         }
      }
   };
   backtrack([]);
   return ans;
};
