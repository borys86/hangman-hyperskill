import random
import string

words = ["python", "java", "swift", "javascript"]

all_inputs = set()
count_wins = 0
count_loses = 0
print("H A N G M A N")


def is_valid_input(input_letter):
    if len(input_letter) != 1:
        print("Please, input a single letter.")
        return False
    elif input_letter not in string.ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    elif input_letter in all_inputs:
        print("You've already guessed this letter.")
        return False
    else:
        all_inputs.add(input_letter)
        return True


def play_game():
    global count_loses
    global count_wins
    attempts = 8
    selected_word = random.choice(words)
    masked_word = list(len(selected_word) * "-")

    print("")
    print(''.join(masked_word))
    while attempts > 0:
        input_letter = input("Input a letter: ")
        if not is_valid_input(input_letter):
            pass
        elif input_letter not in selected_word:
            print("That letter doesn't appear in the word.")
            attempts -= 1
        elif input_letter in masked_word:
            print("No improvements.")
            attempts -= 1
        else:
            for i, letter in enumerate(selected_word):
                if letter == input_letter:
                    masked_word[i] = input_letter
        print(''.join(masked_word))
        if "-" not in masked_word:
            print(f"You guessed the word {''.join(masked_word)}!")
            print("You survived!")
            attempts = 0
            count_wins += 1
    if "-" in masked_word:
        print("")
        print("You lost!")
        count_loses += 1
    all_inputs.clear()


def show_results():
    print(f"You won: {count_wins} times.")
    print(f"You lost: {count_loses} times.")


continue_playing = True
while continue_playing:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if command == "play":
        play_game()
    elif command == "results":
        show_results()
    elif command == "exit":
        continue_playing = False
