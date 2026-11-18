// const grid = [
//    [0, 0, 0, 0, 0, 0, 0],
//    [0, 1, 1, 0, 1, 1, 0],
//    [0, 1, 1, 1, 1, 0, 0],
//    [0, 0, 1, 0, 1, 1, 0],
//    [0, 1, 1, 0, 0, 1, 0],
//    [0, 0, 0, 0, 0, 0, 0],
// ];

const grid = [
   [0, 0, 1, 0],
   [0, 0, 0, 0],
   [1, 0, 1, 0],
   [0, 0, 0, 0],
];
const visited = [];
for (let i = 0; i < grid.length; i++) {
   let cv = [];
   for (let j = 0; j < grid[0].length; j++) {
      cv.push(false);
   }
   visited.push(cv);
}

function floodfill(arr, row, col, asf, visited) {
   if (
      row < 0 ||
      col < 0 ||
      row == arr.length ||
      col == arr[0].length ||
      arr[row][col] == 1 ||
      visited[row][col] == true
   ) {
      return;
   }

   if (row == arr.length - 1 && col == arr[0].length - 1) {
      console.log(asf);
      return;
   }
   visited[row][col] = true;
   floodfill(arr, row - 1, col, asf + "t", visited);
   floodfill(arr, row, col - 1, asf + "l", visited);
   floodfill(arr, row + 1, col, asf + "d", visited);
   floodfill(arr, row, col + 1, asf + "r", visited);
   visited[row][col] = false;
}

floodfill(grid, 0, 0, "", visited);
