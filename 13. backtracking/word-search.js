var exist = function (board, word) {
   let hasWord = false;
   const visited = [];
   for (let i = 0; i < board.length; i++) {
      visited.push([]);
      for (let j = 0; j < board[i].length; j++) {
         visited[i].push(false);
      }
   }

   function backtrack(i, j, x) {
      if (x == word.length) {
         hasWord = true;
      }
      // right
      if (i + 1 < board.length && !visited[i + 1][j]) {
         if (board[i + 1][j] == word[x]) {
            visited[i + 1][j] = true;
            backtrack(i + 1, j, x + 1);
            visited[i + 1][j] = false;
         }
      }

      // left
      if (i - 1 >= 0 && !visited[i - 1][j]) {
         if (board[i - 1][j] == word[x]) {
            visited[i - 1][j] = true;

            backtrack(i - 1, j, x + 1);
            visited[i - 1][j] = false;
         }
      }

      // top
      if (j + 1 < board[i].length && !visited[i][j + 1]) {
         if (board[i][j + 1] == word[x]) {
            visited[i][j + 1] = true;
            backtrack(i, j + 1, x + 1);
            visited[i][j + 1] = false;
         }
      }

      // bottom
      if (j - 1 >= 0 && !visited[i][j - 1]) {
         if (board[i][j - 1] == word[x]) {
            visited[i][j - 1] = true;
            backtrack(i, j - 1, x + 1);
            visited[i][j - 1] = false;
         }
      }
   }
   for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[i].length; j++) {
         if (board[i][j] == word[0]) {
            visited[i][j] = true;
            backtrack(i, j, 1);
            visited[i][j] = false;
         }
      }
   }
   return hasWord;
};

var existV2 = function (board, word) {
   let hasWord = false;

   function backtrack(i, j, x) {
      if (x == word.length) {
         hasWord = true;
      }
      const value = board[i][j];
      board[i][j] = "#";
      // right
      if (i + 1 < board.length && board[i + 1][j] == word[x]) {
         backtrack(i + 1, j, x + 1);
      }

      // left
      if (i - 1 >= 0 && board[i - 1][j] == word[x]) {
         backtrack(i - 1, j, x + 1);
      }

      // top
      if (j + 1 < board[i].length && board[i][j + 1] == word[x]) {
         backtrack(i, j + 1, x + 1);
      }

      // bottom
      if (j - 1 >= 0 && board[i][j - 1] == word[x]) {
         backtrack(i, j - 1, x + 1);
      }

      board[i][j] = value;
   }

   for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[i].length; j++) {
         if (board[i][j] == word[0]) {
            backtrack(i, j, 1);
         }
      }
   }
   return hasWord;
};
