user_input = int(input("What number would you like the factorial for: "))

factorial = 1
for i in range(user_input,1,-1):
    factorial = factorial*i
print("The factorial of ",user_input,"is ",factorial)
