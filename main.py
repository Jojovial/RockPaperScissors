import random

# Constants
CHOICES = ['W', 'F', 'G', 'E', 'P', 'R', 'I', 'D', 'Y', 'K', 'B', 'L', 'H', 'S', 'O', 'N', 'T', 'M']
CHOICE_NAMES = {
    'W': 'Water', 'F': 'Fire', 'G': 'Grass', 'E': 'Electric', 'P': 'Psychic', 'R': 'Rock',
    'I': 'Ice', 'D': 'Dragon', 'Y': 'Fairy', 'K': 'Dark', 'B': 'Bug', 'L': 'Flying',
    'H': 'Ghost', 'S': 'Steel', 'O': 'Poison', 'N': 'Normal', 'T': 'Ground', 'M': 'Fighting'
}
LOSING_CHOICES = {
    'W': ['F', 'E', 'K', 'O', 'M'],
    'F': ['G', 'R', 'I', 'B', 'T'],
    'G': ['W', 'P', 'D', 'L', 'O'],
    'E': ['G', 'R', 'Y', 'S', 'M'],
    'P': ['F', 'W', 'I', 'H', 'K'],
    'R': ['P', 'E', 'D', 'L', 'W'],
    'I': ['W', 'K', 'F', 'O', 'T'],
    'D': ['Y', 'G', 'I', 'S', 'M'],
    'Y': ['K', 'R', 'P', 'B', 'T'],
    'K': ['E', 'Y', 'D', 'H', 'M'],
    'B': ['F', 'S', 'L', 'P', 'N'],
    'L': ['E', 'R', 'H', 'S', 'N'],
    'H': ['D', 'Y', 'K', 'O', 'N'],
    'S': ['F', 'E', 'D', 'L', 'N'],
    'O': ['P', 'H', 'S', 'G', 'M'],
    'N': ['M'],
    'T': ['W', 'L', 'G'],
    'M': ['P', 'L', 'S']
}
WINNING_CHOICES = {v: k for k, values in LOSING_CHOICES.items() for v in values}

def get_user_choice():
    while True:
        choice = input(
            'Choose your Pokémon move (W for Water, F for Fire, G for Grass, E for Electric, P for Psychic, R for Rock, I for Ice, D for Dragon, Y for Fairy, K for Dark, B for Bug, L for Flying, H for Ghost, S for Steel, O for Poison, N for Normal, T for Ground, M for Fighting) (Q to Quit): '
        ).upper()
        if choice in CHOICES or choice == 'Q':
            return choice
        print('Invalid command. Please enter a valid choice or Q to quit.')

def get_cpu_choice(history):
    if not history:
        return random.choice(CHOICES)
    else:
        # Analyze the user's most common choice and counter it with some randomness
        most_common_choice = max(set(history), key=history.count)
        counter_choice = WINNING_CHOICES[most_common_choice]
        return random.choice([counter_choice, random.choice(CHOICES)])

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

def print_type_effectiveness_chart():
    print("Type Effectiveness Chart:")
    for choice in CHOICES:
        print(f"{CHOICE_NAMES[choice]} loses to: {', '.join(CHOICE_NAMES[l] for l in LOSING_CHOICES[choice])}")

def main():
    print("Welcome to the Pokémon Battle Game!")
    print_type_effectiveness_chart()

    num_rounds = int(input("Enter the number of rounds to play (e.g., 3 for best of 3): "))
    rounds_played = 0
    wins, losses, ties = 0, 0, 0
    user_history = []

    while rounds_played < num_rounds:
        user_choice = get_user_choice()
        if user_choice == 'Q':
            break
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
            rounds_played += 1

    print("Game Over!")
    print(f'Final Stats: {wins} Wins, {losses} Losses, {ties} Ties')

if __name__ == "__main__":
    main()
