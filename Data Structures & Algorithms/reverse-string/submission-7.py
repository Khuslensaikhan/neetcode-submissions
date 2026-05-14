class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

        i = 0 
        while stack:
            s[i] = stack.pop()
            i+=1