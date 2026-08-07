class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x1, y1 = point[0], point[1]
            dist = math.sqrt(((x1) ** 2) + ((y1) ** 2))
            heapq.heappush(heap, (dist, [x1, y1]))
        res = []
        count = 0
        while count < k:
            res.append(heapq.heappop(heap)[1])
            count += 1
        return res