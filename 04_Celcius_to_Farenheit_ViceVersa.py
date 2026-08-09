#Convert a temperature from Celsius to Fahrenheit and vice versa.

print("Enter temperature:", end = " ")
temp = int(input())
print("Enter Scale of Temperature Celsius(C) or Farenheit(F):", end = " ")
scale = input()
if scale == 'C':
    Farenheit = ((9 * temp) / 5) + 32
    print("Temperature in Farenheit is:", Farenheit)
elif scale == 'F':
    Celsius = (5 * (temp - 32)) / 9
    print("Temperature in Celcius is:", Celsius)
else:
    print("Incorrect Option, Please enter an appropriate scale!!!")