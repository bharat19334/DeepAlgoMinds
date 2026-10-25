class Solution(object):
    def hammingDistance(self, x, y):
        
        binary_strX = ""
        binary_strY = ""
        while x>0:
            a = x%2
            binary_strX += str(a)
            x = x//2
    
        while y>0:
            a = y%2
            binary_strY += str(a)
            y = y//2

        x = binary_strX[::-1]
        y = binary_strY[::-1]

        length = max(len(x), len(y))
        x = x.zfill(length)
        y = y.zfill(length)

        count = 0
        for n in range(0,length):
            if x[n] != y[n]:
                count +=1
                
        return count 
