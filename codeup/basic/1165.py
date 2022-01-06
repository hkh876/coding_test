# required if ~ else
c_time, score = map(int, input().split())

while True:
  if c_time >= 90:
    break

  score += 1
  c_time += 5

print(score)
