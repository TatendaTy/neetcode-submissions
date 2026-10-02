class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = dict()
        
        for num in nums:
            if num in frequencyMap:
                # increment the count if num has already been seen
                frequencyMap[num] = frequencyMap[num] + 1
            else:
                # initialize count to 1 for first encounter
                frequencyMap[num] = 1
        
        # Sort the keys of frequencyMap according to their values, from highest to lowest.
        sortedNums = sorted(
            frequencyMap,
            key=frequencyMap.get,
            reverse=True
        )

        return sortedNums[:k]
        