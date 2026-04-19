const combination = (n, k) => {
   const ans = [];
   const backtrack = (path, start) => {
      if (path.length == k) {
         ans.push([...path]);
         return;
      }
      for (let i = start; i <= n; i++) {
         path.push(i);
         backtrack(path, i + 1);
         path.pop();
      }
   };

   backtrack([], 1);
   return ans;
};

console.log(combination(4, 2));
