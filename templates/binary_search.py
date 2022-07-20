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


# Find the largest element that is not greater than target
def binary_search_1(nums, target):
    if len(nums) == 0:
        return - 1

    left = 0
    right = len(nums)

    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    # end condition left + 1 == right
    if left == 0 and nums[left] < target:
        return -1

    if right == len(nums) and nums[left] == target:
        return left

    return -1