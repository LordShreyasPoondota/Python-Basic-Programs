#Given a variable holding a string, print its type, length, and whether it's alphanumeric.

print("Enter a String:", end = " ")
string = input()
data_type = type(string)
length = len(string)
alphanumeric = string.isalnum()
print("Type of the variable:", data_type)
print("Length of the variable:", length)
if alphanumeric == True:
    print("The given variable is AlphaNumeric")
else:
    print("The given variable is NOT AlphaNumeric")


