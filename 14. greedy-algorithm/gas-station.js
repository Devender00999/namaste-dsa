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

var canCompleteCircuit = function (gas, cost) {
   let currGain = 0;
   let totalGain = 0;
   let ans = 0;

   for (let i = 0; i < gas.length; i++) {
      let gain = gas[i] - cost[i];
      currGain = gain + currGain;
      totalGain += gain;

      if (currGain < 0) {
         currGain = 0;
         ans = i + 1;
      }
   }

   return totalGain < 0 ? -1 : ans;
};
