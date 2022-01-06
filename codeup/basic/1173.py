# required if ~ else
hour, min = map(int, input().split())

if min - 30 < 0:
  if hour == 0:
    hour = 23
  else:
    hour -= 1

  min += 60 - 30
else:
  min -= 30

print(f'{hour} {min}')