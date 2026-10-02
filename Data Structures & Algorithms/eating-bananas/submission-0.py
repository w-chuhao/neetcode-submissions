class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        right = max(piles)
        left = 1

        mid = (left + right) // 2

        ans = 0


        while left<=right:
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
            
            if hour <= h:
                ans = mid
                right = mid-1
            
            if hour>h:
                left = mid + 1

            
            mid = (left+right)//2
        

        return ans





        