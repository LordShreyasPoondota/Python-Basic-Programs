#Check whether a given number is even or odd using the modulus operator.\

print("Enter a number:", end = "")
a = int(input())
if a % 2 == 0:
    print("The number is Even!")
else:
    print("The number is Odd!")