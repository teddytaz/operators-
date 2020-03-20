#Arithmetic Operations
#Modulus operator
x = 8
y = 10
print(x % y)

#Exponential Operators
x = 7
y = 6
print(x ** y) #same as 2*2*2*2*2

# Floor Division Operators
x = 10
y = 12
print(x // y)
#the floor division // rounds the result down to the nearest whole number

#Assignment Operators
#*= Operator
x = 4
x *= 2
print(x)

#/=Operator
x = 6
x /= 2
print(x)

#%= Operator
x = 9
x%=3
print(x)

#**=Operator
x = 6
x **= 2
print(x)

#//= Operator
x = 6
x//=12
print(x)

#&= Operator
x = 18
x &=2 
print(x)

#>>= Operator
x = 15
x >>= 3
print(x)

#<<= Operator
x = 14
x <<= 7
print(x)

#=Operator
x = 21
print(x)

#Comparison Operators
#<= Opertors
x = 15
y = 5
print(x <= y)
# returns False because 5 is neither less than or equal to 3

#>= Operator
x = 25
y = 5
print(x >= y)
# returns True because five is greater, or equal, to 3

#Logical Operators
#Not Operator
x = 15
print(not(x > 6 and x < 12))
# returns False because not is used to reverse the result

#OR operator
x = 10
print(x > 6 or x < 3)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

#identity Operators 
#Not in Operator
x = ["zetech", "UoN"]
print("TUM" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

#IN operator
x = ["KU", "JKUAT"]
print("JKUAT" in x)
# returns True because a sequence with the value "banana" is in the list

#Bitwise Operators 
#AND & Operator
Sets each bit to 1 if both bits are 1

# ^	 XOR
	Sets each bit to 1 if only one of two bits is 1