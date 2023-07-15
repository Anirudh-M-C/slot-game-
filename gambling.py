import random
import pygame

MAX_LINE = 3
slot = [""] * 10

def sound_effect():
    pygame.mixer.init()
    sound_path = "C:/Users/aniru/Downloads/sound.wav"  # Replace with the actual file path
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            continue
    return amount

def get_numberoflines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINE}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a number.")
            continue
    return lines

def slot_machine():
    print(f"{slot[1]} | {slot[2]} | {slot[3]}")
    print(f"{slot[4]} | {slot[5]} | {slot[6]}")
    print(f"{slot[7]} | {slot[8]} | {slot[9]}")

def spin(lines, bet1):
    if slot[1] == slot[2] == slot[3] and lines == 1:
        winnings = bet1 * 6
        sound_effect()
        print(f"You won ${winnings}")
    elif slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] and lines == 2:
        winnings = bet1 * 6
        sound_effect()
        print(f"You won ${winnings}")
    elif slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] or slot[7] == slot[8] == slot[9] and lines == 3:
        winnings = bet1 * 6
        sound_effect()
        print(f"You won ${winnings}")
    else:
        winnings = 0
        print("You won $0")
    return winnings

def computer():
    for i in range(1, 10):
        slot[i] = random.choice(['A', 'B', 'C', 'D'])

def line(bet_amt, lines):
    if lines == 1:
        return bet_amt
    elif lines == 2:
        return bet_amt * 2
    elif lines == 3:
        return bet_amt * 3

def bet(balance, lines):
    while True:
        bet_amt = int(input("Enter the amount to bet on each line: $"))
        total_amt = line(bet_amt, lines)
        if total_amt <= balance:
            balance -= total_amt
            return bet_amt, balance
        else:
            print(f"Invalid bet amount. Minimum bet is $2 and maximum bet is {balance}.")

def update_leaderboard(player_name, score):
    leaderboard = {}

    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, value = line.strip().split(",")
                leaderboard[name] = int(value)
    except FileNotFoundError:
        pass

    leaderboard[player_name] = score

    with open("leaderboard.txt", "w") as file:
        for name, value in leaderboard.items():
            file.write(f"{name},{value}\n")
    print("Leaderboard updated.")

def display_leaderboard():
    leaderboard = {}

    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, value = line.strip().split(",")
                leaderboard[name] = int(value)

        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

        print("----- Leaderboard -----")
        for i, (name, value) in enumerate(sorted_leaderboard, start=1):
            print(f"{i}. {name}: {value}")

    except FileNotFoundError:
        print("Leaderboard is empty.")

def main():
    player_name = input("Enter your name: ")
    balance = deposit()
    consecutive_wins = 0
    bonus_round = False

    while True:
        print(f"Current balance: ${balance}")
        lines = get_numberoflines()
        bet_amt, balance = bet(balance, lines)

        input("Press enter to start spinning...")
        computer()
        slot_machine()
        balance += spin(lines, bet_amt)

        if balance < lines * 2:
            break

        if consecutive_wins >= 2:
            bonus_round = True
            print("Congratulations! You unlocked the bonus round.")

        if bonus_round:
            # Perform bonus round logic here
            print("Bonus round is in progress...")
            # Add code for the bonus round

        choice = input("Press 'q' to quit or any other key to continue: ")
        if choice.lower() == 'q':
            break

        if balance == 0:
            print("Sorry, you ran out of balance.")
            break

        if balance < lines * 2:
            break
        print(f"Final balance: ${balance}")

        if consecutive_wins >= 2:
            print("You achieved consecutive wins!")
            update_leaderboard(player_name, balance)

        display_leaderboard()
main()
pygame.quit()
