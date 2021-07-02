###################     Algo Expert  ########################


def isValidSubsequence(array, sequence):
    arr_idx = 0
	seq_idx = 0
	while arr_idx < len(array) and seq_idx < len(sequence):
		if array[arr_idx] == sequence[seq_idx]:
			seq_idx += 1
		arr_idx += 1
	return seq_idx == len(sequence)


# Time Complexity: O(n) || n is the length of the main array.
# Space Complexity: O(1)
