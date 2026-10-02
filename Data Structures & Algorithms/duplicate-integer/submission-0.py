class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        seen = set()

        for num in nums:
            if num in seen:
               duplicates.add(num)
            else:
                seen.add(num)

        if len(duplicates) > 0:
            return True
        else:
            return False