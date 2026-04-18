// T(n): O(n * 2 ^ n)
// S(n): O(n * 2 ^ n)
var subsets = function (nums) {
   const res = [];
   function backtrack(path, start) {
      res.push([...path]);
      for (let i = start; i < nums.length; i++) {
         path.push(nums[i]);
         backtrack(path, i + 1);
         path.pop();
      }
   }
   backtrack([], 0);
   return res;
};
