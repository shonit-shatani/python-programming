num = int(input("enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial of " + num + "is "+ fact)
