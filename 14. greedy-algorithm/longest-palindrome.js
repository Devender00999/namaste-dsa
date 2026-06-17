var longestPalindrome = function (s) {
   let sMap = {};
   for (let i = 0; i < s.length; i++) {
      if (!sMap[s[i]]) sMap[s[i]] = 0;
      sMap[s[i]]++;
   }
   const counts = Object.values(sMap);
   let maxLength = 0;
   let hasOddFreq = false;
   for (let i = 0; i < counts.length; i++) {
      if (counts[i] % 2 == 0) {
         maxLength += counts[i];
      } else {
         maxLength += counts[i] - 1;
         hasOddFreq = true;
      }
   }
   if (hasOddFreq) return maxLength + 1;
   return maxLength;
};
