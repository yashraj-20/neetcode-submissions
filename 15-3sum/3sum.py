class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        # -4, -1, -1, 0, 1, 2

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1

            while j < k:
                su = nums[i] + nums[j] + nums[k]
                if su > 0:
                    k -= 1
                elif su < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res