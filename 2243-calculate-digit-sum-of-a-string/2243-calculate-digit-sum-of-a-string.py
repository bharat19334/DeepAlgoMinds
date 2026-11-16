class Solution(object):
    def digitSum(self, s, k):
        
        while len(s)>k:

            result = ""
            i = 0
            while i<len(s):
                total = 0
                for j in range(i,i+k):
                    if j < len(s):
                        total += int(s[j])

                result +=str(total)
                i += k

            s = result

        return s