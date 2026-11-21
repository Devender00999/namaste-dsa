let arr = [
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
];
arr[4];
function knightsTour(arr, i, j, move) {
   if (i < 0 || j < 0 || i >= arr.length || j >= arr.length || arr[i][j] != 0) {
      return;
   } else if (move == arr.length * arr.length) {
      arr[i][j] = move;
      printChessboard(arr);
      arr[i][j] = 0;
      return;
   }
   arr[i][j] = move;
   knightsTour(arr, i - 2, j + 1, move + 1);
   knightsTour(arr, i - 1, j + 2, move + 1);
   knightsTour(arr, i + 1, j + 2, move + 1);
   knightsTour(arr, i + 2, j + 1, move + 1);
   knightsTour(arr, i + 2, j - 1, move + 1);
   knightsTour(arr, i + 1, j - 2, move + 1);
   knightsTour(arr, i - 1, j - 2, move + 1);
   knightsTour(arr, i - 2, j - 1, move + 1);
   arr[i][j] = 0;
}

function printChessboard(arr) {
   for (let i = 0; i < arr.length; i++) {
      let str = "";
      for (let j = 0; j < arr.length; j++) {
         const charLength = arr[i][j].toString().length;
         str += arr[i][j] + "".padEnd(4 - charLength, " ");
      }
      console.log(str + "\n");
   }
   console.log("");
}
knightsTour(arr, 2, 3, 1);
