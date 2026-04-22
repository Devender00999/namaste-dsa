var combinationSum2 = function (nums, target) {
   const res = [];
   nums.sort();
   function backtrack(path, start) {
      const sum = [...path].reduce((acc, curr) => acc + curr, 0);
      if (sum == target) {
         res.push([...path]);
      }
      if (sum > target) return;
      for (let i = start; i < nums.length; i++) {
         if (i > start && nums[i] == nums[i - 1]) continue;
         path.push(nums[i]);
         backtrack(path, i + 1);
         path.pop();
      }
   }
   backtrack([], 0);
   return res;
};
