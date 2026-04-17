var kthSmallest = function (matrix, k) {
   // all the element in first column into the min pq
   let n = matrix[0].length;

   let heap = new MinPriorityQueue((x) => x.val);
   for (let i = 0; i < n; i++) {
      heap.push({ val: matrix[i][0], row: i, col: 0 });
   }

   while (k > 1) {
      const minValue = heap.pop();
      const { row, col } = minValue;
      if (col + 1 < n) {
         heap.push({ val: matrix[row][col + 1], row: row, col: col + 1 });
      }
      k -= 1;
   }
   return heap.front().val;
};
