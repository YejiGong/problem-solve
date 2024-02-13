n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

start = data[0]
count = 1

for location in data[1:]:
  if location in range(start, start+l):
    continue
  else:
    start = location
    count += 1

print(count)