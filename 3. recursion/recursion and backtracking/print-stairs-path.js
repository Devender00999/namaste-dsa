function printStairsPath(n, ans) {
   if (n < 0) return;
   if (n == 0) {
      console.log(ans);
      return;
   }
   printStairsPath(n - 1, ans + "1");
   printStairsPath(n - 2, ans + "2");
   printStairsPath(n - 3, ans + "3");
}

printStairsPath(5, "");
