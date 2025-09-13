function reverseSentence(sentence) {
  const word_list = sentence.split(/\s+/);
  // console.log("word_list (1):", word_list);
  word_list.reverse();
  // console.log("word_list (2):", word_list);
  let result = word_list.join(" ");
  // console.log("result:", result);
  return result;
}

function test_io(input) {
  let output = reverseSentence(input);
  console.log("Testing reverseSentence:");
  console.log(" - input:", input);
  console.log(" - output:", output);
}

function main() {
  test_io("world hello");
  test_io("push commit git");
}

if (require.main == module) {
  main();
}
