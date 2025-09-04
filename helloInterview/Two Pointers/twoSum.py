''' Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False

Brute force solution: 
The naive approach to this problem uses two-pointers i and j in a nested for-loop to consider each pair in the input array, 
for a total of O(n2) pairs considered.


''' 

def isPairSum(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return True
  return False


''' Efficient solution 
Eliminating Pairs
The two-pointer technique leverages the fact that the input array is sorted.
Let's use it to solve the Two Sum problem when nums = [1, 3, 4, 6, 8, 10, 13] and target = 13. We start by initializing two pointers at opposite ends of the array, 
which represent the pair of numbers we are currently considering. This pair has a sum (14) that is greater than our target (13). And because our array is sorted, 
all other pairs ending at our right pointer (13) also have sums greater than our target, as they all involve numbers greater than 1, the value at our left pointer.
So, to move onto the next pair we move our right pointer back, which elimininates those unecessary pairs from our search.

Now, since our sum is less than our target, we know that all other pairs involving our left pointer also have sums less than our target. So, we move our left pointer 
forward to eliminate those unnecessary pairs and arrive at the next pair to consider. This continues until either our pointers meet (in which case we did not find a 
successful pair) or until we find a pair that sums to our target, like we did here.

The two-pointer technique leverages the fact that the input array is sorted to eliminate the number of pairs we consider from O(n2)down to O(n).
The two-pointers start at opposite ends of the array, and represent the pair of numbers we are currently considering.
We repeatedly compare the sum of the current pair to the target, and move a pointer in a way that eliminates unnecessary pairs from our search.
'''

def isPairSum(nums, target):
  left, right = 0 , len(nums)-1

   while left < right:
     total = nums[left]+nums[right]
     if total == target:
         return True
     elif total> target:
         right -=1
     elif total < target:
         left += 1
      
    return False
