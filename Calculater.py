# I'm following a tutorial, this is not my programming however I'll be adding comments to show that I understand the code
# Check the end of this to find some music I think is pretty neat :)

# Defining this chunk of code as a function

def calculate():

# Prompting user for input


    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    Operation = input('''
    Type the operation that you wish to use
    + for addition
    - for subtraction
    * for multiplaction
    / for division 
    ''')

# Operations using else if conditinals

# Addition
    if Operation == '+':
        print('{} + {} = ' .format(number_1, number_2))
        print(number_1 + number_2)

# Subtraction
    elif Operation == '-':
        print('{} - {} = ' .format(number_1, number_2))
        print(number_1 - number_2)

# Multiplaction
    elif Operation == '*':
        print('{} * {} = ' .format(number_1, number_2))
        print(number_1 * number_2)

# Division
    elif Operation == '/':
        print('{} / {} = ' .format(number_1, number_2))
        print(number_1 / number_2)

# Invalid operation or shit code
    else:
        print('Either I\'ve fucked up my code or the operation is invalid')
        

# Defining a new chunk of code to give the user the option the calculate again if they wish

def again():

# Prompting user for input
    
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for yes and N for no.''')

# User types either Y or y
    
    if calc_again.upper() == 'Y':
        calculate()

# User types either N or n

    elif calc_again.upper() == 'N':
        print('aight, fuck off then')

# User has a stroke

    else:
        print('invalid')
        again()

# Calling Calcuator

calculate()

# Calling Again

again()

# Muisc listened to while working on this:
# Glass animal's album, Zaba (Deluxe)
# Left at London's album, Transgender Street Legend, Vol.1
# Left at London's album, Transgender Street Legend, Vol.2
