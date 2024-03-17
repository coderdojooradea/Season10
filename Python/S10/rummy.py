import pygame
import random

# Inintialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rummy")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Card values
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

deck = [(rank,suit) for rank in RANKS for suit in SUITS]


# Functions
# Shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

# Draw card
def draw_card():
    if deck:
        return deck.pop()
    else:
        return None

# Deal cards
def deal_cards(num_players):
    hands = [[] for _ in range(num_players)]  
    for _ in range(10):
        for i in range(num_players):
            hands[i].append(draw_card())
    return hands

# Main function
def main()
    # Shuffle the deck
    shuffle_deck()

    # Deal cards
    hands = deal_cards(2)
    player_hand = hands[0]
    opponent_hand = hands[1]

    # First player is human
    curent_player = 0 
