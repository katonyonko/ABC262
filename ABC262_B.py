import io
import sys

_INPUT = """\
6
5 6
1 5
4 5
2 3
1 4
3 5
2 5
3 1
1 2
7 10
1 7
5 7
2 5
3 6
4 7
1 5
2 4
1 3
1 6
2 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  for _ in range(M):
    U,V=map(int,input().split())
    U-=1; V-=1
    G[U].add(V)
    G[V].add(U)
  ans=0
  for i in range(N):
    for j in range(i+1,N):
      if j in G[i]:
        for k in range(j+1,N):
          if k in G[j] and i in G[k]: ans+=1
  print(ans)