num = int(input("Enter number: "))

original = num
b = 0;

while(num != 0):
    a = num % 10
    b = b *10 + a
    num = num // 10


if b == original:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")