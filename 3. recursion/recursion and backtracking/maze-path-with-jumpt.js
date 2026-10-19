function getMazePath(sr, sc, dr, dc) {
   if (sr == dr && sc == dc) {
      return [""];
   }
   let ans = [];

   // horizontal
   for (let i = 1; i <= dc - sc; i++) {
      let hPaths = getMazePath(sr, sc + i, dr, dc);
      hPaths.forEach((path) => {
         ans.push("h" + i + "" + path);
      });
   }

   // vertical
   for (let i = 1; i <= dr - sr; i++) {
      let vPaths = getMazePath(sr + i, sc, dr, dc);
      vPaths.forEach((path) => {
         ans.push("v" + i + "" + path);
      });
   }

   // diagonal
   for (let i = 1; i <= dr - sr && i <= dc - sc; i++) {
      let vPaths = getMazePath(sr + i, sc + 1, dr, dc);
      vPaths.forEach((path) => {
         ans.push("d" + i + "" + path);
      });
   }

   return ans;
}

console.log(getMazePath(1, 1, 2, 2));
