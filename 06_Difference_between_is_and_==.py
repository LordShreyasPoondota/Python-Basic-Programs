#Demonstrate the difference between is and == using two lists with the same values.

print("Enter numbers for list_1:", end = " ")
list_1 = list(map(int, input().split()))
print("Enter numbers for list_2:", end = " ")
list_2 = list(map(int, input().split())) 

#Comparison between == and is using two lists.
print("The two lists are equal is a", list_1 == list_2, "statement")
print("The two lists are equal is a", list_1 is list_2, "statement")

#Here == checks whether the contents of the both the variables are equal or not --- True
#Here is checks whether both variables refer to the same objects in memory --- False
    

