
# pls note that my game can accept lowercase of valid input

import random

options = ["R", "P", "S"]
Dict = {"R":"Rock", "P":"Paper", "S":"Scissors"}
play = True

while play:
    cpu_input = random.choice(options)
    user_input = input("Select from these options [R, S, P]: ")
    user_input = user_input.upper()  #to convert user input from lowercase to uppercase

    if user_input in options:
        print("User :", Dict.get(user_input), "\nComputer :", Dict.get(cpu_input))

        if cpu_input == user_input:
            print("A Tie")
            continue

        elif (cpu_input == "R" and user_input == "S") or (cpu_input == "P" and user_input == "R") or (cpu_input == "S" and user_input == "P"):
            print("COMPUTER WINS")

        elif (cpu_input == "S" and user_input == "R") or (cpu_input == "R" and user_input == "P") or (cpu_input == "P" and user_input == "S"):
            print("USER WINS")

        break
        
        # c_play = input("Do you want to continue playing [y , n]: ")

        # if c_play == "y":
        #     continue
        # else:
        #     break

    else:
        print("Please enter a valid option")
        continue