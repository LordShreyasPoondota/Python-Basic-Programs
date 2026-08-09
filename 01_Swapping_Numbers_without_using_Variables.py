#Swap the values of two variables without using a third variable.

print("Enter two numbers to be swapped:", end =" ")
a, b = map(int, input().split())
a = a + b
b = a - b
a = a - b
print("Swapped numbers are:", a, b, end = " ")