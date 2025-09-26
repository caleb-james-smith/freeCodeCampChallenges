
function countVowels(s) {
  const vowels = ["a", "e", "i", "o", "u"];
  s = s.toLowerCase();
  let result = 0;
  for (const x of s) {
    if (vowels.includes(x)) {
      result += 1;
    }
  }
  return result;
}

function isBalanced(s) {
  const n = s.length;
  const middle = Math.floor(n/2);
  const half_1 = s.slice(0, middle);
  const half_2 = s.slice(-middle);
  const n_vowels_1 = countVowels(half_1);
  const n_vowels_2 = countVowels(half_2);
  const result = n_vowels_1 == n_vowels_2;
  console.log("result:", result);
  return result;
}



