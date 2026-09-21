class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            strdict[tuple(count)].append(s)
        return list(strdict.values())            
            
