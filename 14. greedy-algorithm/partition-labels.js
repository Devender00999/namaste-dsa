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
         merged[merged.length - 1][1] = Math.max(
            merged[merged.length - 1][1],
            indexes[i][1],
         );
      } else {
         merged.push(indexes[i]);
      }
   }
   return merged.map((item) => item[1] - item[0] + 1);
};

function partitionLabels(s) {
   let first = Array(26).fill(-1);
   let last = Array(26).fill(-1);
   for (let i = 0; i < s.length; i++) {
      let curr = s.charCodeAt(i) - 97;
      if (first[curr] == -1) {
         first[curr] = i;
      }
      last[curr] = i;
   }

   let parStart = (parEnd = 0);
   let ans = [];

   for (let i = 0; i < s.length; i++) {
      let curr = s.charCodeAt(i) - 97;
      if (parEnd < first[curr]) {
         ans.push(parEnd - parStart + 1);
         parStart = first[curr];
      }
      parEnd = Math.max(last[curr], parEnd);
   }

   if (parEnd - parStart + 1 > 0) {
      ans.push(parEnd - parStart + 1);
   }
   return ans;
}
