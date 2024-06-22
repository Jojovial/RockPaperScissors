import random

# Constants
CHOICES = ['R', 'P', 'S']
CHOICE_NAMES = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
LOSING_CHOICES = {'R': 'P', 'P': 'S', 'S': 'R'}
WINNING_CHOICES = {v: k for k, v in LOSING_CHOICES.items()}

def get_user_choice():
    while True:
        choice = input('Please choose your next move (R, P, S) (Q to Quit): ').upper()
        if choice in CHOICES or choice == 'Q':
            return choice
        print('Invalid command. Please enter R, P, S, or Q.')

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
    elif LOSING_CHOICES[user_choice] == cpu_choice:
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
