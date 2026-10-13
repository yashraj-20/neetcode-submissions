class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pref = 1
        suff = 1
        maxi = -1e9
        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref = pref * nums[i]
            suff = suff * nums[n-1-i]
            maxi = max(maxi, pref, suff)
        return maxi
