def insertionSort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        current = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums.insert(j+1, current)
    return nums