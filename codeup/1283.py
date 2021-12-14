# required for
money = int(input())
day = int(input())
percents = list(map(int, input().split()))

temp_money = money
for percent in percents:
  temp_money = temp_money * (1 + (percent / 100))

result = round(temp_money - money)
print(result)

if result > 0:
  print('good')
elif result == 0:
  print('same')
else:
  print('bad')