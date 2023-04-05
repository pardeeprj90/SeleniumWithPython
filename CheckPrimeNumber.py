"""Prime Number identifications
1) Natural Number >1
2) Which has only two factors 1 and itself
"""

def checkIsprime():
    factorCount = 0
    number = int(input("Please enter the number "))
    if number > 1:
        for i in range(1, number+1):
            if (number%1) == 0:
                factorCount+=1
        if factorCount==2:
            print(f'Entered {number} is a prime number')
        else:
            print(f'Entered {number} is not a prime number')
    else:
        print(f'Please enter a number greater than 0')

# checkIsprime()

# Print Factorial

def findFactorial():
    number = int(input("Please enter a number "))
    factorial = 1
    if number < 0:
        print("Enter number is less than 0 so factorial can't be calculated")
    elif number == 0:
        print(f'Factorial of entered number {number} is {factorial}')
    elif number > 0:
        for i in range (1, number+1):
            factorial *= i
        print(f'Factorial of entered number {number} is {factorial}')

# findFactorial()

# Print Factorial using recursion
def recursiveFactorial(num):
    # num = int(input("Please enter the number "))
    if num == 0 or num==1:
        return 1
    else:
        return num * recursiveFactorial(num-1)

# print(recursiveFactorial(5))

# Find max & min val in array
def findMaxMinWithLogic():
    arr = [23,54,98]
    max = arr[0]
    n =len(arr)
    for i in range (1,n):
        if arr[i]> max:
            max = arr[i]
    print(max)

    min = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    print(min)

# findMaxMinWithLogic()

# Find max & min val in array through sort
def findMaxMinWithSort():
    arr = [23, 54, 98]
    arr.sort(reverse= True)
    max =arr[0]
    min =arr[-1]
    print(f'Min value in arr is {min} & Max value in arr is {max}')

findMaxMinWithSort()