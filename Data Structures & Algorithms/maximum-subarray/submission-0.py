class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        # Initialize max_sum to the first element
        current_sum = nums[0]
        # Initialize current_sum to the first element

        for num in nums[1:]:
            # Iterate over the rest of the elements
            current_sum = max(num, current_sum + num)
            # Update current_sum to either the current number or current_sum + num
            max_sum = max(max_sum, current_sum)
            # Update max_sum if current_sum is greater

        return max_sum
        # Return the maximum subarray sum found
        