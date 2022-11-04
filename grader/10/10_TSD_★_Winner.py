win = set()
lose = set()

for _ in range(int(input())):
    team = input().split()
    win.add(team[0])
    lose.add(team[1])

print(sorted(list(win-lose)))