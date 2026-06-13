var insert = function (intervals, newInterval) {
   let n = intervals.length;
   let ans = [];

   // pushing smaller intervals on left
   let i = 0;
   while (i < n && intervals[i][1] < newInterval[0]) {
      ans.push(intervals[i]);
      i++;
   }

   // pushing overlaping intervals
   while (i < n && intervals[i][0] <= newInterval[1]) {
      newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
      newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
      i++;
   }
   ans.push(newInterval);

   // Pushing greater intervals on right
   while (i < n) {
      ans.push(intervals[i]);
      i++;
   }

   return ans;
};
