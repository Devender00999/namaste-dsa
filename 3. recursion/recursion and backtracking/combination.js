let arr = [".;", "abc", "def", "ghi", "jkl", "mnop", "qrst", "uv", "wxyz"];
function getCombinations(arr, str) {
   if (str.length == 0) {
      return [""];
   }
   const curr = str[0];
   const currNumber = parseInt(curr);
   let prevRes = getCombinations(arr, str.slice(1));
   const res = [];
   for (let i = 0; i < arr[currNumber].length; i++) {
      for (let j = 0; j < prevRes.length; j++) {
         res.push(arr[currNumber][i] + prevRes[j]);
      }
   }
   return res;
}

console.log(getCombinations(arr, "573"));
