import random

# Load the list of possible words from the file
with open('Dataset/All_possible_words.txt', 'r') as file:
    possible_words = [line.strip() for line in file]

# Function to generate a random word from the list of possible words
def choose_random_word():
    return random.choice(possible_words)

# Function to evaluate a guess based on user-provided feedback
def evaluate_guess(target_word, guess, feedback):
    feedback_symbols = ["MISS", "MISPLACED", "EXACT"]
    feedback_text = [feedback_symbols[int(fb)] for fb in feedback]
    
    feedback_result = []
    for i, fb in enumerate(feedback_text):
        if fb == "EXACT":
            feedback_result.append(fb)
        elif fb == "MISPLACED":
            if guess[i] in target_word and target_word.count(guess[i]) > guess.count(guess[i]):
                feedback_result.append("MISPLACED")
            else:
                feedback_result.append("MISS")
        else:
            feedback_result.append("MISS")
    
    return feedback_result

# Bayesian algorithm for word selection
def bayesian_choose_word(possible_words, previous_guesses):
    scores = {word: 0 for word in possible_words}
    for word in possible_words:
        for guess, feedback in previous_guesses:
            guess_feedback = evaluate_guess(word, guess, feedback)
            if guess_feedback == feedback:
                scores[word] += 1
    best_words = [word for word, score in scores.items() if score == max(scores.values())]
    return random.choice(best_words)

# Main game loop
target_word = choose_random_word()
attempts = 0
previous_guesses = []

print("Welcome to the Word Guessing Game!")
print("Please think of a word and provide feedback as follows:")
print("0 for MISS, 1 for MISPLACED, and 2 for EXACT.")

while True:
    attempts += 1
    guess = bayesian_choose_word(possible_words, previous_guesses)
    feedback = []
    while True:
        try:
            feedback_input = input(f"Attempt {attempts}: {guess} - Enter feedback (0/1/2): ")
            feedback_input = [int(f) for f in feedback_input]
            if all(f in [0, 1, 2] for f in feedback_input) and len(feedback_input) == len(target_word):
                feedback = feedback_input
                break
            else:
                print("Invalid feedback. Please provide feedback as 0, 1, or 2.")
        except ValueError:
            print("Invalid feedback. Please provide feedback as 0, 1, or 2.")
    
    previous_guesses.append((guess, feedback))
    
    if feedback.count(2) == len(target_word):
        print(f"Congratulations! The word was '{target_word}'. It took {attempts} attempts to guess.")
        break

print("Game over!")
