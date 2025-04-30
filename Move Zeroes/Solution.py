class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        listLen = nums
        zCount = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zCount += 1
                nums.remove(nums[i])
            else:
                i += 1

        j = 0
        while j < zCount:
            nums.append(0)
            j += 1
        