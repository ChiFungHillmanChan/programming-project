#check ugly numbers
ugly_list = ['2','3','5','7']
sign = ['', '+', '-']

def import_number(input_string):
    #variables
    count_ugly_number = 0
    split_input = [a for a in str(input_string)]
    checklist = []
    count_power_number = len(split_input) - 1

    # if only one digit number, directly check and return 
    if int(count_power_number) == 0:
        return check_ugly_requirement(input_string)

    # append a checklist for later calculation
    # 0 means space, 1 means plus sign, 2 means minus sign
    for i in range(count_power_number):
        checklist.append(0)

    #There are 3^(d-1) expression so loop for 3^(d-1) times
    for j in range(3 ** count_power_number):

        # create an expression list
        # expression list format : ['number', 'sign', 'number', 'sign', ....]
        expression = []
        expression.append(split_input[0])

        # add sign to expression list
        for x in range(count_power_number):
            if x == -1:
                break
            if checklist[x-1] == 0:
                expression.append(sign[0])
            elif checklist[x-1] == 1:
                expression.append(sign[1])
            elif checklist[x-1] == 2:
                expression.append(sign[2])
            expression.append(split_input[x+1])
        
        # this section is to change the checklist
        checklist[-1] = int(checklist[-1]) + 1
        for k in reversed(range(len(checklist))):
            try:
                if checklist[k] == 3:
                    checklist[k] = 0
                    checklist[k-1] = int(checklist[k-1]) + 1
            except IndexError:
                continue
        
        # as 01 is invalid. The 0 must be removed if the number is started from 0 
        for idx in range(len(expression)):
            if idx == len(expression) -1:
                break
            try:
                if expression[idx] == '0' and expression[idx+1] == '':
                    expression.pop(idx)
                elif expression[idx] == '0' and int(expression[idx+1]).isnumeric() and not int(expression[idx+1]).isnumeric():
                    expression.pop(idx)
            except ValueError:
                continue
        # join the expression list to become a string
        join_expression = ''.join(expression)
        # use eval to convert the string to an equation 
        count_ugly_number += check_ugly_requirement(eval(join_expression))

    return count_ugly_number

def check_ugly_requirement(expression):
    #check if the expression is an ugly number
    # check if it is divisable by the ugly number list
    for x in ugly_list:
        if int(expression) % int(x) == 0:
            return 1
    # if not return 0 
    return 0

def main():
    #input
    input_string = input('Ender a string:')

    #check requirement
    if not input_string.isnumeric() or len(input_string) > 13:
        print ("Invalid input string!")
        quit()

    #run the program and print the result
    print(import_number(input_string))

main()