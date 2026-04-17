var topKFrequent = function (nums, k) {
   const frequency = {};
   for (let i = 0; i < nums.length; i++) {
      const item = nums[i];
      if (!frequency[item]) frequency[item] = { element: item, count: 0 };
      frequency[item].count += 1;
   }

   const pq = new MinPriorityQueue((i) => i.count);
   const values = Object.entries(frequency);
   for (let i = 0; i < values.length; i++) {
      const [key, value] = values[i];
      pq.push(value);
      if (pq.size() > k) {
         pq.pop();
      }
   }
   return pq.toArray().map((item) => Number(item.element));
};

console.log(topKFrequent([1,2,1,1,1,1,2,3,34,5,6,5,43,34,4,3,3,3], 2))