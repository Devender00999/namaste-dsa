var canPlaceFlowers = function (flowerbed, n) {
   if (flowerbed.length == 1 && flowerbed[0] == 0) return true;
   let len = flowerbed.length;
   for (let i = 0; i < flowerbed.length; i++) {
      if (flowerbed[i] == 0 && n != 0) {
         if (
            i > 0 &&
            i < len - 1 &&
            flowerbed[i - 1] != 1 &&
            flowerbed[i + 1] != 1
         ) {
            flowerbed[i] = 1;
            n -= 1;
         }
         if (i == 0 && flowerbed[i + 1] == 0) {
            flowerbed[i] = 1;
            n -= 1;
         }
         if (i == len - 1 && flowerbed[i - 1] == 0) {
            flowerbed[i] = 1;
            n -= 1;
         }
      }
   }

   // for first index
   console.log(flowerbed, n);
   return 0 == n;
};

var canPlaceFlowers = function (flowerbed, n) {
   let len = flowerbed.length;
   for (let i = 0; i < flowerbed.length; i++) {
      let left = i == 0 || flowerbed[i - 1] == 0;
      let right = i == len - 1 || flowerbed[i + 1] == 0;
      if (flowerbed[i] == 0 && left && right) {
         flowerbed[i] = 1;
         n--;
      }
   }

   return 0 == n;
};
