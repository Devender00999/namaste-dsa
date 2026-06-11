var lemonadeChange = function (bills) {
   //  my approach
   let changes = { 5: 0, 10: 0, 20: 0 };
   for (let i = 0; i < bills.length; i++) {
      changes[bills[i]]++;
      let change = bills[i] - 5;
      while (change >= 10 && changes["10"] > 0) {
         change -= 10;
         changes["10"] = changes["10"] - 1;
      }
      while (change >= 5 && changes["5"] > 0) {
         changes["5"] -= 1;
         change -= 5;
      }
      if (change != 0) return false;
   }

   return true;
};

function lemonadeChange(bills) {
   // akshay's approach
   let wallet = [0, 0];
   for (let i = 0; i < bills.length; i++) {
      if (bills[i] == 5) {
         wallet[0]++;
      } else if (bills[i] == 10) {
         wallet[1] += 1;
         wallet[0] -= 1;
      } else {
         if (wallet[1]) {
            wallet[1]--;
            wallet[0]--;
         } else {
            wallet[0] -= 3;
         }
      }
      if (wallet[0] < 0) return false;
   }
   return true;
}
