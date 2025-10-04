# CodeTester.py

from colorama import Fore, Back, Style, init

class CodeTester:
    def __init__(self, method, tests):
        self.method = method
        self.tests  = tests

    def runTests(self):
        print("Running test(s)...")

        n_tests = len(self.tests)
        n_passed = 0
        n_failed = 0

        for i, test in enumerate(self.tests, start=1):
            print(f"Test {i}:")
            test_passed = self.runTest(test)
            if test_passed:
                print(Fore.GREEN + f"Test {i}: PASS" + Fore.RESET)
                n_passed += 1
            else:
                print(Fore.RED + f"Test {i}: FAIL" + Fore.RESET)
                n_failed += 1
        
        print(f"Ran {n_tests} test(s): {n_passed} passed and {n_failed} failed.")
        print("Testing complete!")

    def runTest(self, test):
        input       = test["input"]
        expected    = test["expected"]
        
        output = self.method(input)

        print(f" - input:       {input}")
        print(f" - output:      {output}")
        print(f" - expected:    {expected}")

        if output == expected:
            return True
        else:
            return False
