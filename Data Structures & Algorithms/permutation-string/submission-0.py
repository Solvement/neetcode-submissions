class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        count1=Counter(s1)
        count2=Counter(s2[:len(s1)])
        if count1==count2:
            return True
        for i in range(n1,n2):
            count2[s2[i]]+=1
            count2[s2[i-n1]]-=1
            if count2[s2[i-n1]]==0:
                del count2[s2[i-n1]]

            if count1==count2:
                return True

        return False
