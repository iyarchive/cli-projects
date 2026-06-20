number = 49
players = []

print("This game only ends when the player/s have guessed the right number.")

while True:
    name = input("Input player name (or 'stop' if you've inputted all players): ")

    if name == "stop":
        break
    else:
        players.append(name.capitalize())

game_over = False

while not game_over:
    try:
        for player in players:
            guess = int(input(f"{player}, guess the number: "))
        
            if guess == number:
                print("We have a winner!")
                game_over = True
                break

            elif guess > number:
                print("Guess is higher than number.")

            else:
                print("Guess is lower than number.")

    except ValueError:
        print("That is not a number. Try again.")
