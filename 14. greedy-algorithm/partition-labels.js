var partitionLabels = function (s) {
   let visited = {};
   const indexes = [];
   for (let i = 0; i < s.length; i++) {
      const ch = s[i];
      if (visited[ch]) continue;
      visited[ch] = true;
      indexes.push([s.indexOf(ch), s.lastIndexOf(ch)]);
   }
   indexes.sort((a, b) => a[0] - b[0]);

   const merged = [indexes[0]];
   for (let i = 1; i < indexes.length; i++) {
      if (merged[merged.length - 1][1] >= indexes[i][0]) {
         merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], indexes[i][1]);
      } else {
         merged.push(indexes[i]);
      }
   }
   return merged.map((item) => item[1] - item[0] + 1);
};
