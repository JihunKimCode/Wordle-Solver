import random

# Load the list of possible words from the file
with open('Dataset/All_possible_words.txt', 'r') as file:
    possible_words = [line.strip() for line in file]

# Define feedback symbols
MISS = "⬛"
MISPLACED = "🟨"
EXACT = "🟩"

# Function to generate a random word from the list of possible words
def choose_random_word():
    return random.choice(possible_words)

# Function to evaluate a guess based on feedback
def evaluate_guess(target_word, guess):
    feedback = []
    for i, char in enumerate(guess):
        if char == target_word[i]:
            feedback.append(EXACT)
        elif char in target_word:
            feedback.append(MISPLACED)
        else:
            feedback.append(MISS)
    return "".join(feedback)

# Bayesian algorithm for word selection
def bayesian_choose_word(possible_words, previous_guesses):
    scores = {word: 0 for word in possible_words}
    for word in possible_words:
        for guess, feedback in previous_guesses:
            guess_feedback = evaluate_guess(word, guess)
            if guess_feedback == feedback:
                scores[word] += 1
    best_words = [word for word, score in scores.items() if score == max(scores.values())]
    return random.choice(best_words)

def play_game(words):
    for word in words:
        target_word = word
        attempts = 0
        previous_guesses = []

        # print(f"Target word: {target_word}")

        while True:
            attempts += 1
            guess = bayesian_choose_word(possible_words, previous_guesses)
            feedback = evaluate_guess(target_word, guess)
            print(f"Attempt {attempts}:")
            # print(f"Guess: {guess}")
            # print(f"Feedback: {feedback}")
            previous_guesses.append((guess, feedback))
            if target_word == guess:
                print(f"Found the word in {attempts} attempts: {guess}")
                break
        # print("Game over!")
    return attempts

# Main game loop
# target_word = choose_random_word()
machine_attempts = []
with open('Dataset/All_possible_words.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        words = line.split()
        machine_attempts.append(play_game(words))
    
print(f"Machine got the correct answer in {sum(machine_attempts)/len(machine_attempts)} attempts on average")
print(f"Min Guess was {min(machine_attempts)} and Max Guess was {max(machine_attempts)}")