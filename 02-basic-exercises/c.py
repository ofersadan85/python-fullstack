# print a given number with *exactly* two decimal places
# 1.23 -> 1.23
# 1.234 -> 1.23
# 2.0 -> 2.00
# 2.001 -> 2.00

# Solution: using the str.format() function / method
number = 2
print("{:.2f}".format(number))
