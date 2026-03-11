#!/usr/bin/env python3
"""Rabin-Karp — rolling hash string matching."""
import sys

def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m > n: return []
    h_pattern = 0; h_text = 0; h = pow(base, m-1, mod)
    results = []
    for i in range(m):
        h_pattern = (base * h_pattern + ord(pattern[i])) % mod
        h_text = (base * h_text + ord(text[i])) % mod
    for i in range(n - m + 1):
        if h_pattern == h_text and text[i:i+m] == pattern:
            results.append(i)
        if i < n - m:
            h_text = (base * (h_text - ord(text[i]) * h) + ord(text[i+m])) % mod
    return results

def multi_search(text, patterns):
    results = {}
    for p in patterns:
        positions = rabin_karp(text, p)
        if positions: results[p] = positions
    return results

if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    for pat in ["AABA", "AA", "BAA"]:
        pos = rabin_karp(text, pat)
        print(f"  '{pat}' at: {pos}")
