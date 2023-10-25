def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input = int(input("Number please: "))

if user_input:
    number = user_input

    if number < 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        result = factorial(number)
        print("Factorial of " + str(number) + " is: " + str(result))

else:
    print("Invalid input. Please enter a valid number.")