# Exercise Name:
# 	03-List-Manipulation
# Description:
# 	Remove items greater than 50 from a list while iterating but without creating a different copy of a list.
# Given:
# 	number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Return:
# 	[10, 20, 30, 40, 50]

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(id(number_list))

for element in number_list[:]: 
    if element > 50:
        number_list.remove(element)

print(number_list)
print(id(number_list))
