# Exercise Name:
# 	04-List-Occurence-Counter
# Description:
# 	Display all duplicate items from a list
# Given:
# 	sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Return:
# 	[20, 60, 30]
# Hint: 
# 	Count occurence of each item in the list and print items occuring more than once.

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

lst = [ele for ele in sample_list if sample_list.count(ele) > 1]
print(list(set(lst)))