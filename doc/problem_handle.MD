# Handle problem.

## The number is out-of-range
0
-1

### Approach to handle
#### Output something indicating problem
##### Output choices
1.""
2."Out-of-range"
3.None

#### raise exception
##### exception choices
1.Standard exception: [ValueError]
2.(*)Extension of standard exception NumberOutOfRange : ValueError
3.Project-specific exception NumberOutOfRange : Exception