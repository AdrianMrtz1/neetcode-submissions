class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def canBreak(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            for j in range(i+1, len(s) + 1):
                word = s[i:j]
                if word in wordSet:
                    if canBreak(j):
                        memo[i] = True
                        return True
                
            memo[i] = False
            return False
        
        return canBreak(0)

        