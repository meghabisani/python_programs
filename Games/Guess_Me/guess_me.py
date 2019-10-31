from random import randint


def guess_game():
    num = randint(1, 100)

    print("-----WELCOME TO GUESS ME!-----")
    print("I am thinking of a number between 1 to 100")
    print("If your guess is within 10 of my number, I will tell you you're WARM!")
    print("If your guess is more then 10 away from my number, I will tell you you're COLD!")
    print("If your guess is closer than your recent guess, I will tell you you're WARMER!")
    print("If your guess is father than your recent guess, I will tell you you're COLDER!")
    print("\n-----LET'S PLAY-----")

    guesses = [0]

    while True:

        user_guess = int(input("\nI am thinking of a number between 1 to 100.\nWhat's your guess? "))

        if user_guess < 1 or user_guess > 100:
            print("OUT OF BOUNDS! Please try again: ")
            continue

        if num == user_guess:
            print(f"\nCONGRATULATIONS!! YOU WON\nYou Guessed it in only {len(guesses)} GUESSES!! ")
            break

        guesses.append(user_guess)

        if guesses[-2]:

            if abs(num - user_guess) < abs(num - guesses[-2]):
                print("WARMER!!")
            else:
                print("COLDER!!")

        else:
            if abs(num - user_guess) <= 10:
                print("WARM!")
            else:
                print("COLD!")


if __name__ == '__main__':
    guess_game()
