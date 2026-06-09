var twoCitySchedCost = function (costs) {
   costs.sort((a, b) => b[1] - b[0] - (a[1] - a[0]));

   let finalCost = 0;
   let totalCandidate = costs.length;
   for (let i = 0; i < totalCandidate; i++) {
      if (i < totalCandidate / 2) {
         finalCost += costs[i][0];
      } else {
         finalCost += costs[i][1];
      }
   }
   return finalCost;
};
