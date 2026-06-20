def game_intro():

    print("Welcome to this Tiger Pet Simulation Game!"
        "\nYour job is to keep the tiger alive, healthy, and happy.")

    while True:

        start = input("Should we get started? Type 'yes' or 'no: ").strip().lower()

        if start == "yes":
            break
        if start == "no":
            quit()
        else:
            print("Type 'yes' or 'no'.")

def menu(stats):

    menu_options = ["Play", "Feed", "Sleep", "Check Stats", "Quit"]

    print("What do you want to do with your pet tiger?")

    for i, option in enumerate(menu_options, 1):
        print(f"{i}. {option}")

    while True:
        
        try:
            user_menu_choice = int(input("Enter the number of your choice: ").strip())
        
            if 0 < user_menu_choice <= len(menu_options):
                break

            else:
                print("Please type a number within the options.")

        except ValueError:
            print("That is not a number. Please try again.")

    if user_menu_choice == 1:
        play_with_tiger(stats)

    elif user_menu_choice == 2:
        feed_tiger(stats)

    elif user_menu_choice == 3:
        make_tiger_sleep(stats)

    elif user_menu_choice == 4:
        check_tiger_stats(stats)

    else:
        quit()

def main():

    stats = {
        "fullness": 50,
        "energy": 80,
        "happiness": 70
    }

    game_intro()

    menu(stats)

def play_with_tiger(stats):

    play_options = [
            ("Throw Ball", 10, -5, 5),
            ("Tug of War", 15, -10, 10),
            ("Chase Game", 20, -15, 15),
            ("Swimming", 15, -10, 5),
            ("Hide and Seek", 10, -5, 5)
        ]

    while True:  

        print("How do you wanna play with tiger?")

        for i, (game, _, _, _) in enumerate(play_options, 1):
            print(f"{i}. {game}")

        while True:
            
            try:
                user_game_choice = int(input("Enter the number of your choice: ").strip())
            
                if 0 < user_game_choice <= len(play_options):
                    break

                else:
                    print("Please type a number within the options.")

            except ValueError:
                print("That is not a number. Please try again.")

        chosen_game, fullness_gain, energy_gain, happiness_gain = play_options[user_game_choice - 1]

        print(f"You've fed the tiger {chosen_game}."
            f"\nIts fullness gains {fullness_gain} pts."
            f"\nIts energy loses {energy_gain} pts."
            f"\nIts happiness gains {happiness_gain} pts.")
        
        stats["fullness"] += fullness_gain
        stats["energy"] += energy_gain
        stats["happiness"] += happiness_gain

        while True:

            user_navigation = input("Do you want to go back to menu? Type 'yes' or 'no': ").strip().lower()

            if user_navigation != "yes" and user_navigation != "no":
                print("Type 'yes' or 'no'.")
            else:
                break

        if user_navigation == "yes":
            break
        else:
            continue

    menu(stats)

def make_tiger_sleep(stats):

    sleep = (70, 30)

    energy_gain, happiness_gain = sleep

    while True:

        if stats["energy"] <= 20:

            print("Your tiger is very tired. They need to sleep.")

            while True:
                user_sleep_choice = input("Make tiger go to sleep? Type 'yes' or 'no': ").strip().lower()

                if user_sleep_choice == "no":
                    menu(stats)
                    break
                
                elif user_sleep_choice == "yes":

                    print("Your tiger had a good night's sleep."
                        f"Its energy gains {energy_gain} pts."
                        f"Its happiness gains {happiness_gain} pts.")

                    stats["energy"] += energy_gain

                    stats["happiness"] += happiness_gain

                    break

                else:
                    print("Please type 'yes' or 'no' only.")

        elif stats["energy"] <= 40:
            print("Your tiger is tired. They may want to sleep.")

            while True:
                user_sleep_choice = input("Make tiger go to sleep? Type 'yes' or 'no': ").strip().lower()

                if user_sleep_choice == "no":
                    menu(stats)
                    break
                
                elif user_sleep_choice == "yes":

                    print("Your tiger had a good night's sleep."
                        f"Its energy gains {energy_gain} pts."
                        f"Its happiness gains {happiness_gain} pts.")

                    stats["energy"] += energy_gain

                    stats["happiness"] += happiness_gain

                    break

                else:
                    print("Please type 'yes' or 'no' only.")
        
        else:
            print("Your tiger still has a lot of energy. They do not want to sleep.")

        while True:

            user_navigation = input("Do you want to go back to menu? Type 'yes' or 'no': ").strip().lower()

            if user_navigation != "yes" and user_navigation != "no":
                print("Type 'yes' or 'no'.")
            else:
                break

        if user_navigation == "yes":
            break
        else:
            continue

    menu(stats)

def feed_tiger(stats):

    foods = [
        ("Chicken", 15, 10, 5),
        ("Beef", 10, 10, 10),
        ("Fish", 20, 15, 5),
        ("Deer", 30, 20, 15),
        ("Boar", 35, 25, 10),
        ("Rabbit", 10, 10, 20),
        ("Duck", 10, 10, 15)
    ]

    while True:

        print("What kind of food do you want to feed the tiger?")

        for i, (food, _, _, _) in enumerate(foods, 1):
            print(f"{i}. {food}")

        while True:
            
            try:
                user_food_choice = int(input("Enter the number of your choice: ").strip())
            
                if 0 < user_food_choice <= len(foods):
                    break

                else:
                    print("Please type a number within the options.")

            except ValueError:
                print("That is not a number. Please try again.")

        chosen_food, fullness_gain, energy_gain, happiness_gain = foods[user_food_choice - 1]

        print(f"You've fed the tiger {chosen_food}."
            f"\nIts fullness gains {fullness_gain} pts."
            f"\nIts energy gains {energy_gain} pts."
            f"\nIts happiness gains {happiness_gain} pts.")
        
        stats["fullness"] += fullness_gain
        stats["energy"] += energy_gain
        stats["happiness"] += happiness_gain

        while True:

            user_navigation = input("Do you want to go back to menu? Type 'yes' or 'no': ").strip().lower()

            if user_navigation != "yes" and user_navigation != "no":
                print("Type 'yes' or 'no'.")
            else:
                break

        if user_navigation == "yes":
            break
        else:
            continue

    menu(stats)

def check_tiger_stats(stats):

    print(f"Fullness: {stats['fullness']}")
    print(f"Energy: {stats['energy']}")
    print(f"Happiness: {stats['happiness']}")

    while True:

        user_navigation = input("Do you want to go back to menu? Type 'yes' or 'no': ").strip().lower()

        if user_navigation == "yes":
            break
        elif user_navigation == "no":
            continue
        else:
            print("Type 'yes' or 'no'.")

    menu(stats)


main()
