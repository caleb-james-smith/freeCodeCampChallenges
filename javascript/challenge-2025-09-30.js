
function formatNumber(number) {
  const country_code  = number.slice(0, 1);
  const area_code     = number.slice(1, 4);
  const part_1        = number.slice(4, 7);
  const part_2        = number.slice(7);
  const result = `+${country_code} (${area_code}) ${part_1}-${part_2}`;
  return result;
}



