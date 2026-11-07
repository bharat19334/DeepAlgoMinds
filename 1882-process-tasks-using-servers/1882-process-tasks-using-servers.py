class Solution(object):
    def assignTasks(self, servers, tasks):
        
        free = []
        busy = []
        ans = []
        time = 0

        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))

        for j in range(len(tasks)):

            time = max(time, j)

            while busy and busy[0][0] <= time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)

            ans.append(idx)

            heapq.heappush(busy, (time + tasks[j], weight, idx))

        return ans