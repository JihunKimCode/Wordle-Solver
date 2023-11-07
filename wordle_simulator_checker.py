# Wordle simulator

import random

# List of possible secret five-letter words
word_list = ["apple", "table", "fable", "maple", "camel", "hello", "world", "happy", "music"]

# Choose the secret word from the list randomly
secret_word = random.choice(word_list)
print(secret_word)
print("---------------------------- << Wordle Simulator >> ----------------------------")
print("Try to guess the 5-letter word!")
print("-----------------------------------Description----------------------------------")
print("X: Letter is not in the word.")
print("-: Letter appears in the word, but in the wrong spot.")
print("--------------------------------------------------------------------------------\n")

attempts = 0
feedback_history = []

print("Try to guess the 5-letter word!")

while True:
    guess = input("Enter your guess (5 letters): ").lower()    
    # Error case
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue
    
    guess_copy = guess
    attempts += 1
    
    # Secret word found
    if guess == secret_word:
        print(f"Congratulations! You guessed the secret word '{secret_word}' in {attempts} attempts.")
        break

    else:
        feedback = []
        remaining_secret_letters = list(secret_word)
        # First, check exact matches (greens)
        for i, (g1, g2) in enumerate(zip(secret_word, guess_copy)):
            if g1 == g2:
                feedback.append(g1)
                remaining_secret_letters.remove(g1)
                guess_copy = guess_copy[:i] + 'O' + guess_copy[i+1:]
            else:
                feedback.append("X")
        feedback_str = "".join(feedback)
        
        # Then, check letters but not in location (yellows)
        for i, g2 in enumerate(guess_copy):
            if g2 in remaining_secret_letters:
                feedback_str = feedback_str[:i] + "-" + feedback_str[i+1:]
                remaining_secret_letters.remove(g2)

        feedback_history.append(feedback_str)
        # Print out feedback history
        for feedbacks in feedback_history:
            print(feedbacks)
