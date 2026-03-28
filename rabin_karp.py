#!/usr/bin/env python3
"""rabin_karp - Rabin-Karp rolling hash string search."""
import sys
def search(text,pattern,base=256,mod=101):
    n,m=len(text),len(pattern);matches=[]
    if m>n:return matches
    ph=th=0;h=pow(base,m-1,mod)
    for i in range(m):ph=(base*ph+ord(pattern[i]))%mod;th=(base*th+ord(text[i]))%mod
    for i in range(n-m+1):
        if ph==th and text[i:i+m]==pattern:matches.append(i)
        if i<n-m:th=(base*(th-ord(text[i])*h)+ord(text[i+m]))%mod
    return matches
def multi_search(text,patterns):
    results={}
    for p in patterns:results[p]=search(text,p)
    return results
if __name__=="__main__":
    if len(sys.argv)<3:print("Usage: rabin_karp.py <pattern> <text>");sys.exit(1)
    pattern=sys.argv[1];text=sys.argv[2]
    matches=search(text,pattern);print(f"{len(matches)} matches: {matches}")
