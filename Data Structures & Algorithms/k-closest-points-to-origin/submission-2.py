class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            dist1 = self.edist(points[i][0], points[i][1])
            if len(heap)<k:
                heapq.heappush_max(heap,[dist1,points[i]])
                continue
            dist2,point2 = heapq.heappop_max(heap)
            if dist1<dist2:
                heapq.heappush_max(heap,[dist1,points[i]])
            else:
                heapq.heappush_max(heap,[dist2,point2])
        result = []

        for dist, point in heap:
            result.append(point)

        return result
    
    def edist(self,x,y):
        return math.sqrt(pow((x-0),2) + pow((y-0),2))
        