function getStairsPath(n) {
   if (n == 0) return [""];
   if (n < 0) return [];
   const path1 = getStairsPath(n - 1);
   const path2 = getStairsPath(n - 2);
   const path3 = getStairsPath(n - 3);
   const res = [];
   for (let path of path1) {
      res.push("1" + path);
   }

   for (let path of path2) {
      res.push("2" + path);
   }

   for (let path of path3) {
      res.push("3" + path);
   }

   return res;
}

console.log(getStairsPath(3));
