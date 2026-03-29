#!/usr/bin/env python3
"""rabin_karp - Rabin-Karp rolling hash string matching."""
import sys

def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    results = []
    h_pattern = 0
    h_text = 0
    power = 1
    for i in range(m - 1):
        power = (power * base) % mod
    for i in range(m):
        h_pattern = (base * h_pattern + ord(pattern[i])) % mod
        h_text = (base * h_text + ord(text[i])) % mod
    for i in range(n - m + 1):
        if h_pattern == h_text:
            if text[i:i + m] == pattern:
                results.append(i)
        if i < n - m:
            h_text = (base * (h_text - ord(text[i]) * power) + ord(text[i + m])) % mod
            if h_text < 0:
                h_text += mod
    return results

def test():
    assert rabin_karp("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert rabin_karp("aaaaaa", "aa") == [0, 1, 2, 3, 4]
    assert rabin_karp("hello", "xyz") == []
    assert rabin_karp("test test test", "test") == [0, 5, 10]
    print("OK: rabin_karp")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: rabin_karp.py test")
