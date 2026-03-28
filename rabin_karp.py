#!/usr/bin/env python3
"""Rabin-Karp string matching with rolling hash."""
import sys
def rabin_karp(text,pattern,base=256,mod=101):
    n,m=len(text),len(pattern);matches=[]
    if m>n: return matches
    ph=th=0;h=pow(base,m-1,mod)
    for i in range(m):
        ph=(base*ph+ord(pattern[i]))%mod
        th=(base*th+ord(text[i]))%mod
    for i in range(n-m+1):
        if ph==th and text[i:i+m]==pattern: matches.append(i)
        if i<n-m:
            th=(base*(th-ord(text[i])*h)+ord(text[i+m]))%mod
            if th<0: th+=mod
    return matches
def main():
    if "--demo" in sys.argv:
        text="the quick brown fox jumps over the lazy dog the end"
        for pat in ["the","fox","xyz"]:
            print(f"'{pat}' found at: {rabin_karp(text,pat)}")
    elif len(sys.argv)>2: print(rabin_karp(sys.argv[1],sys.argv[2]))
if __name__=="__main__": main()
