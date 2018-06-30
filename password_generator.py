# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: Final Exam Practical problem #1

#PseudoCode
#Import Random
# An input for the user to tell me how many characters
#A place holder for the password (empty list)
#a sequence of all capital letters
#A sequence of all lower case letters
#A definite loop running the number of times the user inputs
# A random 1 or 2 to determine capital or lower case
#If capital use a sequence of the alphabet in caps 
##use random to select a number 1-26 that correlates with a letter. add this to my password
#If lower case do the same as capital, but with lower letters.
# append wach character to the list for password
#convert the list to a string
#output the final password

#The actual code
from random import *
passwordLength=int(input("Please enter the length of Password you'd like to create: "))
caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password = []
for character in range(passwordLength):
    lowerUpper = randrange(1,3)#capital letters = 1, lowercase = 2
    if lowerUpper == 1:
        character = caps[randrange(0,26)]
        password.append(character)
    else:
        character = lower[randrange(0,26)]
        password.append(character)
        
passwordstr=''.join(password)
print("Your password is : {0}".format(passwordstr))