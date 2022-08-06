import io
import sys

_INPUT = """\
6
2022
2023
3000
3001
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Y=int(input())
  if Y%4==2: print(Y)
  elif Y%4!=3: print(Y//4*4+2)
  else: print(Y//4*4+6)