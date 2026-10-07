function firstOccurance(arr, idx, d) {
   if (idx == arr.length) return -1;
   let firstIndex = firstOccurance(arr, idx + 1, d);
   if (arr[idx] == d) return idx;
   else return firstIndex;
}

console.log(firstOccurance([2, 3, 6, 8, 9, 2, 6, 2, 4], 0, 4));
