# partial.py - Compute characteristics of partial digests of DNA with enzymes
# Copyright 2017 Humberto Ortiz-Zuazaga <humberto.ortiz@upr.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import itertools
from collections import Counter

def deltaX(X):
    """Given X, a list of restriction sites, 
    compute delta X, the list of fragment sizes 
    produced by a partial digest"""
    result = []
    for i in range(len(X) - 1):
        for j in range(i+1, len(X)):
            result.append(X[j] - X[i])
    result.sort()
    return result

def sameAs(X, Y):
    "Are lists X and Y the same?"
    return set(X) == set(Y)

def BruteForcePDP(L, n):
    "Given L, a list of fragment sizes, compute X, the list of sites"

    M = max(L)
    for sites in itertools.combinations(range(1, M-1), n-2):
        X = [0] + list(sites) + [M]
        dX = deltaX(X)
        if sameAs(dX, L):
            return X
        
    print("No solution")
    return []

def AnotherBruteForcePDP(L, n):
    "Given L, a sorted list of fragment sizes, compute X, the list of sites"

    M = L[-1]
    
    for sites in itertools.combinations(L[:-1], n-2):
        X = [0] + list(sites) + [M]
        dX = deltaX(X)
        if sameAs(dX, L):
            return X

    print("No solution")
    return []

def delta(y, X):
    "Compute the distances between y and each of the elements of X"
    return [abs(y-elem) for elem in X]

def containedin(s1, s2):
    "Is s1 contained in s2?"
    copy = s2[:]
    for elem in s1:
        if elem in copy:
            copy.remove(elem)
        else:
            return False
    return True

def takeout(s1, s2):
    "Remove the elements of s1 from s2."
    for elem in s1:
        s2.remove(elem)

def PartialDigest(L):
    "Given the list of fragment sizes L, compute X, the set of restriction sites"
    width = max(L)
    L.remove(width)
    X = [0, width]
    Place(L, X, width)

def Place(L, X, width):
    "Use Skiena's recursive algorithm to compute X from L"

    if [] == L:
        print ("Found", sorted(X))
        return

    y = max(L)
    # Try placing y closest to the end of X
    dyx = delta(y, X)

    if containedin (dyx, L):
        # add y to X and remove dyx from L
        X.append(y)
        takeout(dyx, L)
        # try the rest (recursively)
        Place(L,X, width)
        # remove y from X and put dyx back into L
        X.remove(y)
        L.extend(dyx)

    # If not, try closest to the start
    dyx = delta(width-y,X)

    if containedin (dyx, L):
        # add width-y to X and remove dyx from L
        X.append(width-y)
        takeout(dyx, L)
        # try the rest (recursively)
        Place(L,X, width)
        # remove width-y from X and put dyx back into L
        X.remove(width-y)
        L.extend(dyx)

    return

## Main, for testing
if __name__ == '__main__':
    # Simulate a partial digest of U23808 with hindIII
    X = [0, 697, 1075, 1811, 5310, 6450, 8298, 8506, 8914]

    # Use a smaller example
    #X = [0, 1, 3, 6, 10]
    dX = deltaX(X)
    PartialDigest(dX)
