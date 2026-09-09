from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            # 当需要替换的字符数超过 k 时，收缩左窗口
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # 记得把移出窗口的字符数量 -1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res