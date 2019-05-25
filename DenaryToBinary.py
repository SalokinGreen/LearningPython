print("Welcome to my second program! Again a denary to binary calculator!")

while True:
    number = int(input ("Decimal:") )

    while number > 0 :
        print(str(int(number % 2)))
        number = int(number / 2)
        if number == 0 :
            break
    
