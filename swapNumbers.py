# approach1
def swapNumberUsingTempVariable():
    num1= input("Please enter number1 ")
    num2 = input("Please enter number2 ")

    print(f'value of number1 is {num1} before swapping')
    print(f'value of number2 is {num2} before swapping')
    temp = num1
    num1 = num2
    num2 = temp
    print(f'value of number1 is {num1} After swapping')
    print(f'value of number2 is {num2} After swapping')
# swapNumberUsingTempVariable()

# approach 2
def swapNumberWithoutTempVariable():
    num1 = input("Please enter number1 ")
    num2 = input("Please enter number2 ")
    print(f'value of number1 is {num1} before swapping')
    print(f'value of number2 is {num2} before swapping')
    num1, num2 = num2, num1
    print(f'value of number1 is {num1} After swapping')
    print(f'value of number2 is {num2} After swapping')

# swapNumberWithoutTempVariable()

# Program to reverse a string

gfg = "geeksforgeeks"
print(gfg[::-1])
print("".join(reversed(gfg)))
