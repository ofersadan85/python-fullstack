number = 952  # Assume this is the input number, change it to other values to test your code

# Exercise 1: Given a 3 digit number, print the digit in the first position (from the left - the hundreds digit).

# Solution 1:
hundreds = number / 100  # hundreds = 3.47
hundreds = int(hundreds)  # hundreds = 3
print(hundreds)

# Solution 2 - Using the number as a string
str_number = str(number)
print(str_number[0])

# Solution 3 - Modulo
remainder = number % 100  # remainder = 47
hundreds = number - remainder  # hundreds = 300
hundreds = hundreds / 100  # hundreds = 3.0
hundreds = int(hundreds)  # hundreds = 3
print(hundreds)


# Exercise 2: Given a 3 digit number, print the digit in the second position (from the left - the tens digit).

# Solution 1
hundreds = number / 100  # hundreds = 3.47
hundreds = int(hundreds)  # hundreds = 3
hundreds = hundreds * 10  # hundreds = 30
new_number = number / 10  # new_number = 34.7
new_number = int(new_number)  # new_number = 34
print(new_number - hundreds)  # 34 - 30 = 4

# Solution 2 - same as solution 1 but in one line
print(int(number / 10) - int(number / 100) * 10)

# Solution 3 - Using the number as a string
str_number = str(number)
print(str_number[1])

# Solution 4 - Modulo
remainder = number % 100  # remainder = 47
ones = remainder % 10  # ones = 7
tens = remainder - ones  # tens = 40
tens = tens / 10  # tens = 4.0
tens = int(tens)  # tens = 4
print(tens)
