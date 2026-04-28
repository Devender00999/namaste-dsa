var partition = function (s) {
   const ans = [];
   const isPalindrome = (str) => {
      let i = 0;
      let j = str.length - 1;
      while (i < j) {
         if (str[i++] != str[j--]) {
            return false;
         }
      }
      return true;
   };
   const backtrack = (path, remaining) => {
      if (!remaining.length) {
         ans.push([...path]);
      }
      for (let i = 1; i <= remaining.length; i++) {
         const choice = remaining.substring(0, i);
         if (!isPalindrome(choice)) continue;
         path.push(choice);
         backtrack(path, remaining.substring(i));
         path.pop();
      }
   };
   backtrack([], s);
   return ans;
};
