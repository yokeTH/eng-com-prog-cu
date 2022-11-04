months = ['January','February','March','April','May','June','July','August','September','October','November','December']

P1 = input().split()
P2 = input().split()

if int(P1[3]) > int(P2[3]):
    print(P2[0])
elif int(P1[3]) < int(P2[3]):
    print(P1[0])
else:
    if months.index(P1[1]) > months.index(P2[1]):
        print(P2[0])
    elif months.index(P1[1]) < months.index(P2[1]):
        print(P1[0])
    else:
        if int(P1[2].strip(',')) > int(P2[2].strip(',')):
            print(P2[0])
        elif int(P1[2].strip(',')) < int(P2[2].strip(',')):
            print(P1[0])
        else:
            print(P1[0], P2[0])
