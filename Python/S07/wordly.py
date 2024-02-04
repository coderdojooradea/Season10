import random

def select_target_word(word_list):
    # Randomly select and return a target word from the list
    pass

def evaluate_guess(guess, target_word):
    # Evaluate the player's guess and return feedback
    pass

def display_feedback(feedback):
    # Display feedback to the player about their guess
    pass

def play_wordle(word_list):
    target_word = select_target_word(word_list)
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 5 or guess not in word_list:
            print("Invalid guess. Please enter a five-letter word.")
            continue
        
        feedback = evaluate_guess(guess, target_word)
        display_feedback(feedback)
        
        if guess == target_word:
            print("Congratulations, you've guessed the word!")
            break
        
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The word was {target_word}.")

if __name__ == "__main__":
    word_list = ["words", "to", "fill"]  # Populate with a real list of words
    play_wordle(word_list)
