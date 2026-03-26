import random


def random_word(file):
    return random.choice(file.readlines())

def main():
    file = open("words.txt", "r")
    print(random_word(file))

    file.close()

main()