import random 
from pyfiglet import *


number = random.randint(0,100)
#a beautiful banner
banner = figlet_format("GUESS the NUMBER!")
print(banner)
print('Welcome to Guessing game!!')
print('-' * 50)
print('''Rules : I will save a no. in my 
    memory and you have to guess what that no. is by 
    the hint I will give you. Only integers''')
print('so lets get started')
a = int(input('enter your first guess:'))
if a == number:
    print("You guessed it in first guess you are lucky!!")
else:
    while(a != number):
        if a == number:
            print("You guessed it right the no. is",a)
        elif(a < number):
            print('Entered no. is very low')
        elif(a > number):
            print('You went too far come down a bit..')
        else:
            print("No input/Invalid input...try again")
        a = int(input("Enter your input:"))
print("Yes the number is ",a)

