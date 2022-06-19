import random 
import time

#define roulette 
def roulette(option):
    roulette = { '0' :(0, "green", "none") }
    change = 0
    check = 0
    color = ["red", "black"]
    choice = ["small", "big"]
    if option == '1':
        roulette.update({'00':('00', "green", "none")}) 
    
    for x in range(1, 37):
        case = {f'{x}': (x, color[change], choice[check])}
        change = 1 if change == 0 else change-1
        check = 1 if x >= 17 else check
        roulette.update(case)

    return roulette

#detect win 
def detect_win(guess, option):
    option_list = { 'red', 'black', 'odd', 'even' , 'big', 'small' }
    if option in option_list:
        pass
    else:
        pass
#count every percentage
def percentage():
    pass

#rule
def show_rule(option):
    if option.lower() == 'y':
        print("RULES: ")
        print(" ")

#main 
def main():
    time_count = 20
    print("Start for the roulette\n")
    print("Ender 1 for American Roulette(with 00)")
    print("Enter 2 for European Roulette(without 00)\n ")
    option = input("Enter which roulette you want to play: ")

    roulette(option)

    print("Roulette is set! Time to guess!! good luck! \n")

    Deposit = input ("Enter your Deposit: ")

    while Deposit > 0:
        option = input("Keep playing? Type 'Y' to continue. ")

        if option.lower() != 'y':
            print("Thank you for playing !")
            quit()
        
            

main()
