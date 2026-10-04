function pzz(n) {
   if (n == 0) return;
   console.log("Pre  ", n);
   pzz(n - 1);
   console.log("In   ", n);
   pzz(n - 1);
   console.log("Post ", n);
}

pzz(3);
