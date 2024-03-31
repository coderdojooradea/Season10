import pygame
import random
import os

class Card:
    rank = None
    suit = None
    image = None
    
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        card_img_path = os.path.join(os.getcwd(),'Cards')
        card_img_name = self.rank+'_of_'+self.suit.lower()+'.svg'
        full_img_path = os.path.join(card_img_path, card_img_name)
        print(f" Card class filename: {full_img_path}")
        self.image = pygame.image.load(full_img_path)


class Deck:
    def __init__(self, card_image_path):
        self.cards =[]
        # Card values
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

        for suit in suits:
            for rank in ranks:
                image_path = f"{card_image_path}/{rank.lower()}_of_{suit.lower()}.svg"
                
                # print(image_path)
                self.cards.append(Card(suit,rank))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            return None
