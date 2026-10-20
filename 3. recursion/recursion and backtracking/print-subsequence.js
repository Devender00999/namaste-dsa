function printSubSequence(ques, ans) {
   if (ques.length == 0) {
      console.log(ans);
      return;
   }
   const ch = ques[0];
   const roq = ques.slice(1);

   printSubSequence(roq, ans);
   printSubSequence(roq, ans + ch);
}

printSubSequence("abcd", "");
