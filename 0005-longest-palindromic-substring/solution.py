class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        matrix=[[False]*n for _ in range(n)]
        longest=0
        ans=[0,0]
        for i in range(n):
            matrix[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                matrix[i][i+1]=True
                ans=[i,i+1]
        for diff in range(2,n):
            for i in range(n-diff):
                j=i+diff
                if s[i]==s[i+diff] and matrix[i+1][j-1]:
                    matrix[i][j]=True
                    ans=[i,j]
        i,j=ans
        return s[i:j+1]