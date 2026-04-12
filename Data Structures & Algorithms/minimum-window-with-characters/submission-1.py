class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, t_dic = {}, {}
        for c in t:
            t_dic[c] = 1 + t_dic.get(c, 0)
        have = 0
        need = len(t_dic)
        min_len = float("inf")
        l =0 
        res = ""
        for r in range(len(s)):
            window[s[r]] = 1+ window.get(s[r], 0)
            if s[r] in t_dic and window[s[r]] == t_dic[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < min_len:
                    min_len = r-l +1
                    res =s[l:r+1]
                window[s[l]] -= 1
                if s[l] in t_dic and window[s[l]] < t_dic[s[l]]:
                    have -= 1
                l+=1
        return res
        