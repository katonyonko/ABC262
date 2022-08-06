import io
import sys

_INPUT = """\
6
4 4 2
1 2
1 3
2 3
3 4
10 10 3
1 2
2 4
1 5
3 6
3 9
4 10
7 8
9 10
5 9
3 4
10 10 10
1 2
2 4
1 5
3 6
3 9
4 10
7 8
9 10
5 9
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M,K=map(int,input().split())
  node=[0]*N
  for _ in range(M):
    U,V=map(int,input().split())
    U-=1; V-=1
    node[U]^=1
    node[V]^=1
  o,e=node.count(1),node.count(0)
  ans=0
  F=[1]
  for i in range(N):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
    I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  for i in range((K+1)//2+1):
    if 2*i<=min(K,o) and K-2*i<=e:
      ans=(ans+F[o]*I[2*i]*I[o-2*i]*F[e]*I[K-2*i]*I[e-K+2*i])%mod
  print(ans)