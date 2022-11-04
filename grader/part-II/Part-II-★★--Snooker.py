a,b = 0,0
balls = {'X':0, 'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
red_cnt = 0
bonus = 0
while red_cnt != 6 or bonus != 6:
    ln = input()
    if red_cnt != 6:
        if ln[0] == '1' and ln[1] == 'R':
            a+=balls[ln[1]]
            red_cnt+=1
            a+=balls[ln[2]]
            if ln[2] == 'R':
                red_cnt+=1
            elif ln[2] != 'X':
                bonus+=1
        elif ln[0] == '2' and ln[1] == 'R':
            b+=balls[ln[1]]
            red_cnt+=1
            b+=balls[ln[2]]
            if ln[2] == 'R':
                red_cnt+=1
            elif ln[2] != 'X':
                bonus+=1
    else:
        if ln[0] == '1':
            a+=balls[ln[1]]
        else:
            b+=balls[ln[1]]
        if balls[ln[1]] != 'X':
                bonus+=1
    print(red_cnt, bonus)