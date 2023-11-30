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
def evaluate_guess(secret_word, guess):
    guess_copy = guess
    feedback = []
    remaining_secret_letters = list(secret_word)
    # First, check exact matches (greens)
    for i, (g1, g2) in enumerate(zip(secret_word, guess_copy)):
        if g1 == g2:
            feedback.append("🟩")
            remaining_secret_letters.remove(g1)
            guess_copy = guess_copy[:i] + "🟩" + guess_copy[i+1:]
        else:
            feedback.append("⬛")
    feedback_str = "".join(feedback)
    # Then, check letters but not in location (yellows)
    for i, g2 in enumerate(guess_copy):
        if g2 in remaining_secret_letters:
            feedback_str = feedback_str[:i] + "🟨" + feedback_str[i+1:]
            remaining_secret_letters.remove(g2)
    feedback = feedback_str
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

# Main game loop
target_word = choose_random_word()
attempts = 0
previous_guesses = []

print(f"Target word: {target_word}")

while True:
    attempts += 1
    guess = bayesian_choose_word(possible_words, previous_guesses)
    feedback = evaluate_guess(target_word, guess)
    print(f"Attempt {attempts}:")
    print(f"Guess: {guess}")
    print(f"Feedback: {feedback}")
    previous_guesses.append((guess, feedback))
    if target_word == guess:
        print(f"Found the word in {attempts} attempts: {guess}")
        break

print("Game over!")