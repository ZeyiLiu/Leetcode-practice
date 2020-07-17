# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

# 你可以返回任何满足上述条件的数组作为答案。

# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受


# https://leetcode-cn.com/problems/sort-array-by-parity-ii/




class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
	# divide input array into 2 arrays(even,odd)
        even_arr = []
        odd_arr = []
        input_array_length = len(A)
        for x in range(input_array_length):
            if (A[x] % 2) == 0 :
                even_arr.append(A[x])
            else:
                odd_arr.append(A[x])
        
	# merge 2 arrays and get the output
        loop_times = len(even_arr)
        output_array = []
        for x in range(0,loop_times):
            output_array.append(even_arr[x])
            output_array.append(odd_arr[x])

        return output_array
		
				
