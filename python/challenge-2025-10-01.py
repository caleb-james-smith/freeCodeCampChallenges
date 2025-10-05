from CodeTester import CodeTester

def to_decimal(binary):
    result = 0
    reversed_binary = binary[::-1]
    for i, x in enumerate(reversed_binary):
        bit = int(x)
        if bit:
            result += 2 ** i
    return result

def main():
    tests = [
        {"input"    : "101",
         "expected" : 5},
        {"input"    : "1010",
         "expected" : 10},
        {"input"    : "10010",
         "expected" : 18},
        {"input"    : "1010101",
         "expected" : 85}
    ]
    tester = CodeTester(to_decimal, tests)
    tester.runTests()

if __name__ == "__main__":
    main()
