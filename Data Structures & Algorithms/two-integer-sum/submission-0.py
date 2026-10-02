class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums is a list of numbers
        # target is the sum of any two given indexes
        # return the indices i,j such that nums[i] + nums[j] == target and i != j
        # create a hash map to store value
        seen = dict()
        # loop throught the nums in the list
        for i, num in enumerate(nums):
            # the complement is the exact number required to reach the target when added to the current number.
            complement = target - num  # calc the exact number needed to reach target
            # check if the complement is already in the map
            if complement in seen:
                return [seen[complement], i]

            # store the current numbers index in the map
            seen[num] = i
        return [] # return empty list if no pair is found


                