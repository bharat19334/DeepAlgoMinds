class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        
        # Brute force
        
        count = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if l <= arr[i]+arr[j]+arr[k] <= r:
                        count +=1
        return count
        
        