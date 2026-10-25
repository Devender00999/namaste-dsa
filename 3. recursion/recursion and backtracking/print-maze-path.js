function printMazePath(sr, sc, dr, dc, ans) {
   if (sr == dr && sc == dc) {
      console.log(ans);
      return;
   }

   if (sr > dr || sc > dc) {
      return;
   }

   printMazePath(sr, sc + 1, dr, dc, ans + "h");
   printMazePath(sr + 1, sc, dr, dc, ans + "v");
}

printMazePath(1, 1, 3, 3, "");
