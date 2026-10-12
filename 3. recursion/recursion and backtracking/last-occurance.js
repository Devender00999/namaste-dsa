// 2, 3, 6, 7

function lastIndex(arr, idx, n) {
   if (idx == arr.length) {
      return -1;
   }
   let lit1 = lastIndex(arr, idx + 1, n);
   if (lit1 == -1) {
      if (arr[idx] == n) return idx;
      else {
         return -1;
      }
   } else {
      return lit1;
   }
}

console.log(lastIndex([3, 2, 3, 4, 2, 3, 1], 0, 2));
