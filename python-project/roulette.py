import random 
import time
import os 
#define time to spin
TIME = 3

#define roulette 
def roulette(option):
    roulette = { '0' :(0, "green", "none") }
    change = 0
    check = 0
    color = ["red", "black"]
    choice = ["small", "big"]
    if option == 2:
        roulette.update({'00':('00', "green", "none")}) 
    
    for x in range(1, 37):
        case = {f'{x}': (x, color[change], choice[check])}
        change = 1 if change == 0 else change-1
        check = 1 if x >= 17 else check
        roulette.update(case)
    

    return roulette
    # ways to get value in key
    # if option in roulette.keys()
    # print option[0] or [1]

#detect win 
def detect_win(option, bet, roulette_choice, run):
    option_list = {'red', 'black', 'odd', 'even' , 'big', 'small' }
    spin = random.randint(0, (len(roulette_choice.keys())-1))
    if(spin > 1):
        num = list(roulette_choice.values())[spin][0]
        color = list(roulette_choice.values())[spin][1]
        check = list(roulette_choice.values())[spin][2]
    else:
        num = list(roulette_choice.values())[spin][0]
        color = list(roulette_choice.values())[spin][1]
        check = 'None'

    print(f'Result: ******** {num} | {color} | {check} ********')

    if option == list(roulette_choice.keys())[spin] and (option == '0' or option == '00'):
        print("        ******** YOU WIN ********")
        return bet * 36
    elif option in option_list:
        #check red black big small
        if option == list(roulette_choice.values())[spin][1]:
            print("        ******** YOU WIN ********")
            return bet * 2
        elif option == list(roulette_choice.values())[spin][2]:
            print("        ******** YOU WIN ********")
            return bet * 2
        #check odd even
        elif list(roulette_choice.values())[spin][0] != '00':
            if int(list(roulette_choice.values())[spin][0]) % 2 == 0:
                if option == 'even':
                    print("        ******** YOU WIN ********")
                    return bet * 2
                else:
                    print("        ******** YOU LOSE ********")
                    return -bet 
            else:
                if option == 'odd':
                    print("        ******** YOU WIN ********")
                    return bet * 2
                else:
                    print("        ******** YOU LOSE ********")
                    return - bet 
        else:
            print("        ******** YOU LOSE ********")
            return -bet 
    elif option == list(roulette_choice.keys())[spin]:
            print("        ******** YOU WIN ********")
            return bet * 36
    else:
        print("        ******** YOU LOSE ********")
        return -bet 

#count every percentage
def percentage(total, win):
    pass

#rule
def show_rule(option):
    if option.lower() == 'y':
        print("RULES: ")
        print(" ")


# time counter
def countdown():
    t = TIME
    while t:
        time.sleep(1)
        t -= 1

def auto_start():
    t = TIME
    while t >= 0:
        try:
            seconds = divmod(t, 60)
            timer = '{:d}'.format(seconds[1])
            print(f'Auto Start in {timer}, click "Ctrl+C" to stop', end="\r")
            time.sleep(1)
            t -= 1
        except KeyboardInterrupt:
            return False
    return True
# clear system
def clear():
    os.system('clear')

#main
def main():
    print("Start for the roulette\n")
    while True:
        print("Enter 1 for European Roulette(without 00)")
        print("Ender 2 for American Roulette(with 00)\n")
        run = int(input("Enter which roulette you want to play: "))
        if run != 1 and run != 2:
            clear()
            print('Invalid Option!Place choose again!')
        else:
            break

    roulette_choice = roulette(run)

    print("Roulette is set! Time to guess!! good luck! \n")

    deposit = int(input("Enter your Deposit: "))
    clear()
    while deposit > 0:
        print(f'Your deposit: {deposit}')
        if auto_start():
            try:
                bet , option = [x for x in input("\nBets by format(amount choice): ").split(" ")]
            except ValueError:
                print("Pleace input 2 value with correct format [amount option]\n")
                continue
            if int(bet) > deposit: 
                print('Not enough deposit\n')
                continue
            deposit += int(detect_win(option.lower(), int(bet), roulette_choice, run-1))
            countdown()
            clear()
        else:
            break

    print(f"\nYour final deposit is {deposit}, Thank you for playing roulette!")
main()
