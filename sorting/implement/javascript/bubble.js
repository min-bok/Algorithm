const arr = [9, 8, 2, 4, 3];

// 오름차순 정렬
// const sort = (arr) => {
//   for (let i = arr.length - 1; i > 0; i--) {
//     for (let j = 0; j < i; j++) {
//       console.log(`i: ${arr[i]}`);
//       console.log(`j: ${arr[j]}`);
//       console.log(`==========================`);

//       //   if (arr[j] > arr[j + 1]) {
//       //     let temp = arr[j];
//       //     arr[j] = arr[j + 1];
//       //     arr[j + 1] = temp;
//       //   }
//     }
//   }

//   return arr;
// };

const sort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      console.log(arr[i]);
      console.log(arr[j]);
      console.log("========================");
    }
  }

  return arr;
};

// 내림차순 정렬
// const sort = (arr) => {
//   for (let i = arr.length - 1; i > 0; i--) {
//     for (let j = 0; j < i; j++) {
//       if (arr[j] > arr[j + 1]) {
//         let temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }

//   return arr;
// };

console.log(sort(arr));
