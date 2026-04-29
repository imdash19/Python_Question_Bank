# Write a Python program to count the number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.

def at_most_k(s, k):
    freq = {}
    left = 0
    count = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        count += right - left + 1

    return count


def exactly_k(s, k):
    return at_most_k(s, k) - at_most_k(s, k - 1)


s = input().strip()
k = int(input())
print(exactly_k(s, k))