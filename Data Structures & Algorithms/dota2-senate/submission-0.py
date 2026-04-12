class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D,R= deque(), deque()
        for i,v in enumerate(senate):
            if v == 'R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            d = D.popleft()
            r = R.popleft()
            if r <d:
                R.append(r+len(senate))
            else:
                D.append(d+len(senate))
        return 'Radiant' if R else 'Dire'