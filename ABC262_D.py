import io
import sys

_INPUT = """\
6
3
2 6 2
5
5 5 5 5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  A=list(map(int,input().split()))
  ans=0
  for i in range(1,N+1): #いくつ選ぶか
    dp=[[0]*i for _ in range(i+1)]
    dp[0][0]=1
    for j in range(N):
      for k in reversed(range(i)):
        for l in range(i):
          dp[k+1][(l+A[j])%i]=(dp[k+1][(l+A[j])%i]+dp[k][l])%mod
    ans=(ans+dp[-1][0])%mod
  print(ans)