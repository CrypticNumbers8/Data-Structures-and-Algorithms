import numpy as np
class Solution:

    def longestCommonSubsequence_Recursive(self, text1: str, text2: str) -> int:
        
            x = list(text1)
            y = list(text2)
            n = len(x)
            m = len(y)
                
            if n == 0 or m == 0:
                return 0
            if(x[n-1] == y[m-1]):
                return 1 + self.longestCommonSubsequence_Recursive(text1[0:n-1],text2[0:m-1])
            else:
                return max(self.longestCommonSubsequence_Recursive(text1[0:n],text2[0:m-1]),
                               self.longestCommonSubsequence_Recursive(text1[0:n-1],text2[0:m]))



    def helper_memoize(self,a,b,i,j,dp):

            if i == 0 or j == 0:
                dp[i][j] = 0
                
            if dp[i][j] != -1:
                return dp[i][j]
            
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + self.helper_memoize(a,b,i-1,j-1,dp)
            else:
                dp[i][j] = max(self.helper_memoize(a,b,i,j-1,dp),self.helper_memoize(a,b,i-1,j,dp))
                
            return dp[i][j]
    

    def longestCommonSubsequence_Recursive_Memoize(self,a:str,b:str):
        
        x = list(a)
        y = list(b)
        m = len(x)
        n = len(y)
        dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        print(dp)
        result = self.helper_memoize(x,y,m,n,dp)
        print(dp)
        print(result)            



    def longestCommonSubsequence_DP_BottomUp(self, text1: str, text2: str):
        

        a = list(text1)
        b = list(text2)
        
        m = len(text1)
        n = len(text2)
        
        t= [[-1 for i in range(n+1)]for j in range(m+1)]

        for i in range(m+1):
            t[i][0] = 0
        for j in range(n+1):
            t[0][j] = 0
    
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if a[i-1] == b[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i][j-1], t[i-1][j])
                                        
        print( "LCS lengths:",t[m][n] )
        return t[m][n],t


    def LCSubstring(self, X:str, Y:str,):
        a = list(X)
        b = list(Y)

        m = len(a)
        n = len(b)

        r= [[-1 for i in range(n+1)]for j in range(m+1)]

        for i in range(m+1):
            r[i][0] = 0
        for j in range(n+1):
            r[0][j] = 0
    
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if a[i-1] == b[j-1]:
                    r[i][j] = 1 + r[i-1][j-1]
                else:
                    r[i][j] = 0

        print(r)
        print("LCSubstring length =",np.max(r))

    def printLCS(self, X:str, Y:str):
        tnew,d1 = self.longestCommonSubsequence_DP_BottomUp(X,Y)
        print(tnew,d1)

        a = list(X)
        b = list(Y)
        #print(a,b)

        lcstr = []

        i = len(a)
        j = len(b)
        #print(i,j)

        while (i>0 and j>0):
            if a[i-1] == b[j-1]:
                lcstr.append(a[i-1])
                #print(lcstr)
                i = i-1
                j = j-1
            else:
                if(d1[i-1][j]>d1[i][j-1]):
                    i = i-1
                else:
                    j = j-1

        lcstr.reverse()
        print("LCS string:","".join(lcstr))

    def length_of_shortest_common_supersequence(self,x:str,y:str):

        m = len(x)
        n = len(y)

        lcs, w = self.longestCommonSubsequence_DP_BottomUp(x,y)

        print("SCS LENGTH:",m+n-lcs)

    def print_shortest_common_supersequence(self, x:str, y:str):

        scs_str = []
        a1 = list(x)
        b1 = list(y)
        #print(a1,b1)
        lcs, dp = self.longestCommonSubsequence_DP_BottomUp(x,y)
        #print(lcs)
        #print(dp)

        i = len(x)
        j = len(y)

        print(dp)

        while (i>0 and j>0):
            if a1[i-1] == b1[j-1]:
                scs_str.append(b1[j-1])
                dp[i][j] = 50000
                i -= 1
                j -= 1

            else:
                if(dp[i-1][j] > dp[i][j-1]):
                    scs_str.append(a1[i-1])
                    dp[i][j] = 60000
                    i -= 1

                else: #(dp[i-1][j] < dp[i][j-1]):
                    scs_str.append(b1[j-1])
                    dp[i][j] = 70000

                    j -= 1

        print(dp)

        while i>0:
            scs_str.append(a1[i-1])
            print("i--")
            i -= 1

        while j>0:
            scs_str.append(b1[j-1])
            print("j--")
            j -= 1


        print("SCS string:","".join(scs_str[::-1]))


if __name__ == '__main__':

    l1 = Solution()
    print("START")
    print(l1.longestCommonSubsequence_Recursive('abcef','abfr'))
    print("------------------------CHECKPOINT---------------------------")
    l1.longestCommonSubsequence_Recursive_Memoize('abcef','abfr')
    print("------------------------CHECKPOINT---------------------------")
    l1.longestCommonSubsequence_DP_BottomUp('abcef','abfr')
    print("------------------------CHECKPOINT---------------------------")
    l1.LCSubstring('abcef','abfr')
    print("------------------------CHECKPOINT---------------------------")
    l1.printLCS('abcef','abfr')
    print("------------------------CHECKPOINT---------------------------")
    l1.length_of_shortest_common_supersequence('abcef','abfr')
    print("------------------------CHECKPOINT---------------------------")
    l1.print_shortest_common_supersequence('abcef','abfr')
    print("END")
