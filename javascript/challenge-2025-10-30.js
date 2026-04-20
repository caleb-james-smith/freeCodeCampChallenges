function nthPrime(n) {
  let result = 2;
  let ith_prime = 1;
  while (ith_prime < n)
  {
    result += 1;
    if (isPrime(result))
    {
      ith_prime += 1;
    }
  }
  return result;
}

function isPrime(n)
{
  if (n < 2)
  {
    return false;
  }
  let num_divisors = getNumDivisors(n);
  if (num_divisors == 2)
  {
    return true;
  }
  else
  {
    return false;
  }
}

function getNumDivisors(n)
{
  let result = 0;
  for (let i = 1; i < n + 1; i++)
  {
    if (n % i == 0)
    {
      result += 1;
    }
  }
  return result;
}
