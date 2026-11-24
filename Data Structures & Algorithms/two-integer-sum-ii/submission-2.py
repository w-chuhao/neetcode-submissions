class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ans = []

        left = 0
        right = len(numbers)-1

        while left<right:
            total = numbers[left] + numbers[right]

            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                ans.append(left+1)
                ans.append(right+1)
                return ans
        
        return []





        