class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = [0] * 26
        heap = []

        for task in tasks:
            freq[ord(task) - ord('A')] -= 1
        
        for f in freq:
            if f<0:
                heapq.heappush(heap,f)
        
        queue = deque()
        time = 0
        while heap or queue:
            time+=1
            while queue and queue[0][1] <= time:
                freq, available_time = queue.popleft()
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)
                freq+=1

                if freq<0:
                    queue.append([freq,time+n+1])
        
        return time


        
