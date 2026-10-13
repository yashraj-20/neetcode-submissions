class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = len(set(nums))
        my_list = len(nums)

        if my_set == my_list:
            return False
        else:
            return True


