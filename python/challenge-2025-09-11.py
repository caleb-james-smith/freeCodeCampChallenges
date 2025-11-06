def reverse_sentence(sentence):
    word_list = sentence.split()
    word_list.reverse()
    result = " ".join(word_list)
    return result

def test_io(input):
    output = reverse_sentence(input)
    print(f" - input:   {input}")
    print(f" - output:  {output}")

def run_tests(inputs):
    print("Running tests...")
    for i, input in enumerate(inputs, start=1):
        print(f"Test {i}:")
        test_io(input)
    print("Testing complete!")

def main():
    inputs = [
        "world hello",
        "push commit git",
        "npm  install   apt    sudo",
        "import    default   function  export"
    ]
    run_tests(inputs)

if __name__ == "__main__":
    main()
