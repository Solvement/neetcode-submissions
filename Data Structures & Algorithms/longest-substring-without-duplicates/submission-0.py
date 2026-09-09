class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        n=len(s)
        l=0
        res=0
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            res=max(res,r-l+1)
        return res
