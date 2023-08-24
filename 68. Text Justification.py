class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        cur_len = 0
        for word in words:
            if cur_len + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - cur_len):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur = []
                cur_len = 0
            cur.append(word)
            cur_len += len(word)
        res.append(" ".join(cur).ljust(maxWidth))
        return res
