import json
import random

class FlashCard:
    def __init__(self, filename='flashcards.json'):
        self.flashcards = {}
        self.filename = filename
        self.load_flashcards()

    def add_card(self, term, definition):
        self.flashcards[term] = {'definition': definition, 
                                'correct': 0,
                                'attempts': 0}

    def save_card(self):
        with open(self.filename, 'w') as f:
            json.dump(self.flashcards, f, indent=4)

    def load_flashcards(self):
        try:
            with open(self.filename, 'r') as f:
                self.flashcards = json.load(f)
        except FileNotFoundError:
            print(f"Flash card {self.filename} not found")
        except json.JSONDecodeError:
            print(f"Flash card app {self.filename} is corrupted or not in JSON format.")

    def show_terms(self):
        pass

flashcard_app = FlashCard()
print(flashcard_app.flashcards)
flashcard_app.add_card("Python", 
                       "A high-level programming")  
flashcard_app.add_card("C++", 
                       "Also a high-level programming")  
print(flashcard_app.flashcards)
flashcard_app.save_card()
