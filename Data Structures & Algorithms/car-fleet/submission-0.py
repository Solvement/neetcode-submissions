class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st=[]
        pairs=[(p,s) for p,s in zip(position,speed) ]
        pairs.sort(reverse=True)
        for pair in pairs:
            t=(target-pair[0])/pair[1]
            st.append(t)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
            

        return len(st)