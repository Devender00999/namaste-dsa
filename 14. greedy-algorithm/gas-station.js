var canCompleteCircuit = function (gas, cost) {
   for (let i = 0; i < gas.length; i++) {
      let start = i;
      let fuel = gas[i];
      let j = 0;
      let nextStation = 0;
      while (j < gas.length) {
         let currentStation = (start + j) % gas.length;
         if (cost[currentStation] > fuel) {
            break;
         }
         nextStation = (start + j + 1) % gas.length;

         fuel = fuel - cost[currentStation] + gas[nextStation];
         j += 1;
      }
      if (j == gas.length) return i;
   }
   return -1;
};
