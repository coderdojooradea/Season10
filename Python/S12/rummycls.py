import pygame

class Card:
    rank = None
    suit = None
    image = None
    
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.image = pygame.image.load('./Cards/'+self.rank+'_of_'+self.suit.lower()+'.svg')
