class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for x in dic.items():
            if x[1] == 1:
                ans = x[0]
        return ans
        