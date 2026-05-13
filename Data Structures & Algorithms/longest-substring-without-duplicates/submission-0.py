class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_without_duplicate = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_without_duplicate = max(longest_without_duplicate, right - left + 1)

        return longest_without_duplicate