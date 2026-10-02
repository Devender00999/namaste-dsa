function power(x, n) {
   if (n == 0) return 1;
   let xnpb2 = power(x, parseInt(n / 2));
   let xn = xnpb2 * xnpb2;
   if (n % 2 == 0) {
      return xn;
   } else {
      return x * xn;
   }
}

console.log(power(2, 100));
