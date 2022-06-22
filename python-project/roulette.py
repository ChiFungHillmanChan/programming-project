import random 
import time
import os 
#define time to spin
TIME = 3

#define roulette 
def roulette(option):
    roulette = { '0' :(0, "green", "none") }
    change = 0
    size_check = 0
    color = ["red", "black"]
    size = ["small", "big"]
    if option == 2:
        roulette.update({'00':('00', "green", "none")}) 
    
    for x in range(1, 37):
        case = {f'{x}': (x, color[change], size[size_check])}
        change = 1 if change == 0 else change-1
        size_check = 1 if x >= 17 else size_check
        roulette.update(case)

    return roulette
    # ways to get value in key
    # if option in roulette.keys()
    # print option[0] or [1]

#count every percentage
def percentage(total, set, color, odd_even, size, result):
    option_list = {'red', 'black', 'odd', 'even' , 'big', 'small' }
    if set == 'set_percentage':
        for item in option_list:
            case = {f'{item}': 0}
            result.update(case)
        return result
    elif set == 'check_result':
        print("Now Percentage:\n")
        print("-------------------------------------------")
        print(f" |   Red: {result.get('red'):.2f}%    |    Black: {result.get('black'):.2f}%   |")
        print(f" |   Odd: {result.get('odd'):.2f}%    |    Even : {result.get('even'):.2f}%   |")
        print(f" |   Big: {result.get('big'):.2f}%    |    Small: {result.get('small'):.2f}%   |")
        print("-------------------------------------------")
    else:
        if color == 'red':
            percentage_for_each = (int(result['red'])+100)/(total)
            result['red'] = percentage_for_each
            result['black'] = 100 - percentage_for_each
        elif color == 'black':
            percentage_for_each = (int(result['black'])+100)/(total)
            result['black'] = percentage_for_each
            result['red'] = 100 - percentage_for_each

        if odd_even == 'odd':
            percentage_for_each = (int(result['odd'])+100)/(total)
            result['odd'] = percentage_for_each
            result['even'] = 100 -percentage_for_each
        elif odd_even == 'even':
            percentage_for_each = (int(result['even'])+100)/(total)
            result['even'] = percentage_for_each
            result['odd'] = 100 - percentage_for_each

        if size == 'big':
            percentage_for_each = (int(result['big'])+100)/(total)
            result['big'] = percentage_for_each
            result['small'] = 100 -percentage_for_each
        elif size == 'small':
            percentage_for_each = (int(result['small'])+100)/(total)
            result['small'] = percentage_for_each
            result['big'] = 100 -percentage_for_each

        print("Now Percentage:\n")
        print("-------------------------------------------")
        print(f" |   Red: {result.get('red'):.2f}%    |    Black: {result.get('black'):.2f}%   |")
        print(f" |   Odd: {result.get('odd'):.2f}%    |    Even : {result.get('even'):.2f}%   |")
        print(f" |   Big: {result.get('big'):.2f}%    |    Small: {result.get('small'):.2f}%   |")
        print("-------------------------------------------")
        return result

#detect win 
def detect_win(option, bet, roulette_choice, total, result):
    option_list = {'red', 'black', 'odd', 'even' , 'big', 'small' }
    spin = random.randint(0, (len(roulette_choice.keys())-1))
    if int(list(roulette_choice.values())[spin][0]) % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'

    if(spin > 1):
        num = list(roulette_choice.values())[spin][0]
        color = list(roulette_choice.values())[spin][1]
        size = list(roulette_choice.values())[spin][2]
    else:
        num = list(roulette_choice.values())[spin][0]
        color = list(roulette_choice.values())[spin][1]
        size = 'None'

    result = percentage(total, 'none', color, odd_even, size, result)
    print(f'Result: ******** {num} | {color} | {size} ********')

    if option == list(roulette_choice.keys())[spin] and (option == '0' or option == '00'):
        print("        ******** YOU WIN ********")
        return bet * 36 - bet
    elif option in option_list:
        #check red black big small
        if option == list(roulette_choice.values())[spin][1]:
            print("        ******** YOU WIN ********")
            return bet * 2 - bet
        elif option == list(roulette_choice.values())[spin][2]:
            print("        ******** YOU WIN ********")
            return bet * 2 - bet
        #check odd even
        elif list(roulette_choice.values())[spin][0] != '00':
            if option == odd_even:
                print("        ******** YOU WIN ********")
                return bet * 2 - bet
            else:
                print("        ******** YOU LOSE ********")
                return -bet
        else:
            print("        ******** YOU LOSE ********")
            return -bet 
    elif option == list(roulette_choice.keys())[spin]:
            print("        ******** YOU WIN ********")
            return bet * 36 - bet
    else:
        print("        ******** YOU LOSE ********")
        return -bet 
    

#rule
def show_rule(option):
    if option.lower() == 'y':
        print("RULES: ")
        print(" ")

# time counter
def countdown():
    t = TIME
    while t:
        seconds = divmod(t, 60)
        timer = '{:d}'.format(seconds[1])
        print(f'Result in {timer} .....', end="\r")
        time.sleep(1)
        t -= 1

# auto start spin
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
    result = {}
    print("Start for the roulette\n")
    try:
        while True:
            print("Enter 1 for European Roulette(without 00)")
            # print("Ender 2 for American Roulette(with 00)\n")
            run = int(input("Enter which roulette you want to play: "))
            if run != 1 and run != 2:
                clear()
                print('Invalid Option!Place choose again!')
            else:
                break

        roulette_choice = roulette(run)
        clear()
        print("Roulette is set! Time to guess!! good luck! \n")
        result = percentage(0,'set_percentage', -1, -1, -1, result)
        deposit = int(input("Enter your Deposit: "))

        total = 1
        while deposit > 0:
            print(f'Your deposit: {deposit}')
            if auto_start():
                if input('\nCheck?:') == 'check':
                    percentage((total-1),'check_result', -1, -1, -1, result)
                    continue
                try:
                    bet , option = [x for x in input("\nBets by format(amount choice): ").split(" ")]
                except ValueError:
                    print("Pleace input 2 value with correct format [amount option]\n")
                    continue
                if int(bet) > deposit: 
                    print('Not enough deposit\n')
                    continue
                countdown()
                deposit += int(detect_win(option.lower(), int(bet), roulette_choice, total, result))
                total += 1
            else:
                break

        print(f"\nYour final deposit is {deposit}, Thank you for playing roulette!")
    except ValueError:
        print("Error occurs! Please re-run the program. Thank you!")
    except KeyboardInterrupt:
        print("\nYou have ended the program. Thank you for joining !")
main()
