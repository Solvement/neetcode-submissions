class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        st=[]
        left=[-1]*n
        ans=float("-inf")
        for i,h in enumerate(heights):
            while st and heights[st[-1]]>=h:
                st.pop()
            if st:
                left[i]=st[-1]
            st.append(i)
        st.clear()
        right=[n]*n
        for i in range(n-1,-1,-1):
            h=heights[i]
            while st and heights[st[-1]]>=h:
                st.pop()
            if st:
                right[i]=st[-1]
            st.append(i)
        for h,l,r in zip(heights,left,right):
            ans=max(ans,(r-l-1)*h)

        return ans