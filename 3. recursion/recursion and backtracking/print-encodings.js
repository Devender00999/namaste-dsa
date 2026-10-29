const encodings = [
   "",
   "a",
   "b",
   "c",
   "d",
   "e",
   "f",
   "g",
   "h",
   "i",
   "j",
   "k",
   "l",
   "m",
   "n",
   "o",
   "p",
   "q",
   "r",
   "s",
   "t",
   "u",
   "v",
   "w",
   "x",
   "y",
   "z",
];

function printEncodings(ques, ans) {
   if (ques.length == 0) {
      console.log(ans);
      return;
   } else if (ques.length == 1) {
      if (ques == "0") return;
      else {
         ans += encodings[parseInt(ques)];
         console.log(ans);
      }
   } else {
      const curr = parseInt(ques.slice(0, 1));
      if (curr == 0) {
         return;
      } else {
         printEncodings(ques.slice(1), ans + encodings[curr]);
      }
      const curr2 = parseInt(ques.slice(0, 2));
      if (curr2 <= 26) {
         ans += encodings[curr2];
         printEncodings(ques.slice(2), ans);
      }
   }
}

printEncodings("123", "");
