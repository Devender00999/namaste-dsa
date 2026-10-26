function printMazePath(sc, sr, dc, dr, ans) {
   if (sc == dc && sr == dr) {
      console.log(ans);
      return;
   }
   if (sc > dc || sr > dr) {
      console.log(ans);
      return;
   }
   // horizontal
   for (let i = 1; i <= dr - sr; i++) {
      printMazePath(sc, sr + i, dc, dr, ans + "h" + i);
   }

   // vertical
   for (let i = 1; i <= dc - sc; i++) {
      printMazePath(sc + i, sr, dc, dr, ans + "v" + i);
   }

   // diagonal
   for (let i = 1; i <= dc - sc && i <= dr - sr; i++) {
      printMazePath(sc + i, sr + i, dc, dr, ans + "d" + i);
   }
}
printMazePath(1, 1, 3, 3, "");
