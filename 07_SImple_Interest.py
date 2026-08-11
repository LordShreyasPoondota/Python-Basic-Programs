print("Enter Principal Amount:", end = " ")
principal = int(input())
print("Enter rate of interest:", end = " ")
rate = int(input())
print("Enter loan period in terms of years:", end = " ")
time = int(input())

SI = (principal * rate * time) / 100
print("Simple Interest for the given loan is:", SI)