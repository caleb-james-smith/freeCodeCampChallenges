function reverseSentence(sentence) {
  const word_list = sentence.split(/\s+/);
  word_list.reverse();
  let result = word_list.join(" ");
  return result;
}

function test_io(input) {
  let output = reverseSentence(input);
  console.log(" - input:", input);
  console.log(" - output:", output);
}

function run_tests(inputs) {
  console.log("Running tests...");
  // FIXME: Start with test number 1.
  for (let i = 0; i < inputs.length; i++) {
    // FIXME: Print number as white (not yellow) and remove space between number and colon.
    console.log("Test", i, ":");
    test_io(inputs[i]);
  }
  console.log("Testing complete!");
}

function main() {
  const inputs = [
    "world hello",
    "push commit git",
    "npm  install   apt    sudo",
    "import    default   function  export"
  ];
  run_tests(inputs);
}

if (require.main == module) {
  main();
}
