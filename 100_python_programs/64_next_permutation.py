"""
Program: Next Permutation
Description: Compute next lexicographical permutation.
"""

nums = list(map(int, input("Enter numbers separated by space: ").split()))

i = len(nums) - 2
while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1

# If no pivot found → array is in descending order
if i == -1:
    nums.reverse()
else:
    # Step 2: Find the successor
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Step 3: Swap pivot and successor
    nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the right part
    nums[i+1:] = reversed(nums[i+1:])

print("Next permutation is:", nums)
