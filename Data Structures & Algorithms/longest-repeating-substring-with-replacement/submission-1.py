from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long_len = 0
        s_len = len(s)
        l, r = 0, 0
        hmap = defaultdict(int)
        while l <= r and r < s_len:
            hmap[s[r]] += 1
            max_freq = max(hmap.values())
            if ((r - l + 1) - max_freq) <= k:
                long_len = max(long_len, r - l + 1)
                r += 1
            else:
                hmap[s[l]] -= 1
                hmap[s[r]] -= 1
                l += 1
        return long_len