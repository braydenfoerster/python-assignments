def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = multiply(num1, num2)
print("The product is", result)
