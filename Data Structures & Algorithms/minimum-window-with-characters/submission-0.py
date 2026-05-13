'''
Observations:
Iterate through s while maintaining a window
We need to understan when to expand and when to shrink the window.
Expand until: we have all the target char in the window.
    save the result.
Shrink after saving results: until we don't have one of the char in the window

I need to compare the current window to the target.
If the target string is in the current window return current window.
Else return ""

Objectives:
1. How do we know all the target char is in the window
2. How do we know if we lose one of the char while shrinking
(Let's use hashmap to count the characters) as window expands

3. Expand the window by moving the right pointer and adding chars into window map
4. Once it covers target we shrink to make it small as possible.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        have = 0 # how many chars currently meet the required count
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")

        left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need: 
                if(right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""


















