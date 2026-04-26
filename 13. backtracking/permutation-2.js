// permua
var permuteUnique = function (nums) {
   let ans = [];
   const backtrack = (path, choices) => {
      if (path.length == nums.length) {
         ans.push([...path]);
         return;
      }

      for (let i = 0; i < choices.length; i++) {
         if (i > 0 && choices[i] == choices[i - 1]) continue;
         path.push(choices[i]);
         backtrack(path, [...choices.slice(0, i), ...choices.slice(i + 1)]);
         path.pop();
      }
   };
   nums = nums.sort();
   backtrack([], nums);
   return ans;
};
