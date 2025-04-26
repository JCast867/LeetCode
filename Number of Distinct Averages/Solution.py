class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = {}  # keep track of the averages
        while len(nums) != 0:  # while the list is not empty
            minimum = min(nums)
            maximum = max(nums)
            avg = (minimum + maximum)

            if avg not in averages:
                averages[avg] = 1
            
            nums.remove(minimum)
            nums.remove(maximum)

        return len(averages)