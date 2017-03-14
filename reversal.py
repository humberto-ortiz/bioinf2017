#!/bin/env python3
# Reversal Sorting examples from Chapter 5
# Copyright 2017 - Humberto Ortiz-Zuazaga

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
