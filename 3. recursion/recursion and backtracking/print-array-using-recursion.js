const printArray = (arr, idx) => {
   if (idx >= arr.length) {
      return;
   }
   console.log(arr[idx]);
   printArray(arr, idx + 1);
};

printArray([1, 2, 3, 4], 0);
