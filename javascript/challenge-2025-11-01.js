
function verify(message, key, signature) {
  const message_value = getValueOfString(message);
  const key_value = getValueOfString(key);
  const total_value = message_value + key_value;
  if (total_value === signature) {
    return true;
  } else {
    return false;
  }
}

function getValueOfString(string) {
  let result = 0;
  for (let x of string) {
    const value = getValueOfChar(x);
    result += value;
  }
  return result;
}

function getValueOfChar(x) {
  let result = 0;
  const x_code = x.charCodeAt(0);
  if ('a'.charCodeAt(0) <= x_code && x_code <= 'z'.charCodeAt(0)) {
    result = x_code - 'a'.charCodeAt(0) + 1;
  }
  if ('A'.charCodeAt(0) <= x_code && x_code <= 'Z'.charCodeAt(0)) {
    result = x_code - 'A'.charCodeAt(0) + 27;
  }
  return result;
}



