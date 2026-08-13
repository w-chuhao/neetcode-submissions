class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ans = []
        for i in range(len(nums)):
            second = target - nums[i];

            if second in map:
                ans.append(map.get(second))
                ans.append(i)
            
            else:
                map[nums[i]] = i;
        
        return ans;
        