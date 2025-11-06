from CodeTester import CodeTester

def to_binary(decimal):
    result = bin(decimal)
    result = result[2:]
    return result

def main():
    tests = [
        {"input"    : 5,
         "expected" : "101"},
        {"input"    : 12,
         "expected" : "1100"},
        {"input"    : 50,
         "expected" : "110010"},
        {"input"    : 99,
         "expected" : "1100011"}
    ]
    tester = CodeTester(to_binary, tests)
    tester.runTests()

if __name__ == "__main__":
    main()
