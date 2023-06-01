# 정렬(Sorting)

- 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 의미함
- 일반적으로 문제 상항에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨
  - 데이터의 갯수가 적을때
  - 데이터의 범위가 특정 범위로 한정되어있을때
  - 이미 데이터가 거의 정렬되어있는 경우 등

# 선택 정렬

- N-1개의 단계를 거침
- 가장 작은것을 선택해서 앞으로 보내는 정렬 기법
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- 매 단게에서 가장 작은것을 선택하는데 약 N번의 연산이 필요함(선형탐색)
- 결과적으로 약 N개의 단계를 거친다는 점에서 최약의 경우 O(N^2)의 시간복잡도를 가짐
- 비효율적이지만 동작방식이 직관적이며 구현난이도가 낮음
- 탐색범위는 반복시 마다 줄어들게 되며, 매번 가장 작은 데이터를 찾기위해 탐색 범위만큼을 탐색해야하므로, 매번 선형 탐색을 수행하는 것과 동일
- 이중 반복문을 통해 이러한 선택 정렬 구현이 가능함
- 시간복잡도 O(N^2)로 비효율적인 정렬 알고리즘 중 하나

```js
// javascript
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
```

```python
# python
def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```
