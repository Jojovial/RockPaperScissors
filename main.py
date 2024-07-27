import random

# Constants
CHOICES = ['W', 'F', 'G', 'E', 'P', 'R', 'I', 'D', 'Y', 'K']
CHOICE_NAMES = {'W': 'Water', 'F': 'Fire', 'G': 'Grass', 'E': 'Electric', 'P': 'Psychic', 'R': 'Rock', 'I': 'Ice', 'D': 'Dragon', 'Y': 'Fairy', 'K': 'Dark'}
LOSING_CHOICES = {
    'W': ['F', 'E', 'K'],
    'F': ['G', 'R', 'I'],
    'G': ['W', 'P', 'D'],
    'E': ['G', 'R', 'Y'],
    'P': ['F', 'W', 'I'],
    'R': ['P', 'E', 'D'],
    'I': ['W', 'K', 'F'],
    'D': ['Y', 'G', 'I'],
    'Y': ['K', 'R', 'P'],
    'K': ['E', 'Y', 'D']
}
WINNING_CHOICES = {v: k for k, values in LOSING_CHOICES.items() for v in values}

def get_user_choice():
    while True:
        choice = input('Choose your Pokémon move (W for Water, F for Fire, G for Grass, E for Electric, P for Psychic, R for Rock, I for Ice, D for Dragon, Y for Fairy, K for Dark) (Q to Quit): ').upper()
        if choice in CHOICES or choice == 'Q':
            return choice
        print('Invalid command. Please enter W, F, G, E, P, R, I, D, Y, K, or Q.')

def get_cpu_choice(history):
    if not history:
        return random.choice(CHOICES)
    else:
        # Analyze the user's most common choice and counter it
        most_common_choice = max(set(history), key=history.count)
        return WINNING_CHOICES[most_common_choice]

def determine_winner(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        return 'tie'
    elif cpu_choice in LOSING_CHOICES[user_choice]:
        return 'loss'
    else:
        return 'win'

def print_result(result, user_choice, cpu_choice):
    if result == 'tie':
        print(f"It's a tie! You both chose {CHOICE_NAMES[user_choice]}.")
    elif result == 'loss':
        print(f'CPU Wins! You chose {CHOICE_NAMES[user_choice]}, the CPU chose {CHOICE_NAMES[cpu_choice]}.')
    elif result == 'win':
        print(f'You Win! You chose {CHOICE_NAMES[user_choice]}, the CPU chose {CHOICE_NAMES[cpu_choice]}.')

def print_stats(wins, losses, ties):
    print(f'Current Stats: {wins} Wins, {losses} Losses, {ties} Ties')

def main():
    done = False
    wins, losses, ties = 0, 0, 0
    user_history = []

    while not done:
        user_choice = get_user_choice()
        if user_choice == 'Q':
            done = True
        else:
            user_history.append(user_choice)
            cpu_choice = get_cpu_choice(user_history)
            result = determine_winner(user_choice, cpu_choice)
            if result == 'tie':
                ties += 1
            elif result == 'loss':
                losses += 1
            elif result == 'win':
                wins += 1
            print_result(result, user_choice, cpu_choice)
            print_stats(wins, losses, ties)

if __name__ == "__main__":
    main()
