# [Single Number](https://leetcode.com/problems/single-number/)
## Description

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Solution

### Solution 1

배열을 하나 만들어서 원래 배열의 원소들을 하나씩 옮긴다.
옮길 때 이미 있는 원소이면 그 원소를 삭제하고
없는 원소이면 추가한다.
그러면 마지막 남게되는 원소는 1번만 나온 원소가 된다. 
(엄밀히 말하면 홀수번 나온 원소이겠지만 여기서는 한 원소를 빼고는 모두 두 번 나온다고 했으므로) 

### Solution 2

배열에서 중복된 요소를 제거하고 그 수를 모두 합하고 두 배 한다.
위 수에서 원본 배열의 합을 뺀다. 

예를 들어, [ 1, 1, 2 ] 배열이 있다면,

( 1 + 2 ) * 2 - (1 + 1 + 2) = 2

다음과 같이 나오게 된다.

- [1, 2] [1, 2]
- [1, 1, 2]

이 두개를 비교해보면 이해가 간다.
