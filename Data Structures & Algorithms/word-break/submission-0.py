class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # solve it with dp algo, from top to buttom
        dp = [False] * (len(s) +1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    #break the loop, because it doesn't have to
                    #match every word in the wordDict, can even 
                    #take duplicate, so should move on to next index
                    # that says, if doesn't meet the condition below
                    # we've check the next few index doesn't combine
                    # a word in the dict, so can return false 
                    if dp[i]:
                        break
        return dp[0]
                    