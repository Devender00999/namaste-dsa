var maximumUnits = function (boxTypes, truckSize) {
   let sortedBoxes = boxTypes.sort((a, b) => b[1] - a[1]);
   let totalUnit = 0;
   for (let i = 0; i < sortedBoxes.length; i++) {
      let currentBox = sortedBoxes[i];
      if (truckSize == 0) {
         break;
      }
      if (currentBox[0] <= truckSize) {
         totalUnit += currentBox[1] * currentBox[0];
         truckSize -= currentBox[0];
      } else {
         totalUnit += truckSize * currentBox[1];
         truckSize -= truckSize;
      }
   }
   return totalUnit;
};
