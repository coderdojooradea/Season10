import pygame
import random

class Card:
    rank = None
    suit = None
    image = None
    
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.image = pygame.image.load('./Cards/'+self.rank+'_of_'+self.suit.lower()+'.svg')


class Deck:
    def __init__(self, card_image_path):
        self.cards =[]
        # Card values
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

        for suit in suits:
            for rank in ranks:
                image_path = f"{card_image_path}/{rank.lower()}_of_{suit.lower()}.svg"
                self.cards.append(Card(rank, suit, image_path))

        self.shuffle()

        def shuffle(self):
            random.shuffle(self.cards)

        def draw(self):
            if len(self.card)>0:
                return self.cards.pop()
            else:
                return None
