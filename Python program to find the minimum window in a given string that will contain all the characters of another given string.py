# Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "OERIUS"

def min_window(s, t):
    from collections import Counter

    if not s or not t:
        return ""

    t_count = Counter(t)
    window = {}
    have, need = 0, len(t_count)
    res = [-1, -1]
    res_len = float("inf")
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in t_count and window[char] == t_count[char]:
            have += 1

        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""


str1 = input().strip()
str2 = input().strip()
print("Minimum window is", min_window(str1, str2))