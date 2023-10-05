import random
import time

steps = 0
num1 = 0
launchCode = int(input('Enter Launch Codes: '))

# Launch Code 1: Run once, choose number, write to file, print on screen.

def code1():
    num1 = int(input('Please enter a number: '))
    steps = 0

    file = open("code1Result.txt", "w")
    file.write("Starting on number: ")
    file.write(str(num1))
    
    while num1 != 1:
        if (num1 % 2) == 0:
            num1 = num1 / 2
            steps = steps + 1
            print('Step Number:', steps, 'Current Number:', num1)
            file.write("\nStep Number: ")
            file.write(str(steps))
            file.write(" Current Number: ")
            file.write(str(num1))
        elif (num1 % 2) != 0:
            num1 = num1 * 3
            num1 = num1 + 1
            steps = steps + 1
            print('Step Number:', steps, 'Current Number:', num1)
            file.write("\nStep Number: ")
            file.write(str(steps))
            file.write(" Current Number: ")
            file.write(str(num1))

    print('It took', steps, 'steps to get to 1.\n')
    file.write("\nIt took ")
    file.write(str(steps))
    file.write(" steps to get to 1.\n\n")
    file.close

# Launch Code 2: Run once, choose number, write to file.

def code2():
    num1 = int(input('Please enter a number: '))
    steps = 0

    file = open("code2Result.txt", "w")
    file.write("Starting on number: ")
    file.write(str(num1))
    
    while num1 != 1:
        if (num1 % 2) == 0:
            num1 = num1 / 2
            steps = steps + 1
            file.write("\nStep Number: ")
            file.write(str(steps))
            file.write(" Current Number: ")
            file.write(str(num1))
        elif (num1 % 2) != 0:
            num1 = num1 * 3
            num1 = num1 + 1
            steps = steps + 1
            file.write("\nStep Number: ")
            file.write(str(steps))
            file.write(" Current Number: ")
            file.write(str(num1))

    print('It took', steps, 'steps to get to 1.\n')
    file.write("\nIt took ")
    file.write(str(steps))
    file.write(" steps to get to 1.\n\n")
    file.close

# Launch Code 3: Run once, choose number, print on screen.

def code3():
    num1 = int(input('Please enter a number: '))
    steps = 0

    while num1 != 1:
        if (num1 % 2) == 0:
            num1 = num1 / 2
            steps = steps + 1
            print('Step Number:', steps, 'Current Number:', num1)
        elif (num1 % 2) != 0:
            num1 = num1 * 3
            num1 = num1 + 1
            steps = steps + 1
            print('Step Number:', steps, 'Current Number:', num1)

    print('It took', steps, 'steps to get to 1.\n')

# Launch Code 4: Run forever, choose number, write to file, print on screen.

def code4():
    num1 = 5
    steps = 0
    file = open("code4Result.txt", "w")

    while True:
        num1 = int(input('Please enter a number: '))
        file = open("code4Result.txt", "a")
        file.write("Starting on number: ")
        file.write(str(num1))
        
        while num1 != 1:
            if num1 == 0:
                exit
            elif (num1 % 2) == 0:
                num1 = num1 / 2
                steps = steps + 1
                print('Step Number:', steps, 'Current Number:', num1)
                file.write("\nStep Number: ")
                file.write(str(steps))
                file.write(" Current Number: ")
                file.write(str(num1))
            elif (num1 % 2) != 0:
                num1 = num1 * 3
                num1 = num1 + 1
                steps = steps + 1
                print('Step Number:', steps, 'Current Number:', num1)
                file.write("\nStep Number: ")                
                file.write(str(steps))
                file.write(" Current Number: ")
                file.write(str(num1))

        print('It took', steps, 'steps to get to 1.\n')
        file.write("\nIt took ")
        file.write(str(steps))
        file.write(" steps to get to 1.\n\n")
        file.close()
        steps = 0

# Launch Code 5: Run forever, choose number, write to file.

def code5():
    num1 = 5
    steps = 0

    file = open("code5Result.txt", "w")
    
    while True:
        num1 = int(input('Please enter a number: '))
        file = open("code5Result.txt", "a")
        file.write("Starting on number: ")
        file.write(str(num1))
    
        while num1 != 1:
            if num1 == 0:
                exit
            elif (num1 % 2) == 0:
                num1 = num1 / 2
                steps = steps + 1
                file.write("\nStep Number: ")
                file.write(str(steps))
                file.write(" Current Number: ")
                file.write(str(num1))
            elif (num1 % 2) != 0:
                num1 = num1 * 3
                num1 = num1 + 1
                steps = steps + 1
                file.write("\nStep Number: ")                
                file.write(str(steps))
                file.write(" Current Number: ")
                file.write(str(num1))

        print('It took', steps, 'steps to get to 1.\n')
        file.write("\nIt took ")
        file.write(str(steps))
        file.write(" steps to get to 1.\n\n")
        file.close()
        steps = 0

# Launch Code 6: Run forever, choose number, print on screen.

