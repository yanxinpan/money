# Time complexity: O(n)
# base case. Find exactly the target.
def binary_search(nums, target):
    if len(nums) == 0:
        return - 1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # end condition left > right
    return -1


# Variant 1:
def binary_search_1(nums, target):
    left = 0
    right = len(nums)

    # when there is an equal sigh in while statement, it means the search space is [0, len(nums) - 1]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    # if only left gets update with + 1, then mid won't stack.
    # if only right gets update with -1, then mid will stack, so the while statement has to be left + 1 < right


# Variant 2:
def binary_search_2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

# Variant 3:
# Count the number of elements smaller than x
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/
