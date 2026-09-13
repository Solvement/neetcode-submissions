class Solution:
    def isValid(self, s: str) -> bool:
        map={")":"(","]":"[","}":"{"}
        st=[]
        for ch in s:
            if ch not in map:
                st.append(ch)
            elif not st or st.pop()!=map[ch]:
                return False
        if st:
            return False
        return True
