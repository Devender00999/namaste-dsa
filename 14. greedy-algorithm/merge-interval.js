var merge = function (arr) {
   // My Attempt
   // let ans = [];
   // let n = arr.length;
   // arr.sort((a,b) => a[0]-b[0])
   // for (let i = 0; i < n; i++) {
   //     let j = i + 1;
   //     while (j < n && arr[i][1] >= arr[j][0]) {
   //         arr[i][0] = Math.min(arr[i][0], arr[j][0])
   //         arr[i][1] = Math.max(arr[i][1], arr[j][1])
   //         j += 1;
   //     }
   //     ans.push(arr[i]);
   //     i = j - 1
   // }

   //  Akshay's solution
   arr.sort((a, b) => a[0] - b[0]);
   let ans = [arr[0]];

   for (let i = 1; i < arr.length; i++) {
      if (arr[i][0] <= ans[ans.length - 1][1]) {
         ans[ans.length - 1][1] = Math.max(arr[i][1], ans[ans.length - 1][1]);
      } else {
         ans.push(arr[i]);
      }
   }
   return ans;
};
