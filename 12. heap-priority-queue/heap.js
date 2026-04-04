class MinHeap {
   constructor() {
      // this.heap = [];
      this.heap = [5, 10, 20, 30];
   }

   getLeftChildIndex(i) {
      return 2 * i + 1;
   }

   getRightChildIndex(i) {
      return 2 * i + 2;
   }

   getParentIndex(i) {
      return Math.floor((i - 1) / 2);
   }

   insert(elem) {
      this.heap.push(elem);
      this.heapifyUp(this.heap.length - 1);
   }

   // heapifyUp() {
   //    let currIdx = this.heap.length - 1;
   //    let parentIndex = this.getParentIndex(currIdx);
   //    while (currIdx > 0 && this.heap[parentIndex] > this.heap[currIdx]) {
   //       let temp = this.heap[parentIndex];
   //       this.heap[parentIndex] = this.heap[currIdx];
   //       this.heap[currIdx] = temp;
   //       currIdx = parentIndex;
   //       parentIndex = this.getParentIndex(currIdx);
   //    }
   // }
   heapifyUp(i) {
      while (i > 0) {
         let parentIndex = this.getParentIndex(i);
         if (this.heap[i] < this.heap[parentIndex]) {
            [this.heap[i], this.heap[parentIndex]] = [
               this.heap[parentIndex],
               this.heap[i],
            ];
            i = parentIndex;
         } else {
            break;
         }
      }
   }
}

const heap = new MinHeap();
heap.insert(1);
heap.insert(0);
console.log(heap.heap);
