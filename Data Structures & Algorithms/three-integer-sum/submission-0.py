class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []


        for i in range(len(nums)):
            
            j = i+1
            k = len(nums)-1
            if i==k-1:
                break

            while j<k:
                arr = []

                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    arr.append(nums[i])
                    arr.append(nums[j])
                    arr.append(nums[k])
                    j+=1
                    k-=1
                    if arr in ans:
                        continue
                    
                    ans.append(arr)

        return ans
                



        
        