def code6():
    num1 = 5
    steps = 0

    while True:
        num1 = int(input('Please enter a number: '))
        while num1 != 1:
            if num1 == 0:
                exit
            elif (num1 % 2) == 0:
                num1 = num1 / 2
                steps = steps + 1
                print('Step Number:', steps, 'Current Number:', num1)
            elif (num1 % 2) != 0:
                num1 = num1 * 3
                num1 = num1 + 1
                steps = steps + 1
                print('Step Number:', steps, 'Current Number:', num1)

        print('It took', steps, 'steps to get to 1.\n')
        steps = 0

# Launch Code 7: Run forever, incremental numbers, write to file, print on screen.

def code7():
    num1 = 5
    steps = 0
    x = 1
    num2 = 0
    file = open("code7Result.txt", "w")

    while True:
        for i in range(50):
            x = x + 1
            num1 = x
            print('Starting on:', x)
            
            file = open("code7Result.txt", "a")
            file.write("Starting on number: ")
            file.write(str(num1))
            
            while num1 != 1:
                if (num1 % 2) == 0:
                    num1 = num1 / 2
                    steps = steps + 1
                    print('Step Number:', steps, 'Current Number:', num1)
                    file.write("\nStep Number: ")
                    file.write(str(steps))
                    file.write(" Current Number: ")
                    file.write(str(num1))
                elif (num1 % 2) != 0:
                    num1 = num1 * 3
                    num1 = num1 + 1
                    steps = steps + 1
                    print('Step Number:', steps, 'Current Number:', num1)
                    file.write("\nStep Number: ")
                    file.write(str(steps))
                    file.write(" Current Number: ")
                    file.write(str(num1))

            print('It took', steps, 'steps to get to 1.\n')
            file.write("\nIt took ")
            file.write(str(steps))
            file.write(" steps to get to 1.\n\n")
            file.close
            steps = 0
            num2 = num2 + 1
        ans = input('Would you like to continue? (Y/N) ')
        ans = str.lower(ans)
        if ans == 'y':
           print('Continuing.') 
        else:
            exit()

# Launch Code 8: Run forever, incremental numbers, write to flie.

def code8():
    num1 = 5
    steps = 0
    x = 1
    num2 = 0
    file = open("code8Result.txt", "w")

    while True:
        for i in range(50):
            x = x + 1
            num1 = x
            print('Starting on:', x)
            
            file = open("code8Result.txt", "a")
            file.write("Starting on number: ")
            file.write(str(num1))
            
            while num1 != 1:
                if (num1 % 2) == 0:
                    num1 = num1 / 2
                    steps = steps + 1
                    file.write("\nStep Number: ")
                    file.write(str(steps))
                    file.write(" Current Number: ")
                    file.write(str(num1))
                elif (num1 % 2) != 0:
                    num1 = num1 * 3
                    num1 = num1 + 1
                    steps = steps + 1
                    file.write("\nStep Number: ")
                    file.write(str(steps))
                    file.write(" Current Number: ")
                    file.write(str(num1))

            print('It took', steps, 'steps to get to 1.\n')
            file.write("\nIt took ")
            file.write(str(steps))
            file.write(" steps to get to 1.\n\n")
            file.close
            steps = 0
            num2 = num2 + 1
        ans = input('Would you like to continue? (Y/N) ')
        ans = str.lower(ans)
        if ans == 'y':
           print('Continuing.') 
        else:
            exit()

# Launch Code 9: Run forever, incremental numbers, print on screen.

def code9():
    num1 = 5
    steps = 0
    x = 1
    num2 = 0

    while True:
        for i in range(50):
            x = x + 1
            num1 = x
            print('Starting on:', x)

            while num1 != 1:
                if (num1 % 2) == 0:
                    num1 = num1 / 2
                    steps = steps + 1
                    print('Step Number:', steps, 'Current Number:', num1)
                elif (num1 % 2) != 0:
                    num1 = num1 * 3
                    num1 = num1 + 1
                    steps = steps + 1
                    print('Step Number:', steps, 'Current Number:', num1)

            print('It took', steps, 'steps to get to 1.\n')
            steps = 0
            num2 = num2 + 1
        ans = input('Would you like to continue? (Y/N) ')
        ans = str.lower(ans)
        if ans == 'y':
           print('Continuing.') 
        else:
            exit()

"""
Launch Code 1: Run once, choose number, write to file, print on screen.
Launch Code 2: Run once, choose number, write to file.
Launch Code 3: Run once, choose number, print on screen.

Launch Code 4: Run forever, choose number, write to file, print on screen.
Launch Code 5: Run forever, choose number, write to file.
Launch Code 6: Run forever, choose number, print on screen.

Launch Code 7: Run forever, incremental numbers, write to file, print on screen.
Launch Code 8: Run forever, incremental numbers, write to flie.
Launch Code 9: Run forever, incremental numbers, print on screen.

*** PRINTING TO SCREEN MAKES PROGRAM RUN SLOWER ***
*** FILE IS SAVED TO THE SAME DIRECTORY (FOLDER) AS THE PYTHON SCRIPT ***

"""

if launchCode == 1:
    code1()
elif launchCode == 2:
    code2()
elif launchCode == 3:
    code3()
elif launchCode == 4:
    code4()
elif launchCode == 5:
    code5()
elif launchCode == 6:
    code6()
elif launchCode == 7:
    code7()
elif launchCode == 8:
    code8()
elif launchCode == 9:
    code9()
else:
    print('Invalid launch code. Exiting.')
    exit()
