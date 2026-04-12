class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            s = str(len(s)) +"#" + s
            string += s
        return string

    def decode(self, s: str) -> List[str]:
        stringList = []
        idx = 0
        while idx < len(s):
            i = idx 
            while s[i] != "#":
                i += 1
            length = int(s[idx:i])
            i+=1
            stringList.append(s[i : i+length])
            idx = i + length
        return stringList


