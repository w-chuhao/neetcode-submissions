class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set()

        for i in range(len(nums)):
            s.add(nums[i])
        

        max_count = 0
        count = 0

        for i in range(len(nums)):
            if nums[i]-1 not in s:
                current_num = nums[i]
                count=1
                while nums[i]+1 in s:
                    count+=1
                    nums[i]+=1
            
            max_count = max(max_count, count)
        
        return max_count
