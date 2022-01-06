import math

# required if ~ else
a,b,c = map(int, input().split())

if a + b <= c:
  result = '삼각형아님'
elif a == b == c:
  result = '정삼각형'
elif math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
  result = '직각삼각형'
elif a == b or b == c or c == a:
  result = '이등변삼각형'
else:
  result = '삼각형'

print(result)