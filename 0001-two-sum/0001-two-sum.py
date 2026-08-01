class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):

            op = target-nums[i]
            
            if op in seen:
                 return [seen[op], i]

            seen[nums[i]] = i