class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            mp[nums[i]] = 1
            
        return False