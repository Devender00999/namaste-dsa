function allIndices(arr, x, idx, ans) {
   if (arr.length == idx) return ans;

   if (arr[idx] == x) {
      ans.push(idx);
   }
   return allIndices(arr, x, idx + 1, ans);
}

console.log(allIndices([1, 2, 3, 1, 1], 1, 0, []));
