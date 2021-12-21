'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list 
was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N), 
where N is the length of the list. 
You can assume that all the numbers in the list are unique.
'''
def countRotations(nums):
    n = len(nums)
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        prev = (mid-1+n)%n
        nex = (mid+1)%n
        if nums[mid]<nums[prev] and nums[mid]<=nums[nex]:
            return mid
        elif nums[mid] > nums[-1]:
            low = mid + 1
        elif nums[mid] < nums[-1]:
            high = mid - 1
    return -1

