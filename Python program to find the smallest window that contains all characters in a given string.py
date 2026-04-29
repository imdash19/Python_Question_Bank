# Write a Python program to find the smallest window that contains all characters in a given string.

def smallest_window(s):
    unique_chars = set(s)
    need = len(unique_chars)

    freq = {}
    left = 0
    min_len = float('inf')
    result = ""

    have = 0

    for right in range(len(s)):
        c = s[right]
        freq[c] = freq.get(c, 0) + 1

        if freq[c] == 1:
            have += 1

        while have == need:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                result = s[left:right+1]

            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                have -= 1
            left += 1

    return result


s = input().strip()
print("Smallest window containing all characters:", smallest_window(s))