class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input: s = "racecar", t = "carrace"
        # Output: true

        #If the lengths of the strings differ, return false immediately.
        if len(s) != len(t):
            return False 

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        

        # Create a frequency array count of size 26 initialized to 0.
        # Iterate through both strings:
        # Increment the count at the index corresponding to s[i].
        # Decrement the count at the index corresponding to t[i].
        # After processing both strings, scan through the count array:
        # If any value is not 0, return false because the frequencies differ.
        # If all values are 0, return true since the strings are anagrams.