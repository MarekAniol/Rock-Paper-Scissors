from random import choice
from os import system


def valid_player_input(user_info, choose_option):
    player_input = input(user_info)
    if player_input != "x":
        if player_input not in choose_option:
            print("Input should be: 'paper', 'scissors', 'rock'.")
            return None
        else:
            user_value = player_input
    else:
        user_value = player_input
    return user_value


def compare_cpu_to_human(player_entry, player_value):
    cpu_choice = choice(list(options_dict))
    cpu_value = options_dict.get(cpu_choice)
    check_win = cpu_value - player_value
    print(f"CPU get: {cpu_choice}")
    print(f"Human get: {player_entry}")
    return check_win


def count_win(counter):
    if counter in [-1, 2]:
        count_wins["CPU"] += 1
    elif counter in [-2, 1]:
        count_wins["Human"] += 1
    else:
        print("Draw!")
    print(f"Human points: {count_wins['Human']}\nCPU points: {count_wins['CPU']}")
    return count_wins["Human"], count_wins["CPU"]


def show_winner():
    for p, num in count_wins.items():
        if num == 2:
            who_win = list(count_wins)[list(count_wins.values()).index(num)]
            print(f"Winner is: {who_win}")


def main():
    while True:
        human_entry = valid_player_input("Entry paper, scissors or rock (x to exit):", options_dict)
        if human_entry == "x":
            break
        system("clear")
        try:
            human_value = options_dict[human_entry]
        except KeyError:
            continue

        winner_counter = compare_cpu_to_human(human_entry, human_value)
        count_win(winner_counter)
        show_winner()

        if count_wins["CPU"] == 2 or count_wins["Human"] == 2:
            if input("Would you like to play again?(yes/any for exit):") == "yes":
                count_wins["CPU"] = 0
                count_wins["Human"] = 0
            else:
                break


if __name__ == "__main__"
    '''Start Game'''
    count_wins = {"Human": 0, "CPU": 0}
    options_dict = {"rock": 1, "scissors": 2, "paper": 3}
    main()
