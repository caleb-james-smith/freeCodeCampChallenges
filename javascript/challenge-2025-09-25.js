
function compareNumbers(a, b) {
  return a - b;
}

function secondLargest(arr) {
  let result = Infinity;
  console.log("arr (1):", arr);
  arr.sort(compareNumbers).reverse();
  console.log("arr (2):", arr);

  let assignments = 0;
  let i = 0;
  while (assignments < 2) {
    if (arr[i] < result) {
      result = arr[i];
      assignments += 1;
    }
    i += 1;
  }
  console.log("assignments:", assignments);
  console.log("result:", result);
  return result;
}
