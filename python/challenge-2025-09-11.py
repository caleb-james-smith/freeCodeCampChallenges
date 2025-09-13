def reverse_sentence(sentence):
    word_list = sentence.split()
    word_list.reverse()
    result = " ".join(word_list)
    return result

def test_io(input):
    output = reverse_sentence(input)
    print(f"input: {input}")
    print(f"output: {output}")

def main():
    test_io("world hello")

if __name__ == "__main__":
    main()
