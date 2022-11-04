def total(pocket):
    t = 0
    for k in pocket:
        t+= k*pocket[k]
    return t

def take(pocket, money_in):
    for k in money_in:
        if k in sorted(pocket.keys(),reverse=True):
            pocket[k] += money_in[k]
        else:
            pocket[k] = money_in[k]

def pay(pocket, amt):
    if total(pocket) < amt:
        return {}
    else:
        paid = {}
        for k in sorted(pocket.keys(),reverse=True):
            cnt = amt//k
            if cnt > pocket[k]:
                cnt = pocket[k]
            if cnt != 0:
                paid[k] = cnt
            amt -= cnt*k
            pocket[k] -= cnt
            if amt == 0:
                break
        return paid

exec(input().strip())