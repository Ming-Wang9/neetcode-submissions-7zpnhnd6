class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        window, tdict = {}, {}
        for c in t:
            tdict[c] = 1+tdict.get(c,0)
        minlen = len(s)+1
        res = ''
        have, need = 0, len(tdict)
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            if s[r] in tdict and window[s[r]] == tdict[s[r]]:
                have+=1
            while have == need:
                if (r-l+1)<minlen:
                    res=s[l:r+1]
                    minlen=r-l+1
                window[s[l]]-=1
                if s[l] in tdict and window[s[l]] < tdict[s[l]]:
                    have-=1
                l+=1 
        return res




