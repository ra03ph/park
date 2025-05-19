a = 1
b = 1
c = 2
d = 3
e = 3

vars = [a, b, c, d, e]
checked = []

for i in range(len(vars)):
    count = 0
    if i in checked:
        continue
    for j in range(len(vars)):
        if vars[i] is vars[j]:
            count += 1
    print(f"{vars[i]} : {count}개")
    checked.extend([j for j in range(len(vars)) if vars[i] is vars[j]])
