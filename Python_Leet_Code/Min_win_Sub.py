s="a"
t="b"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ##initialize variable with returned combo
        output = [None] * (len(s)+1)
        i = 0
        j = 0
        c_t = list(t)
        temp_out = []

        if len(t) > len(s):
            return ''
    
            
        else:
            while i<len(s):
                if s[i] in c_t:
                    j = i
                    r_t = c_t[:]
                    while len(r_t) > 0: 
                        if s[j] in r_t:
                            temp_out.append(s[j])
                            r_t.remove(s[j])
                            if j == len(s)-1 and len(r_t) > 0:
                                temp_out = [None] * (len(s)+1)
                                break
                            elif j == len(s)-1 and len(r_t) == 0:
                                break 
                            else:       
                                j = j+1
                        else:
                            temp_out.append(s[j])
                            if j == len(s)-1 and len(r_t) > 0:
                                temp_out = [None] * (len(s)+1)
                                break
                            elif j == len(s)-1 and len(r_t) == 0:
                                break 
                            else:       
                                j = j+1
                    
                    if temp_out is not None and len(temp_out) <= len(output):

                        output = temp_out
                    
                    i = i + 1
                    temp_out = []
                
                else:
                    i = i + 1
            

            if output == [None] * (len(s)+1):
                return ''
            else:
                return "".join(output)
    
sol = Solution()
print(sol.minWindow(s,t))  