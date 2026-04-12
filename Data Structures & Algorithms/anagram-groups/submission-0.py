class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strhash = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            strhash[key].append(s)
        return list(strhash.values())