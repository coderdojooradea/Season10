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
        terms = list(self.flashcards.keys())
        print(terms)
        weighted_terms = [term for term in terms for _ in range(max(1, self.flashcards[term]['attempts']-self.flashcards[term]['correct']))]
        print(weighted_terms)
        term = random.choice(weighted_terms if weighted_terms else terms)
        print(f"Term: {term}")
        return term

flashcard_app = FlashCard()
# flashcard_app.add_card("Python", 
#                        "A high-level programming")  
# flashcard_app.add_card("C++", 
#                        "Also a high-level programming")  
# flashcard_app.save_card()
flashcard_app.show_terms()
