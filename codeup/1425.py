n, c = map(int, input().split())
heights = list(map(int, input().split()))

sorted_heights = sorted(heights)
count = 0
for height in sorted_heights:
  count += 1
  print(height, end=' ')
  if count == c:
    count = 0
    print()
