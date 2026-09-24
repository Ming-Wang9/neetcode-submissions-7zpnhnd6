class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sformat = [0]*26
            for c in s:
                sformat[ord(c)-ord('a')] +=1
            res[tuple(sformat)].append(s)
        return list(res.values())