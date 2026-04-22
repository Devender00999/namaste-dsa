var combinationSum = function (nums, target) {
   const res = [];
   function backtrack(path, start) {
      const sum = [...path].reduce((acc, curr) => acc + curr, 0);
      if (sum == target) {
         res.push([...path]);
      }
      if (sum > target) {
         start + 1;
         return;
      }
      for (let i = start; i < nums.length; i++) {
         path.push(nums[i]);
         backtrack(path, i);
         path.pop();
      }
   }
   backtrack([], 0);
   return res;
};

var combinationSum = function (nums, target) {
   const res = [];
   function backtrack(path, start, currTarget) {
      if (currTarget == 0) {
         res.push([...path]);
      }

      if (currTarget < 0) {
         return;
      }
      for (let i = start; i < nums.length; i++) {
         path.push(nums[i]);
         backtrack(path, i, currTarget - nums[i]);
         path.pop();
      }
   }
   backtrack([], 0, target);
   return res;
};
