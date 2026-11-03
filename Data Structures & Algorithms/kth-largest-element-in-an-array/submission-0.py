class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap,num)
                continue
            
            x = heap[0]
            if x<=num:
                heapq.heappushpop(heap,num)

        return heap[0]
            
            
        