import random

# Constants
CHOICES = ['W', 'F', 'G', 'E', 'P', 'R', 'I', 'D', 'Y', 'K', 'B', 'L', 'H', 'S', 'O', 'N', 'T', 'M']
CHOICES_WITH_STELLAR = CHOICES + ['Z']
CHOICES_WITH_SHADOW = CHOICES_WITH_STELLAR + ['X']
CHOICE_NAMES = {
    'W': 'Water', 'F': 'Fire', 'G': 'Grass', 'E': 'Electric', 'P': 'Psychic', 'R': 'Rock',
    'I': 'Ice', 'D': 'Dragon', 'Y': 'Fairy', 'K': 'Dark', 'B': 'Bug', 'L': 'Flying',
    'H': 'Ghost', 'S': 'Steel', 'O': 'Poison', 'N': 'Normal', 'T': 'Ground', 'M': 'Fighting',
    'Z': 'Stellar', 'X': 'Shadow'
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
    'M': ['P', 'L', 'S'],
    'Z': [],  # Stellar type is weak to nothing
    'X': []   # Shadow type is weak to nothing and strong against everything
}
WINNING_CHOICES = {v: k for k, values in LOSING_CHOICES.items() for v in values}

def gigantamax_check():
    # 10% chance to trigger Gigantamax
    return random.random() < 0.1

def get_user_choice(win_streak, lose_streak):
    if lose_streak >= 5:
        available_choices = CHOICES_WITH_SHADOW
    elif win_streak >= 3:
        available_choices = CHOICES_WITH_STELLAR
    else:
        available_choices = CHOICES

    available_choice_str = ' / '.join([f'{c} for {CHOICE_NAMES[c]}' for c in available_choices])

    while True:
        choice = input(
            f'Choose your Pokémon move ({available_choice_str}) (Q to Quit): '
        ).upper()
        if choice in available_choices or choice == 'Q':
            return choice
        print('Invalid command. Please enter a valid choice or Q to quit.')

def get_cpu_choice(history):
    if not history:
        return random.choice(CHOICES)
    else:
        most_common_choice = max(set(history), key=history.count)
        counter_choice = WINNING_CHOICES.get(most_common_choice, random.choice(CHOICES))
        return random.choice([counter_choice, random.choice(CHOICES)])

def determine_winner(user_choice, cpu_choice, gigantamax):
    if gigantamax:
        return 'win'
    if user_choice == cpu_choice:
        return 'tie'
    elif cpu_choice in LOSING_CHOICES[user_choice]:
        return 'loss'
    else:
        return 'win'

def print_result(result, user_choice, cpu_choice, gigantamax):
    if gigantamax:
        print(f'You Gigantamaxed! You chose {CHOICE_NAMES[user_choice]}, the CPU chose {CHOICE_NAMES[cpu_choice]}. You win automatically!')
    elif result == 'tie':
        print(f"It's a tie! You both chose {CHOICE_NAMES[user_choice]}.")
    elif result == 'loss':
        print(f'CPU Wins! You chose {CHOICE_NAMES[user_choice]}, the CPU chose {CHOICE_NAMES[cpu_choice]}.')
    elif result == 'win':
        print(f'You Win! You chose {CHOICE_NAMES[user_choice]}, the CPU chose {CHOICE_NAMES[cpu_choice]}.')

def print_stats(wins, losses, ties):
    print(f'Current Stats: {wins} Wins, {losses} Losses, {ties} Ties')

def print_type_effectiveness_chart():
    print("Type Effectiveness Chart:")
    for choice in CHOICES_WITH_SHADOW:
        if LOSING_CHOICES[choice]:
            print(f"{CHOICE_NAMES[choice]} loses to: {', '.join(CHOICE_NAMES[l] for l in LOSING_CHOICES[choice])}")
        else:
            print(f"{CHOICE_NAMES[choice]} loses to: None")

def main():
    print("Welcome to the Pokémon Battle Game!")
    print_type_effectiveness_chart()

    num_rounds = int(input("Enter the number of rounds to play (e.g., 3 for best of 3): "))
    rounds_played = 0
    wins, losses, ties = 0, 0, 0
    win_streak, lose_streak = 0, 0
    user_history = []

    while rounds_played < num_rounds:
        user_choice = get_user_choice(win_streak, lose_streak)
        if user_choice == 'Q':
            break
        else:
            gigantamax = gigantamax_check()
            user_history.append(user_choice)
            cpu_choice = get_cpu_choice(user_history)
            result = determine_winner(user_choice, cpu_choice, gigantamax)
            if result == 'tie':
                ties += 1
                win_streak = 0
                lose_streak = 0
            elif result == 'loss':
                losses += 1
                win_streak = 0
                lose_streak += 1
            elif result == 'win':
                wins += 1
                win_streak += 1
                lose_streak = 0
            print_result(result, user_choice, cpu_choice, gigantamax)
            print_stats(wins, losses, ties)
            rounds_played += 1

    print("Game Over!")
    print(f'Final Stats: {wins} Wins, {losses} Losses, {ties} Ties')

if __name__ == "__main__":
    main()
