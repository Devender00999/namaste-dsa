function getSubSequence(str) {
   if (str.length == 0) {
      return [""];
   }
   let cChar = str[0];
   let seq = str.slice(1);
   let res = getSubSequence(seq);
   let result = [];
   for (let i = 0; i < res.length; i++) {
      result.push(res[i]);
      result.push(cChar + res[i]);
   }
   return result;
}

console.log(getSubSequence("123"));
