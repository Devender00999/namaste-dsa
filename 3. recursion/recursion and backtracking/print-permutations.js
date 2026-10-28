function printPermutations(quest, ans) {
   if (quest.length == 0) {
      console.log(ans);
      return;
   }
   for (let i = 0; i < quest.length; i++) {
      printPermutations(quest.slice(0, i) + quest.slice(i + 1), ans + quest[i]);
   }
}

printPermutations("abc", "");
