class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countHash = {}
        
        for ch in s:
            countHash[ch] = countHash.get(ch, 0) + 1
        
        for ch in t:
            if ch not in countHash:
                return False
            countHash[ch] -= 1

            if countHash[ch] < 0:
                return False
        return True
             
            
        