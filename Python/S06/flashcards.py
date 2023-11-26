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

    def load_flashcards(self):
        try:
            with open(self.filename, 'r') as f:
                self.flashcards = json.load(f)
        except FileNotFoundError:
            print(f"Flash card {self.filename} not found")        


flashcard_app = FlashCard()
flashcard_app.add_card("Python", 
                       "A high-level programming")        
