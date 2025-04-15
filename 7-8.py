with open('coord.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
points = []

for line in lines[1:n + 1]:
    x, y = map(int, line.strip().split())
    points.append((x, y))

points.sort(key=lambda point: (point[0], point[1]))

for point in points:
    print(point[0], point[1])
