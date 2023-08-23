class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        count = collections.Counter(s)
        max_count = max(count.values())
        if max_count > (len(s) + 1) // 2:
            return ""
        ans = [None] * len(s)
        even, odd = 0, 1
        half = len(s) // 2
        for c, cnt in count.items():
            while cnt > 0 and cnt <= half and odd < len(s):
                ans[odd] = c
                cnt -= 1
                odd += 2
            while cnt > 0:
                ans[even] = c
                cnt -= 1
                even += 2
        return "".join(ans)