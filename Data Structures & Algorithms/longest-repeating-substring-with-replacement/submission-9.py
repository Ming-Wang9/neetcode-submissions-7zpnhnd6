class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #can't remember how many time you've done this
        #you better can figure it out next time!
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r], 0)
            while (r-l+1 - max(count.values()))>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
