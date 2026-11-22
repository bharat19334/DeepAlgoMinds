class Solution(object):
    def checkString(self, s):
        

    
        i = 0
        while i<len(s)-1:
            if s[i] == "b" and s[i+1] == "a":
                return False
            i+=1
        return True
            
            