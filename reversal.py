#!/bin/env python3
# Reversal Sorting examples from Chapter 5
# Copyright 2017 - Humberto Ortiz-Zuazaga

def SimpleReversalSort(pi):
    "Sort a permutation pi by flipping segments."
    # compute the identity permutation once
    identity = sorted(pi)
    # loop over list indicies, flip correct element into place
    for i in range(len(pi) -1):
        j = pi.index(i)
        if i != j:
            pi = flip(pi, i, j)
            print(pi)
        if pi == identity:
            return

def flip(pi, i, j):
    "Flip the segment of pi between i and j (inclusive)"
    middle = pi[i:j+1]
    middle.reverse()
    return pi[:i] + middle + pi[j+1:]

if __name__ == "__main__":
    # in book is 3 5 2 4 1
    mouse = [2,4,1,3,0]
    print("Mouse to man")
    print(mouse)
    SimpleReversalSort(mouse)
