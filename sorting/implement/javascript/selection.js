arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

// 선택정렬 구현하기
// 제일 앞에꺼 찾고, 제일 작은거 찾아서 제일 앞에꺼랑 바꾸기

const sort = (arr) => {
  // i: 제일 앞에 있는 요소 선택
  for (let i = 0; i < arr.length; i++) {
    let min_idx = i;
    // j: 이미 정렬된 요소 제외하고 탐색
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[min_idx] > arr[j]) {
        min_idx = j;
      }
    }

    let temp = arr[i];
    arr[i] = arr[min_idx];
    arr[min_idx] = temp;
  }

  return arr;
};

console.log(sort(arr)); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
