import random

if __name__ == "__main__":
    n = random.randint(1, 99)
    i = 0
    print("This is an interactive guessing game!\nYou have to ", end = '')
    print("enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!\n")
    while(1):
        print("\033[1;34mWhat's your guess between 1 and 99?\033[0;0m")
        i += 1
        choice = input()
        if choice == 'exit':
            print("Goodby!")
            exit()
        try:
            choice = int(choice)
        except:
            print("That's not a number.")
            continue
        if (choice < 1 or choice > 99):
            print("Only numbers between 1 and 99!")
        elif (choice < n):
            print("Too low!")
        elif (choice > n):
            print("Too high!")
        else:
            if n == 42:
                print("The answer to the ultimate... blablabla")
            if (i > 1):
                print("Congratulations! You've got it!\nYou won in", i, "attempts!")
            else:
                print("Contratulations! You got it on your first try!")
            exit()
