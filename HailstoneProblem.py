from os import close
import random

def checkAndWrite(line):
    if storingFile == 'y':
        file = open(fileName, 'at')
        file.write("\n" + line)
        file.close()

baseNum = int(input('Enter any integer or leave blank for a random number between 2 & 10 Million: '))
if baseNum == "":
    baseNum = random.randint(2,10000000)
    print("Your number will be: " + str(baseNum))
workNum = baseNum

counter = 0
fileName = 'Hailstone ' + str(baseNum) + '.txt'

storingFile = input('Would you like to store the output to a text file? (y/n) ')

while workNum > 1:
    if workNum % 2 == 0:
        print('Even Number, Dividing '+ str(workNum) + ' by 2.')
        checkAndWrite('Even Number, Dividing ' + str(workNum) + ' by 2.')
        workNum = workNum / 2
        print("Result is " + str(workNum))
        checkAndWrite("Result is " + str(workNum))

    else:
        print('Odd number, Multiplying ' + str(workNum) + ' by 3 and adding 1.')
        checkAndWrite('Odd number, Multiplying ' + str(workNum) + ' by 3 and adding 1.')
        workNum = workNum * 3
        workNum += 1
        print('Result is ' + str(workNum))
        checkAndWrite('Result is ' + str(workNum))

    counter += 1
    print('Not solved, going again.')
    checkAndWrite('Not solved, going again.')

print('Your base Number was: ' + str(baseNum))
checkAndWrite('Your base Number was: ' + str(baseNum))
print('It resulted in: ' + str(workNum))
checkAndWrite('It resulted in: ' + str(workNum))
print('It took ' + str(counter) + ' steps to reach 1')
checkAndWrite('It took ' + str(counter) + ' steps to reach 1')