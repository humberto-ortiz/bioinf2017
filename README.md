# partial.py

Functions for computing properties of simulated partial digests of DNA.

I have provided 3 functions: `deltaX`, `BruteForcePDP` and
`AnotherBruteForcePDP`. `deltaX(sites)` will compute the sizes of all the
possible fragments of a partial digest of a sequence given a list of
restriction sites.

```
>>> from partial import *
>>> deltaX([0, 1, 3, 6, 10])
[1, 2, 3, 3, 4, 5, 6, 7, 9, 10]
```

`BruteForcePDP(L, n)` computes the list of restriction sites if given a
valid list of fragment sizes.

```
>>> BruteForcePDP([1, 2, 3, 3, 4, 5, 6, 7, 9, 10], 5)
[0, 1, 3, 6, 10]
```

The function `AnotherBruteForcePDP` does the same as the first, but
iterates over the frangments sizes in `L` instead of over all the
integers. It's much faster when the `max(L)` is large. For example

```
>>> from partial import *
>>> X=[0,1,3,6,500,3000]
>>> L = deltaX(X)
>>> BruteForcePDP(L,6)
[0, 1, 3, 6, 500, 3000]
```

Takes 47 seconds on my computer, but `AnotherBruteForcePDP` only
takes 0.001 seconds.
