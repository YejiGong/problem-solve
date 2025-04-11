T, start_time, destination = map(int, input().split())

trains = []
while True:
    try:
        line = input()
        if not line.strip():
            break
        parts = line.split()
        name, times = parts[0], map(int, parts[1:-1])  # 마지막 도착지는 제외
        for time in times:
            trains.append((time, name))
    except EOFError:
        break

trains.sort()

start_index = next((i for i, (time, _) in enumerate(trains) if time >= start_time), 0)
remainder = destination % len(trains)
index = (start_index + remainder - 1) % len(trains)

print(trains[index][1])