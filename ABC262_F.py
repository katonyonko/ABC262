import io
import sys

_INPUT = """\
6
5 3
4 5 2 3 1
3 0
3 2 1
15 10
12 10 7 2 8 11 9 1 6 14 3 15 13 5 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  P=list(map(int,input().split()))
  