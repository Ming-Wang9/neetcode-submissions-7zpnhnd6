class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = {}
        for s in strs:
            patten = ''.join(sorted(s))
            if patten not in sdict:
                sdict[patten] = []
            sdict[patten].append(s)
        return list(sdict.values())