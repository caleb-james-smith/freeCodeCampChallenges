from CodeTester import CodeTester

def reverse_sentence(sentence):
    word_list = sentence.split()
    word_list.reverse()
    result = " ".join(word_list)
    return result

def main():
    tests = [
        {"input"    : "hello world",
         "expected" : "world hello"},
    ]
    tester = CodeTester(reverse_sentence, tests)
    tester.runTests()

if __name__ == "__main__":
    main()
