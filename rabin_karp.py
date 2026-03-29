#!/usr/bin/env python3
"""Rabin-Karp string search. Zero dependencies."""

def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m > n or m == 0: return []
    h_pat = 0; h_txt = 0; h = pow(base, m - 1, mod)
    matches = []
    for i in range(m):
        h_pat = (base * h_pat + ord(pattern[i])) % mod
        h_txt = (base * h_txt + ord(text[i])) % mod
    for i in range(n - m + 1):
        if h_pat == h_txt and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            h_txt = (base * (h_txt - ord(text[i]) * h) + ord(text[i + m])) % mod
            if h_txt < 0: h_txt += mod
    return matches

def multi_search(text, patterns):
    result = {}
    for p in patterns:
        m = rabin_karp(text, p)
        if m: result[p] = m
    return result

if __name__ == "__main__":
    print(rabin_karp("AABAACAADAABAABA", "AABA"))
