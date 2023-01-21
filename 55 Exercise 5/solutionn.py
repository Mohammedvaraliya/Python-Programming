# Snake Water Gun
import random

def snake_water_gun():
    print("Lets play this awesome game named 'Snake Water Gun'")
    try:
        computer_input = random.randint(1, 3)
        user_input = int(input("\n 1. Snake \n 2. Water \n 3. Gun \n Enter your input : "))

        name_list = ["Snake", "Water", "Gun"]

        print(f"Computer input is {computer_input}, means compueter selected {name_list[computer_input - 1]}")
        print(f"Your input is {user_input}, means you selected {name_list[user_input - 1]}")

        if(user_input == 1 and computer_input == 1):
            print("Match draw")
        elif(user_input == 2 and computer_input == 2):
            print("Match draw")
        elif(user_input == 3 and computer_input == 3):
            print("Match draw")
        elif(user_input == 1 and computer_input == 2):
            print("You Won")
        elif(user_input == 1 and computer_input == 3):
            print("You Lose")
        elif(user_input == 2 and computer_input == 1):
            print("You Lose")
        elif(user_input == 2 and computer_input == 3):
            print("You Won")
        elif(user_input == 3 and computer_input == 1):
            print("You Won")
        elif(user_input == 3 and computer_input == 2):
            print("You Lose")
        else:
            print("Invalid Input, try again")
    except Exception as e:
        print(e)




if __name__ == "__main__":

    snake_water_gun()