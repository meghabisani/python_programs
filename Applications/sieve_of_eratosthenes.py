"""
The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
"""


def sieve(user_num):
    num_list = list(range(2, user_num+1))

    for num in range(2, int(user_num ** 0.5) + 1):

        if num in num_list:

            for item in range(num*2, user_num + 1, num):
                if item in num_list:
                    num_list.remove(item)

    return num_list


def find_primes():
    while True:
        try:
            user_input = int(input("Please enter the number till you want to find prime numbers: "))
        except ValueError:
                print("Please enter Integer only!!")
                continue
        else:
            if user_input > 0:
                result = sieve(user_input)
            else:
                print("Please enter positive number!!")
                continue

        print("The prime numbers are: ", result)
        print("The total prime numbers are: ", len(result))
        break


if __name__ == "__main__":
    find_primes()
