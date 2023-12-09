def prefix_function(haystack):
    n = len(haystack)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and haystack[j] != needle[i]:
            j = pi[j-1]
        if needle[i] == haystack[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(haystack, needle, start_index=0):
    j = 0
    pi = prefix_function(needle)
    for i in range(start_index, len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = pi[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j >= len(needle):
            return i - j + 1
    return None


haystack = "abcabcabcabcabd"
needle = "abcabd"

print(kmp_search(haystack, needle, 0))
print(prefix_function(needle))

