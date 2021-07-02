def twoNumberSum(array, targetSum):
    # Write your code here.
	array_size = len(array)
	
    for i in range(array_size-1):
		number = targetSum - array[i]
        firstNum = array[i]		
		for j in range(i+1, array_size):
			if array[j] == number:
				secondNum = array[j]
			    return [firstNum, secondNum]
    return [] # In case there is none 


# Time Complexity:   O(n^2)
# Space Complexity:  O(1)
