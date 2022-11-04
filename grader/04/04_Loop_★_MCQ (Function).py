def grade_mcq(sol, ans):
    if len(sol) == len(ans):
        score = 0
        for i in range(len(sol)):
            if sol[i] == ans[i]:
                score += 1
        return score
    else:
        return -1

exec(input())