# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

# 你可以返回任何满足上述条件的数组作为答案。

# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受


# https://leetcode-cn.com/problems/sort-array-by-parity-ii/




# This function divides input array into 2 arrays(odd and even)
def divide_array(input_array):
	even_arr = []
	odd_arr = []
	input_array_length = len(input_array)
	for x in range(input_array_length):
		if (input_array[x] % 2) == 0 :
			even_arr.append(input_array[x])
		else:
			odd_arr.append(input_array[x])
	merge_arrays(even_arr, odd_arr)



# This function merge 2 arrays.
def merge_arrays(even_arr, odd_arr):
	loop_times = len(even_arr)
	output_array = []
	for x in range(0,loop_times):
		output_array.append(even_arr[x])
		output_array.append(odd_arr[x])

	print(output_array)
	return



# test case : 
testB = [13,52,4,15,12,24,96,1,7,17,9,100]
print(divide_array(testB))
print("==========================")

# output result: [52, 13, 4, 15, 12, 1, 24, 7, 96, 17, 100, 9]
		
				