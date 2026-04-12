class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, tmap = {},{}
        for c in t:
            tmap[c]=1+tmap.get(c,0)
        have,needCount=0,len(tmap)
        minlen=float('inf')
        l=0
        res=''
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have +=1
            while have == needCount:
                if (r-l+1) < minlen:
                    res=s[l:r+1]
                    minlen=r-l+1
                window[s[l]]-=1
                if s[l] in tmap and window[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1
        return res





