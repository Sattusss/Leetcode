from functools import lru_cache
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dp(unique_songs, listened_songs):
            if unique_songs == 0 and listened_songs==0:return 1
            if unique_songs<0 or unique_songs>listened_songs:return 0
            res = dp(unique_songs-1, listened_songs-1)*(N-(unique_songs-1))  % MOD
            if unique_songs-K > 0:
                res += dp(unique_songs, listened_songs-1)*(unique_songs-K) % MOD
            return res % MOD
        return dp(N, L)
