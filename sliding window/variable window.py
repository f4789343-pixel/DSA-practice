def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    freq = {}
    max_ = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1
        max_= max(max_, right-left+1)
    return max_
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
        