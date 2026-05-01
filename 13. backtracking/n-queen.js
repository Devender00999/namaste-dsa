var solveNQueens = function (n) {
   const ans = [];
   const matrix = [];
   for (let i = 0; i < n; i++) {
      const arr = [];
      for (let j = 0; j < n; j++) {
         arr.push(".");
      }
      matrix.push(arr);
   }

   const backtrack = (matrix, row, columnSet, diagSet, antiDiagSet) => {
      if (row == n) {
         ans.push(matrix.map((i) => i.join("")));
      }
      for (let j = 0; j < n; j++) {
         if (
            row >= n ||
            columnSet.has(j) ||
            diagSet.has(row + j) ||
            antiDiagSet.has(j - row)
         )
            continue;
         matrix[row][j] = "Q";
         columnSet.add(j);
         diagSet.add(row + j);
         antiDiagSet.add(j - row);
         backtrack(matrix, row + 1, columnSet, diagSet, antiDiagSet);
         matrix[row][j] = ".";
         columnSet.delete(j);
         diagSet.delete(row + j);
         antiDiagSet.delete(j - row);
      }
   };
   backtrack(matrix, 0, new Set(), new Set(), new Set());
   return ans;
};
