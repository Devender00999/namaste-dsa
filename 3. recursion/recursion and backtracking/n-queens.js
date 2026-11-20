let arr = [
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
];
// let arr = [
//    [0, 0],
//    [0, 0],
// ];
function nQueens(arr, asf, row) {
   if (row == arr.length) {
      console.log(asf);
      return;
   }

   for (let col = 0; col < arr.length; col++) {
      if (checkValidMove(arr, row, col, asf) == true) {
         arr[row][col] = 1;
         nQueens(arr, asf + row + "-" + col + ",", row + 1);
         arr[row][col] = 0;
      }
   }
}

function checkValidMove(arr, row, col) {
   for (let i = row - 1, j = col; i >= 0; i--) {
      if (arr[i][j] == 1) {
         return false;
      }
   }
   for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (arr[i][j] == 1) {
         return false;
      }
   }
   for (let i = row - 1, j = col + 1; i >= 0 && j < arr.length; i--, j++) {
      if (arr[i][j] == 1) {
         return false;
      }
   }

   return true;
}

nQueens(arr, "", 0);
