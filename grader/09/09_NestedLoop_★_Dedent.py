lines = []
for _ in range(int(input())):
    lines.append(input())

for ln in lines:
    dot = 0
    for char in ln:
        if char == '.':
            dot+=1
        else:
            break
    print(ln[int(dot/2):])