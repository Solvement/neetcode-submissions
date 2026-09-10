class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = Counter(t)
        window = Counter()

        l = 0
        have = 0
        need = len(target)

        ansleft = -1
        ansright = -1
        anslen = float("inf")

        for r, ch in enumerate(s):
            window[ch] += 1

            if ch in target and window[ch] == target[ch]:
                have += 1

            while have == need:
                if r - l + 1 < anslen:
                    ansleft = l
                    ansright = r
                    anslen = r - l + 1

                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1

                l += 1

        if ansleft == -1:
            return ""

        return s[ansleft:ansright + 1]