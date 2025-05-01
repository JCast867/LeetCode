class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        nums = []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
                
        for j in nums2:
            if j in dic and j not in nums:
                nums.append(j)

        return nums