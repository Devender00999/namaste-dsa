const printArray = (arr, idx) => {
   if (idx >= arr.length) {
      return;
   }
   printArray(arr, idx + 1);
   console.log(arr[idx]);
};

printArray([1, 2, 3, 4], 0);
