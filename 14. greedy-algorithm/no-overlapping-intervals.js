var eraseOverlapIntervals = function (intervals) {
   intervals.sort((a, b) => a[1] - b[1]);
   let start = intervals[0][0],
      end = intervals[0][1];
   let ans = 0;
   for (let i = 1; i < intervals.length; i++) {
      curr = intervals[i];
      if (curr[0] < end) {
         ans += 1;
      } else {
         end = Math.max(end, curr[1]);
      }
   }
   return ans;
};
