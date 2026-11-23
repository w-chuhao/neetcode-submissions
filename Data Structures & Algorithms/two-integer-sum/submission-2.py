class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = {}
        ans = []

        for i in range(len(nums)):
            second = target - nums[i]

            if second in mp:
                ans.append(mp[second])
                ans.append(i)
            else:
                mp[nums[i]] = i
        
        return ans;
    