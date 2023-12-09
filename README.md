# Wordle Solver
Using Bayesian Algorithm, make a model to play [Wordle](https://www.nytimes.com/games/wordle/index.html). Our Bayesian model can find the target word in 3.87 on average.

# Works Flow
## Dataset
- **Training dataset**: [All possible words that have 5 characters that Wordle takes](https://github.com/3b1b/videos/blob/master/_2022/wordle/data/possible_words.txt)
- **Testing dataset**: [Previous Wordle answers](https://www.fiveforks.com/wordle/)
- **Algorithm**: Bayesian model

## Main Goal
1. Random guess from list (whole word list).
2. Feedback based on the letter location (yellow, green, gray).
3. Go back and guess with the feedback information.
4. Find the best word to start.

## Our Model
* **Models/play_wordle_reduced_bestword.ipynb**
  * Run model along with training and testing phase to find and test the best starting word
* **Wordle Player/simulator_with_userinput.py**
  * You already choose the best starting word
    * Fix *line 57* to use your start word.
  * Just want to test the Bayesian Algorithm we implemented
