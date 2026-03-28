#!/usr/bin/env python3
"""rabin_karp - Rabin-Karp rolling hash string search."""
import argparse

def rabin_karp(text: str, pattern: str, base: int = 256, mod: int = 101) -> list:
    n, m = len(text), len(pattern)
    if m > n: return []
    matches = []
    h_pattern = h_text = 0
    power = pow(base, m - 1, mod)
    for i in range(m):
        h_pattern = (h_pattern * base + ord(pattern[i])) % mod
        h_text = (h_text * base + ord(text[i])) % mod
    for i in range(n - m + 1):
        if h_pattern == h_text and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            h_text = ((h_text - ord(text[i]) * power) * base + ord(text[i + m])) % mod
    return matches

def main():
    p = argparse.ArgumentParser(description="Rabin-Karp search")
    p.add_argument("pattern"); p.add_argument("text", nargs="?")
    p.add_argument("-f", "--file")
    args = p.parse_args()
    if args.file: text = open(args.file).read()
    elif args.text: text = args.text
    else: import sys; text = sys.stdin.read()
    matches = rabin_karp(text, args.pattern)
    print(f"Matches: {len(matches)} at {matches[:20]}")

if __name__ == "__main__":
    main()
