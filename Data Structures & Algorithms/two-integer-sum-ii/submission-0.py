class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        sum_total = numbers[left] + numbers[right]
        ans = []

        while sum_total != target:
            if sum_total>target:
                right-=1
            else:
                left+=1
            sum_total = numbers[left] + numbers[right]
        
        ans.append(left+1)
        ans.append(right+1)

        return ans




        