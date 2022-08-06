import io
import sys

_INPUT = """\
6
4
1 3 2 4
10
5 8 2 2 1 6 7 2 9 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(lambda x: int(x)-1,input().split()))
  n=len([1 for i in range(N) if A[i]==i])
  ans=n*(n-1)//2
  m=0
  for i in range(N):
    if A[i]!=i and A[A[i]]==i: m+=1
  print(ans+m//2)