def bubbleSort(nums):
    # copy of list
    nums = list(nums)
    # repeat process n-1 times
    for i in range(len(nums) - 1):
        # iterate over array, avoiding last element
        for j in range(len(nums) - 1):
            # compare num with next num
            if nums[j] > nums[j+1]:
                # swap
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums
