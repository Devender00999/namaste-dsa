var candy = function (ratings) {
   let ltr = Array(ratings.length).fill(1);
   let rtl = Array(ratings.length).fill(1);

   for (let i = 1; i < ratings.length; i++) {
      if (ratings[i - 1] < ratings[i]) {
         ltr[i] = ltr[i - 1] + 1;
      }
   }

   for (let i = ratings.length - 2; i >= 0; i--) {
      if (ratings[i + 1] < ratings[i]) {
         rtl[i] = rtl[i + 1] + 1;
      }
   }
   console.log(rtl, ltr);
   let candies = 0;
   for (let i = 0; i < ratings.length; i++) {
      candies += Math.max(ltr[i], rtl[i]);
   }
   return candies;
};

var candy = function (ratings) {
   let n = ratings.length;
   let ans = n;

   let i = 1;
   while (i < n) {
      let up = 0;

      if (ratings[i] == ratings[i - 1]) {
         i += 1;
         continue;
      }
      while (ratings[i] > ratings[i - 1]) {
         up += 1;
         ans += up;
         i += 1;
      }

      let down = 0;
      while (ratings[i] < ratings[i - 1]) {
         down += 1;
         ans += down;
         i += 1;
      }

      ans -= Math.min(up, down);
   }
   return ans;
};
