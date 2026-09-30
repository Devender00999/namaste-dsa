// f(5) = 5 x 4 x 3 x 2 x 1
// f(4) = 4 x 3 x 2 x 1
// f(4) = 4 x 3 x 2 x 1

// f(n) = n x f(n - 1)

function factorial(n) {
   if (n == 1) return 1;
   return n * factorial(n - 1);
}

console.log(factorial(5));
