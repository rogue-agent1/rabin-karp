from rabin_karp import rabin_karp, multi_search
assert rabin_karp("AABAACAADAABAABA", "AABA") == [0, 9, 12]
assert rabin_karp("hello world", "world") == [6]
assert rabin_karp("aaa", "a") == [0, 1, 2]
assert rabin_karp("abc", "xyz") == []
assert rabin_karp("", "a") == []
ms = multi_search("the cat sat on the mat", ["the", "at"])
assert ms["the"] == [0, 15]
assert 5 in ms["at"]  # "cat" has "at" at 5
print("rabin_karp tests passed")
