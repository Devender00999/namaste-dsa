function targetSum(arr, sum, asf, totalSum) {
   if (arr.length == 0) {
      if (sum == totalSum) {
         console.log(asf);
      }
      return;
   }

   const curr = arr[0];
   targetSum(arr.slice(1, arr.length), sum, asf, totalSum);
   targetSum(arr.slice(1, arr.length), sum, [...asf, curr], totalSum + curr);
   return;
}

targetSum([10, 20, 30, 40, 50], 60, [], 0);
