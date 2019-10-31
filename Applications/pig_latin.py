# 1) If word starts with vowel, add "ay" at the end
#
# 2) If word does not start with vowel then put first letter at the end, then add "ay"
#
# Examples:
# apple -> appleay
# word -> ordway


def pig_latin(word):
    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


def main():
    print(pig_latin('apple'))


main()
