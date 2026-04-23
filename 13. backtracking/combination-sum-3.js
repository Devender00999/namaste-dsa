var combinationSum3 = function (k, n) {
   const res = [];
   const backtrack = (path, start, target, level) => {
      if (level == 0 && target == 0) {
         res.push([...path]);
      }
      for (let i = start; i <= 9; i++) {
         path.push(i);
         backtrack(path, i + 1, target - i, level - 1);
         path.pop();
      }
   };
   backtrack([], 1, n, k);
   return res;
};
