print("Welcome to my first program! A decimal to binary calculator!")

number = int(input ("Decimal:") )
if number >0 :
    print ("1 digit: " + str(int(number % 2)))
zero = int(number / 2) 
if zero == 0:
    input()

if zero >0 :
    print("2 digit: " + str(int(zero % 2)))
one = int(zero / 2) 
if one == 0:
    input()

if one >0 :
    print("3 digit: " + str(int(one % 2)))
two = int(one / 2)
if two == 0:
    input() 

if two >0 :
    print("4 digit: " + str(int(two % 2)))
three = int(two / 2)
if three == 0:
    input() 

if three >= 0:
    print("5 digit: " +  str(int(three % 2)))
four = int(three / 2)
if four == 0:
    input() 

if four >= 0:
    print("6 digit: " +  str(int(four % 2)))
five = int(four / 2)
if five == 0:
    input() 

if five >= 0:
    print("7 digit: " +  str(int(six % 2)))
