import json
import random

# Possible items and enemies
items = ['torch', 'health_potion', 'sword', 'key', '']
enemies = ['bat', 'ghost', 'goblin', 'dragon', '']

# Scenario templates
# TODO 1: Add more diverse and complex scenario templates.
scenario_templates = {
    # Example scenario format:
    # 'start': {
    #     'text': 'You find yourself in a dark cave. Exits are North and South.',
    #     'options': ['Go North', 'Go South'],
    #     'outcomes': ['north_scenario', 'south_scenario'],
    #     'items': ['torch'],
    #     'health_change': 0,
    #     'enemies': ['bat']
    # },
    # Add more scenarios here.

    'cave': {
        'text': 'You find yourself in a dark cave. Exits are {} and {}.',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': items,
        'health_change': 0,
        'enemy': enemies
    },
    'tunnel': {
        'text': 'You find yourself in a dimly lit tunnel. Exits are {} and {}.',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': items,
        'health_change': -5,
        'enemy': enemies
    },
    'treasure_room': {
        'text': 'You have found the legendary treasure room! Congratulations!',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': [],
        'health_change': 0,
        'enemy': ['']
    },
    'secret_room': {
        'text': 'You discover a hidden door leading to a secret room. Exits are {} and {}.',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': items,
        'health_change': 0,
        'enemy': enemies
    },
    'chest_room': {
        'text': 'You find a treasure chest. The cave continues to {} and {}.',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': items,
        'health_change': -10,
        'enemy': enemies
    },
    'dark_tunnel': {
        'text': 'The tunnel is a dead end, but you find a healing fountain.',
        'options' : ['Go North', 'Go West'],
        'outcomes': ['north_scenario', 'west_scenario'],
        'items': ['health_potion'],
        'health_change': 0,
        'enemy': ['']
    }
}

def generate_scenario(exits):
    # TODO 2: Enhance scenario generation with more dynamic and varied logic.
    pass

scenarios = {
    # TODO 3: Create a function to generate the initial scenarios dynamically rather than hardcoding them.
    'start': {
        'text': 'You find yourself in a dark cave. Exits are North and West.',
        'options': ['North', 'West'],
        'items': items,
        'health_change': 0,
        'enemy': enemies,
        'outcomes': ['north_scenario','west_scenario']
    },
        'north_scenario': {
        'text': 'You find yourself in a northern dark cave. Exits are North and West.',
        'options': ['North', 'West'],
        'items': items,
        'health_change': 0,
        'enemy': enemies,
        'outcomes': ['north_scenario','west_scenario']
    },
        'west_scenario': {
        'text': 'You find yourself in a western dark cave. Exits are North and West.',
        'options': ['North', 'West'],
        'items': items,
        'health_change': 0,
        'enemy': enemies,
        'outcomes': ['north_scenario','west_scenario']
    }
}

player = {
    'inventory': [],
    'health': 100,
    'current_scenario': 'start',
}

def display_scenario(scenario):
    # TODO 4: Enhance user interface with ASCII art or color.
    print("\n" + scenario['text'])
    for i, option in enumerate(scenario['options'], 1):
        print(f"{i}. {option}")
    

def get_player_choice(message, options):
    # TODO 5: Implement input validation to handle non-integer inputs gracefully.
    
    while True:
        try:
            choice = int(input(message))
            if choice in range(1, len(options)+1):
                break
            else: 
                print("Invalid choice. Please choose a number between 1 and {}.".format(len(options)))
        except ValueError:
            print("Invalid input. Enter a number")
        
        except KeyboardInterrupt:
            print("\nOperation canceled by user")
            return 1 # handle none
                
    return choice

def get_user_input(prompt, valid_inputs):
    # TODO 6: Add a timeout feature to this function, so that it doesn’t wait indefinitely for user input.
    pass

def apply_outcome(choice, outcomes):
    # TODO 7: Implement a system to log player choices and outcomes for future playback or debugging.
    if choice <= len(outcomes):
        player['current_scenario'] = outcomes[choice-1]

def fight_enemy(enemy):
    # TODO 8: Enhance the battle system with more options and strategies.
    pass

def leave_enemy(enemy):
    # TODO 9: Implement consequences or rewards for choosing to leave an enemy.
    pass

def collect_item(item):
    # TODO 10: Implement item weight or size system to limit the number of items a player can carry.
    pass

def use_item():
    # TODO 11: Add more items with different use effects.
    pass

def drop_item(item):
    # TODO 12: Implement a feature where dropped items remain in the scenario and can be picked up again later.
    pass

def apply_health_change(amount):
    # TODO 13: Implement additional effects (like status effects) when health changes.
    pass

def encounter_enemy(enemy):
    # TODO 14: Implement different behaviors for different enemies.
    pass

def save_game():
    # TODO 15: Implement a feature to allow multiple save slots.
    pass

def load_game():
    # TODO 16: Complete this function to enable loading saved games.
    pass

def play_game():
    # TODO: Display the current scenario.
    while True:
        current_scenario = scenarios[player['current_scenario']]
        display_scenario(current_scenario)

        options = list(range(1,len(current_scenario['options'])+1))
        #print(options)
        choice = get_player_choice("Choose direction: ", options)
        apply_outcome(choice, current_scenario['outcomes'])

        # TODO: Get the player's choice.
        # TODO: Apply the outcome of the choice.
        # TODO: Check for enemy encounters or item usage.
        # TODO: Check if the player is still alive. If not, end the game.

def main_menu():
    while True:
        print("\n Adventure game")
        print("1. Play")
        print("2. Exit")
        choice = get_player_choice("Choose an option: ", ['1', '2'])
        if choice == 1:
            play_game()
        elif choice == 2:
            print("Thanks for playing!")
            break
        # TODO: Display the main menu.
        # TODO: Get the player's choice.
        # TODO: Start the game, load a game, or exit based on choice.
        pass

if __name__ == "__main__":
    main_menu()
