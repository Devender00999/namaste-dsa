var leastInterval = function (tasks, n) {
   let map = {};
   let maxFreq = 0;
   for (let i = 0; i < tasks.length; i++) {
      let currTask = tasks[i];
      if (!map[currTask]) map[currTask] = 0;
      map[currTask] += 1;
      maxFreq = Math.max(maxFreq, map[currTask]);
   }
   let countOfMaxFreq = 0;
   const frequencies = Object.values(map);

   for (let i = 0; i < frequencies.length; i++) {
      if (frequencies[i] == maxFreq) {
         countOfMaxFreq += 1;
      }
   }
   let cycles = (n + 1) * (maxFreq - 1) + countOfMaxFreq;
   return Math.max(tasks.length, cycles);
};
