def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
    
num = int(input("Enter number: "))
value = fact(num)
print(f"The factorial of the {num} is: {value}")