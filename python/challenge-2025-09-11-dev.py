from CodeTester import CodeTester

def reverse_sentence(sentence):
    word_list = sentence.split()
    word_list.reverse()
    result = " ".join(word_list)
    return result

def main():
    tests = [
        {"input"    : "world hello",
         "expected" : "hello world"},
        {"input"    : "push commit git",
         "expected" : "git commit push"},
        {"input"    : "npm  install   apt    sudo",
         "expected" : "sudo apt install npm"},
        {"input"    : "import    default   function  export",
         "expected" : "export function default import"},
        {"input"    : "chicken biscuit",
         "expected" : "biscuit chicken"},
        {"input"    : "hasta la pasta",
         "expected" : "pasta la hasta"}
    ]
    tester = CodeTester(reverse_sentence, tests)
    tester.runTests()

if __name__ == "__main__":
    main()
