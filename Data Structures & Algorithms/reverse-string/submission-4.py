class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(left, right): 
            if left < right:
                reverse(left + 1, right - 1)
                s[left], s[right] = s[right], s[left]

        reverse(0, len(s)-1)
