import pygame
import random
from pygame import K_ESCAPE
import os
from rummycls import Card, Deck

# Inintialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rummy")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

# Deal cards
def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]  
    for _ in range(10):
        for i in range(num_players):
            hands[i].append(deck.draw())
    return hands

# Evaluate hand for potential strings and melds
def evaluate_hand(hand):
    strings = []
    melds = []

    # Sort hand by rank
    hand.sort(key=lambda x: RANKS.index(x.rank))

    # Check for strings
    for suit in SUITS:
        current_string = [hand[0]]
        for card in hand[1:]:
            if card.suit == suit and RANKS.index(card.rank) == RANKS.index(current_string[-1].rank) + 1:
                current_string.append(card)
            else:
                if len(current_string) >= 3:
                    strings.append(current_string)
                current_string = [card]
        if len(current_string) >= 3:
            strings.append(current_string)

    # Check for melds
    for rank in RANKS:
        current_meld = [card for card in hand if card.rank == rank]
        if len(current_meld) >= 3:
            melds.append(current_meld)

    return strings, melds

# Main function
def main():
    # Get cards image path
    card_path = os.path.join(os.getcwd(), 'Cards')
    
    # Generate and Shuffle the deck
    deck = Deck(card_path)
    
    # Deal cards
    hands = deal_cards(deck, 2)
    player_hand = hands[0]
    opponent_hand = hands[1]
    print(hands)

    # First player is human
    current_player = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                running = False

        screen.fill(GREEN)

        x_offset = 50
        y_offset = 100

        # Display player's hand
        # print(player_hand)
        for card in player_hand:
            screen.blit(card.image, (x_offset, y_offset))
            x_offset += 80

        # Display opponent's hand (face-down)
        x_offset = 50
        y_offset = 300
        back_image = pygame.image.load('./Cards/card_back.svg')
        for _ in opponent_hand:
            screen.blit(back_image, (x_offset, y_offset))
            x_offset += 80

        # Evaluate opponent's hand
        strings, melds = evaluate_hand(opponent_hand)
        # print("Opponent's hand:")
        # print("Strings:", strings)
        # print("Melds:", melds)

        # Make AI decisions
        # Assuming strings and melds are lists of potential strings and melds, respectively

        # Going for Strings
        if len(strings) > len(melds):
            # print("Opponent decides to go for strings.")
            
            # Prioritize keeping cards for strings
            for string in strings:
                for card in string:
                    # Check if card is already part of the hand
                    if card in opponent_hand:
                        # Keep the card in hand
                        pass

            # Discard unnecessary cards
            for card in opponent_hand:
                if all(card not in string for string in strings):
                    # Discard the card
                    # opponent_hand.remove(card)
                    pass

            # Pick up from deck if no strings are possible
            if not strings:
                card_from_deck = draw_card()
                opponent_hand.append(card_from_deck)

        # Going for Melds
        else:
            # print("Opponent decides to go for melds.")
            
            # Prioritize keeping cards for melds
            for meld in melds:
                for card in meld:
                    # Check if card is already part of the hand
                    if card in opponent_hand:
                        # Keep the card in hand
                        pass

            # Discard unnecessary cards
            for card in opponent_hand:
                if all(card not in meld for meld in melds):
                    # Discard the card
                    opponent_hand.remove(card)

            # Pick up from deck if no melds are possible
            if not melds:
                card_from_deck = card.draw()
                opponent_hand.append(card_from_deck)


        pygame.display.flip()

    pygame.quit()
    
main()
