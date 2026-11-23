class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        leng = max_len = 0
        for num in nums:
            if (num-1) not in nums:
                leng = 0
            
                while (num+leng) in nums:
                    leng += 1
                max_len = max(leng, max_len)
        return max_len