# Find a subarray having the given sum in an integer array
# Given an integer array, find a subarray having a given sum in it.
# For example,
# Input: nums[] = {2, 6, 0, 9, 7, 3, 1, 4, 1, 10}, target = 15
# Output: {6, 0, 9}

# Input: nums[] = {0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10}, target = 15
# Output: {1, -4, 7, 6, 1, 4} or {4, 1, 10}

# Input: nums[] = {0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10}, target = -3
# Output: {1, -4} or {-7, 1, -4, 7}

# Function to print sublist having a given sum using
# sliding window technique
def findSublist(nums, target):
    # maintains the sum of the current window
    windowSum = 0

    # maintain a window [low, high-1]
    (low, high) = (0, 0)

    # consider every sublist starting from `low` index
    for low in range(len(nums)):

        # if the current window's sum is less than the given sum,
        # then add elements to the current window from the right
        while windowSum < target and high < len(nums):
            windowSum += nums[high]
            high = high + 1

        # if the current window's sum is equal to the given sum
        if windowSum == target:
            print('Sublist found', (low, high - 1))
            return

        # At this point, the current window's sum is more than the given sum.
        # Remove the current element (leftmost element) from the window
        windowSum -= nums[low]


if __name__ == '__main__':
    # a list of positive integers
    nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
    target = 15

    findSublist(nums, target)
