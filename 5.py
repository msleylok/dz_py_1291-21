nums_in_list = [1, 27, 12, 64, 6, 7]
nums_in_tuple = {6, 12, 3, 4, 17, 1}
sym_diff = nums_in_tuple.symmetric_difference(nums_in_list)
diff = nums_in_tuple.difference(nums_in_list)
result = sym_diff.difference(diff)
print(result)
