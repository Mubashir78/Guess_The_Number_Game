# Programmed by: Mubashir Ahmed OR known as Mubashir78 on GitHub
# https://www.github.com/Mubashir78

from random import randint
from sys import stdout
from time import sleep

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

error_code = color.BOLD+color.RED+"Invalid input. Please try again."+color.END
max_num = 10

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.025)
    print(" ")

def startup():
    print_slow(color.BOLD+"=======================\n Guess The Number Game \n======================="+color.END)
    sleep(1)
    return intro()

def intro():
    print_slow(color.BOLD+f"\nIn this game, you have to guess a number from 1 to 10!"+color.END)
    sleep(1.3)
    return main(max_num)

def set_max_num(max_num):
    print_slow(color.ITALIC+"==========\n Settings \n=========="+color.END)
    sleep(0.5)

    print_slow(color.BOLD+"\nHere you can set the max number to guess upto.")
    sleep(0.8)

    print_slow("The default is 10.")
    sleep(0.6)

    while True:
        max_num = input(color.BOLD+color.CYAN+"\nSet the max number to: "+color.END)
        try:
            max_num = int(max_num)
            print_slow(color.BOLD+color.GREEN+f"Max number changed to {max_num} successfully."+color.END)
            sleep(0.8)

            print_slow(color.ITALIC+"Starting the game with new settings... "+color.END)
            sleep(0.6)

            print_slow(color.BOLD+f"\nNow you have to guess a number from 1 to {max_num}!"+color.END)
            sleep(1)

            return max_num

        except ValueError:
             print_slow("%s" % error_code)
             sleep(0.5)

def exit_code():
    print_slow(color.BOLD+"\nThe script will now exit.")
    sleep(0.5)

    print_slow("Thanks for playing!"+color.END)
    sleep(0.8)

    return
                                    
def main(max_num):
    ran_num = randint(1,max_num)

    while True:
        num = input(color.BOLD+color.CYAN+"\nEnter the number: "+color.END).lower()
        
        if num == "show" or num == "reveal":
            print_slow(color.BOLD+f"The number was {ran_num}."+color.END)
            sleep(0.6)

            return retry_code()
            
        elif num =="set":
            max_num = set_max_num(max_num)

            return main(max_num)
            
        elif num == "exit" or num == "quit":
            return exit_code()
            
        else:
             try:
                num = int(num)

             except ValueError:
                print_slow("%s" % error_code)
                sleep(1)
                continue
      
             if num == ran_num:
                print_slow(color.BOLD+color.GREEN+f"You guessed correct! It was {ran_num}!"+color.END)
                sleep(1.3)

                return retry_code()
            
             elif num < 1:
                print_slow(color.BOLD+color.RED+f"That's too low!\nPlease make sure to enter from 1 to {max_num}."+color.END)
                sleep(1.8)
            
             elif num > max_num:
                print_slow(color.BOLD+color.RED+f"That's too high!\nPlease make sure to enter from 1 to {max_num}."+color.END)
                sleep(1.8)
        
             elif num > ran_num:
                print_slow("Guess lower!")
                sleep(1)
            
             elif num < ran_num:
                print_slow("Guess higher!")
                sleep(1)   

def retry_code():
    choice = input(color.BOLD+color.BLUE+"\nDo you wish to play again?(y/n): "+color.END).lower()
    
    if choice == "y":
        print_slow(color.ITALIC+"Restarting..."+color.END)
        sleep(1)

        return main(max_num) 
        
    elif choice == "n":
        return exit_code()
        
    else:
        print_slow("%s" % error_code)
        sleep(1.3)

        return retry_code()

startup()

# Programmed by: Mubashir Ahmed OR known as Mubashir78 on GitHub
# https://www.github.com/Mubashir78
