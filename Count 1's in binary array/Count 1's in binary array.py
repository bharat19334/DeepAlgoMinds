class Solution:
    def countOnes(self, arr):
        
        count = 0
        i=0
        while i<len(arr):
            if arr[i]==1:
                count +=1
            i+=1
        return count
