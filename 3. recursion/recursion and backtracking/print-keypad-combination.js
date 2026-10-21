let arr = [".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"];
function printKeypadCombination(ques, ans) {
   if (ques.length == 0) {
      console.log(ans);
      return;
   }
   const ch = ques[0];
   const roq = ques.slice(1);
   const chIndex = parseInt(ch);
   for (let i = 0; i < arr[chIndex].length; i++) {
      printKeypadCombination(roq, ans + arr[chIndex][i]);
   }
}

printKeypadCombination("678", "");
