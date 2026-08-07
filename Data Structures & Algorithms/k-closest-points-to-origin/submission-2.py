class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(heap, (dist, [x, y]))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res