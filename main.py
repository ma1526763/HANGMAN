import random
# HANGMAN PROGRAM
from hangman_art import stages, word_list
random_word = list(random.choice(word_list))
guess_word = ["_"] * len(random_word)
lives = "❤" * 6
wrong_inputs = ""
print(f"Total lives left: {lives}\nGuess the letter: {''.join(guess_word)}")
while len(lives) > 0:
    user_guess = input("Enter your guess: ")
    if user_guess in guess_word or user_guess in wrong_inputs:
        print("You already select this later. Choose another")
        continue
    if user_guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == user_guess:
                guess_word[i] = user_guess
        if guess_word == random_word:
            print("YOU GUESS IT CORRECTLY. YOU WON!!!")
            break
    else:
        lives = lives[:-1]
        wrong_inputs += user_guess
        if len(lives) == 0:
            print(f"\nYOU ARE HANGED{stages[len(lives)]}\nDeath is Truth! You have LOST the game!!\nCorrect letter was \"{''.join(random_word)}\"")
            break
        print(f"\nTotal lives left: {lives}", end="")
        print(stages[len(lives)])

    print("\nGuess the letter: ", ''.join(guess_word))
    print(f"\nWrong input list \"{wrong_inputs}\"" * (wrong_inputs != ""))
