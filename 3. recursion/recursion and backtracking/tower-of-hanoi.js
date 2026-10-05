function toi(n, a, b, c) {
   if (n == 0) return;
   toi(n - 1, a, c, b);
   console.log(`${a} -> ${b}`);
   toi(n - 1, c, b, a);
}

toi(100, "A", "B", "C");
