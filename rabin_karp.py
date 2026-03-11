#!/usr/bin/env python3
"""Rabin-Karp string search."""
import sys
if len(sys.argv)<3: sys.exit("Usage: rabin_karp <pattern> <text|file>")
pat, arg = sys.argv[1], sys.argv[2]
try: text = open(arg).read()
except: text = arg
d, q, m = 256, 101, len(pat)
hp = ht = 0; h = pow(d, m-1, q); matches = []
for i in range(m): hp=(d*hp+ord(pat[i]))%q; ht=(d*ht+ord(text[i]))%q
for i in range(len(text)-m+1):
    if hp==ht and text[i:i+m]==pat: matches.append(i)
    if i<len(text)-m: ht=(d*(ht-ord(text[i])*h)+ord(text[i+m]))%q
print(f"Found {len(matches)} match(es)" + (f": {matches[:20]}" if matches else ""))
