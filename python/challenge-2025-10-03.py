from CodeTester import CodeTester

def check_strength(password):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_lower = letters.lower()
    letters_upper = letters.upper()
    numbers = "0123456789"
    special_characters = "!@#$%^&*"

    passed_rules = 4 * [False]
    num_rules_to_strength = {
        0 : "weak",
        1 : "weak",
        2 : "medium",
        3 : "medium",
        4 : "strong"
    }

    password_length = len(password)

    contains_lower = False
    contains_upper = False
    contains_number = False
    contains_special_character = False
    
    for x in password:
        if x in letters_lower:
            contains_lower = True
        if x in letters_upper:
            contains_upper = True
        if x in numbers:
            contains_number = True
        if x in special_characters:
            contains_special_character = True

    if password_length >= 8:
        passed_rules[0] = True
    if contains_lower and contains_upper:
        passed_rules[1] = True
    if contains_number:
        passed_rules[2] = True
    if contains_special_character:
        passed_rules[3] = True
    
    passed_rules_int = [int(x) for x in passed_rules]
    num_rules_passed = sum(passed_rules_int)
    result = num_rules_to_strength[num_rules_passed]

    return result

def main():
    tests = [
        {"input"    : "123456",
         "expected" : "weak"},
        {"input"    : "pass!!!",
         "expected" : "weak"},
        {"input"    : "Qwerty",
         "expected" : "weak"},
        {"input"    : "PASSWORD",
         "expected" : "weak"},
        {"input"    : "PASSWORD!",
         "expected" : "medium"},
        {"input"    : "PassWord%^!",
         "expected" : "medium"},
        {"input"    : "qwerty12345",
         "expected" : "medium"},
        {"input"    : "S3cur3P@ssw0rd",
         "expected" : "strong"},
        {"input"    : "C0d3&Fun!",
         "expected" : "strong"}
    ]
    tester = CodeTester(check_strength, tests)
    tester.runTests()

if __name__ == "__main__":
    main()
