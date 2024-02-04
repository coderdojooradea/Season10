import random

# Define the path to the file you downloaded
file_path = 'words.txt'

def filter_five_letter_words(file_path):
    """
    Filter and return a list of five-letter words from the provided file.
    """
    five_letter_words = []

    # Attempt to open and read the file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip()  # Remove newline characters and whitespace
                if len(word) == 5:  # Check if the word is exactly five letters
                    five_letter_words.append(word.lower())  # Add to the list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return five_letter_words

def select_target_word(word_list):
    # Randomly select and return a target word from the list
    return random.choice(word_list)

def evaluate_guess(guess, target_word):
    # Evaluate the player's guess and return feedback
    score = ['⬛','⬛','⬛','⬛','⬛']
    target_letters = []
    if guess == target_word:
        print("Congratulations, you've guessed the word!")
        return ['🟩','🟩','🟩','🟩','🟩']
    for i in range(5):
        if guess[i] == target_word[i]:
            score[i] = '🟩'
    for i in range(5):
        if target_word[i] not in target_letters:
            target_letters.append(target_word[i])
    for i in range(5):
        if guess[i] in target_letters and guess[i] != target_word[i]:
            score[i] = '🟨'

    return score
    

def display_feedback(feedback):
    # Display feedback to the player about their guess
    display = ""
    for i in range(5):
        display += feedback[i]
    print(f"Score: {display}")
        

def play_wordle(word_list):
    target_word = select_target_word(word_list)
    attempts = 0
    max_attempts = 6

    print("Welcome to Wordle! Guess the 5-letter word.")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}/{max_attempts}. Enter your guess: ").lower()
        
        # Ensure the guess is valid
        if len(guess) != 5 or guess not in word_list:
            print("Invalid guess. Please enter a five-letter word.")
            continue
        
        # Evaluate the guess and display feedback
        feedback = evaluate_guess(guess, target_word)
        display_feedback(feedback)
        
        if guess == target_word:
            print("Congratulations, you've guessed the word!")
            break
        
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The word was {target_word}.")

if __name__ == "__main__":
    word_list = filter_five_letter_words(file_path)  # Populate with a real list of words
    play_wordle(word_list)
