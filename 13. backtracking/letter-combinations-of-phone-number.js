var letterCombinations = function (digits) {
   const digitMapping = {
      2: "abc",
      3: "def",
      4: "ghi",
      5: "jkl",
      6: "mno",
      7: "pqrs",
      8: "tuv",
      9: "wxyz",
   };

   const ans = [];
   const backtrack = (path, start) => {
      if (path.length == digits.length) {
         ans.push([...path].join(""));
         return;
      }
      const choices = digitMapping[digits[start]];
      for (let i = 0; i < choices?.length; i++) {
         path.push(choices[i]);
         backtrack(path, start + 1);
         path.pop();
      }
   };

   backtrack([], 0);
   return ans;
};
