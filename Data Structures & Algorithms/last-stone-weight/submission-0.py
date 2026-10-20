class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)

            if a>b:
                a = a-b
                heapq.heappush_max(stones,a)
            elif a<b:
                b = b-a
                heapq.heappush_max(stones,b)
        
        if not stones:
            return 0
        
        return stones[0]
