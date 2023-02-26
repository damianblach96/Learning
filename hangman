import random

print("H A N G M A N")
win_count = 0
lose_count = 0
list_of_answers = ['python', 'java', 'swift', 'javascript']
def play_game():
    attempts = 0
    answer = random.choice(list_of_answers)
    result = "-" * (len(answer))
    saved_letter = []
    while attempts < 8:
        print(result)
        if result == answer:
            print(f"You guessed the word {result}!\nYou survived!")
            global win_count
            win_count += 1
            break
        all_indexes = []
        letter = input("Input a letter:")
        if len(letter) > 1 or letter == "":
            print("Please, input a single letter.")
        elif letter.islower() == False:
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in result or letter in saved_letter:
            print("You've already guessed this letter.")
        elif letter not in answer:
            print(f"That letter doesn't appear in the word.\n")
            saved_letter += letter
            attempts += 1
        else:
            for i in range(0, len(answer)):
                if answer[i] == letter: 
                    all_indexes.append(i)
              
            for j in range(0, len(all_indexes)):
                result = result[:all_indexes[j]] + letter + result[all_indexes[j]+1:]
    if attempts >= 8:
        global lose_count
        lose_count = lose_count + 1
        print("\nYou lost!")

def show_results():

    print(f"You won: {win_count} times.")
    print(f"You lost: {lose_count} times.")


while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:\n')
    if choice == "play":
        play_game()
    elif choice == "results":
        show_results()
    elif choice == "exit":
        exit()




