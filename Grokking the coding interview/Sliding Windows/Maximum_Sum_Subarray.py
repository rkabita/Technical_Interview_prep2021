##### Problem Statement #######
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].





def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  result = subarray_sum(k, arr)
  max = result[0]
  for i in range(len(result)):
    if max < result[i]:
      max = result[i]
  return max



def subarray_sum(k, arr):
  result = []
  windowSum = 0.0
  windowStart = 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    if windowEnd >= k-1:
      result.append(windowSum)
      windowSum -= arr[windowStart]
      windowStart += 1
  return result

# Time complexity: O(N + K) || N = initial array size, K = result array size
# Space complexity: O(K) || To store the result array


# We can approach this problem a litle bit differently without storing all the array sum. In this way we will keep track of the Maximum Sum as we go.
# This approach will minimize the space complexity. 


def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  result = subarray_sum(k, arr)
  max = result[0]
  for i in range(len(result)):
    if max < result[i]:
      max = result[i]
  return max

