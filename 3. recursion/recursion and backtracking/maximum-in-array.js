// arr = [1,2,4,2, 1]
// expectation max(arr, 0) => max element
// faith max(arr, 1) => maximum element from 1 to n
// Faith & expectation => Math.max(arr[0], max(arr, 1))

function maximum(arr, idx) {
   if (idx == arr.length - 1) return arr[idx];
   let maxtnm1 = maximum(arr, idx + 1);
   return Math.max(maxtnm1, arr[idx]);
}

console.log(maximum([1, 2, 4, 2, 11], 0));
