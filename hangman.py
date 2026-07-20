import random

words = ["apple", "mango", "chair", "school", "python"]

word = random.choice(words)

guess = ""
chance = 6

print("Welcome to Hangman Game")

while chance > 0:

    print("\nWord : ", end="")

    for letter in word:
        if letter in guess:
            print(letter, end=" ")
        else:
            print("_ ", end="")

    user = input("\nEnter a letter: ")

    if user in guess:
        print("You already entered this letter.")
        continue

    guess = guess + user

    if user not in word:
        chance = chance - 1
        print("Wrong Guess!")
        print("Chances Left:", chance)

    if all(letter in guess for letter in word):
        print("\nCongratulations! You Won")
        print("Correct Word:", word)
        break

if chance == 0:
    print("\nGame Over")
    print("Correct Word:", word)