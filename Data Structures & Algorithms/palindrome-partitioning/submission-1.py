class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #have a helper function to determine if palidrome
        #then do backtrack with each character, like a 
        #decision tree, either add this word if palindrome
        #or not add it, if it is not palidrome, move to next charater

        def isPali(string):
            if len(string) == 1:
                return True
            l,r = 0, len(string)-1
            while l<=r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True

        res = []
        part = []
        def backtrack(i):
            if i == len(s):
                res.append(part.copy())
                return 
            for j in range(i, len(s)):
                if isPali(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
        






