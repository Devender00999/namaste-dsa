function getMazePath(sr, sc, dr, dc) {
   if (sr == dr && sc == dc) {
      return [""];
   }

   if (sr > dr || sc > dc) {
      return [];
   }
   let hPaths = getMazePath(sr, sc + 1, dr, dc);
   let vPaths = getMazePath(sr + 1, sc, dr, dc);
   let ans = [];
   for (let i = 0; i < hPaths.length; i++) {
      ans.push("h" + hPaths[i]);
   }

   for (let i = 0; i < vPaths.length; i++) {
      ans.push("v" + vPaths[i]);
   }
   return ans;
}

console.log(getMazePath(1, 1, 3, 3));
