// power(x, n)

// 2, 5 = 32
// 2, 4 = 2 * 2 ^ 3
// 2, 3 = 2 * 2 ^ 2

function calculatePower(x, n) {
   if (x == 0) return 0;
   if (n == 0) return 1;
   return x * calculatePower(x, n - 1);
}

console.log(calculatePower(2, 10));
