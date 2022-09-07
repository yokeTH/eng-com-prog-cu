ans = input()
key = input()
score = 0


if len(ans) == len(key):
    for i in range(len(ans)):
        if ans[i] == key[i]:
            score+=1

    print(score)

else:
    print('Incomplete answer')