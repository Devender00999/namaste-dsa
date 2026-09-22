let store = {};

// top down approach(memoization)
const fibonacci = (n) => {
   if (n <= 1) return n;
   if (!store[n]) {
      store[n] = fibonacci(n - 1) + fibonacci(n - 2);
   }
   return store[n];
};

console.log(fibonacci(10));

// tabulation
const fib = (n) => {
   if (n <= 1) return n;
   let store = [0, 1];

   for (let i = 2; i <= n; i++) {
      store[i] = store[i - 1] + store[i - 2];
   }

   return store[n];
};
console.log(fib(10));
