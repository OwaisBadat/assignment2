number = int(input("What number would you like to check: "))


if number > 1:
    for i in range(2, number):
        if(number % i == 0):
            print("This number is not a prime number")
            break
    else:
        print("This number is a prime number")
