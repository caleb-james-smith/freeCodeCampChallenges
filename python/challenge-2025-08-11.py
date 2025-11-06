
def countVowels(s):
    result = 0
    vowels = ["a", "e", "i", "o", "u"]
    s = s.lower()
    for x in s:
        if x in vowels:
            result += 1
    return result

def is_balanced(s):
    n = len(s)
    middle = n//2 
    half_1 = s[:middle]
    half_2 = s[-middle:]
    n_vowels_1 = countVowels(half_1)
    n_vowels_2 = countVowels(half_2)
    result = n_vowels_1 == n_vowels_2
    print(f"result: {result}")
    return result



