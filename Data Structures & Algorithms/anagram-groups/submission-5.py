class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadic = {}
        for s in strs:
            patten = "".join(sorted(s))
            if patten not in anadic:
                anadic[patten] = []
            anadic[patten].append(s)
        return list(anadic.values())