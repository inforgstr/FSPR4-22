import random


def find_num(x, guess):
    try:
        if 0 < int(guess) < 11:
            if int(guess) == x:
                print("You are genius!")
                return True
        else:
            print("enter number in range 1-10")
            return False
    except ValueError as error:
        return error


if __name__ == "__main__":
    x = random.randint(1, 11)
    while True:
        guess = int(input("find a secret number in range of 1-10: "))
        if find_num(x, guess):
            break
