class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)

        while min_k <= max_k:
            mid = min_k + (max_k - min_k)//2

            hour = 0
            for i in piles:
                hour += (i + mid-1)//mid

            if hour <= h:
                max_k = mid -1
            else:
                min_k = mid +1
            
        return min_k
