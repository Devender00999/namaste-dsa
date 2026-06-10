var findContentChildren = function (g, s) {
   let i = 0;
   j = 0;
   g.sort((a, b) => a - b);
   s.sort((a, b) => a - b);
   while (i < g.length && j < s.length) {
      if (g[i] <= s[j]) {
         i++;
         j++;
      } else {
         j++;
      }
   }
   return i;
};
