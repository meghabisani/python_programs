def main():

    with open('words.txt', 'r') as rf:
        word_list = rf.read()

    word_list = [word.lower() for word in word_list.split('\n')]

    input_word = input("Please Enter the Phrase: ")
    r_word = input_word.lower().replace(" ", "")

    for word in word_list:
        if sorted(list(r_word)) == sorted(list(word)) and (not (set(r_word)) - (set(word))) \
                and (not len(r_word) - len(word)) and (not (r_word == word)):
                    print(f"Anagram of '{input_word}' is '{word}'")


if __name__ == '__main__':
    main()
