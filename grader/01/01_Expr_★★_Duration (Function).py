def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
    return  ('0'+str(h))[-2:] + ':' + \
            ('0'+str(m))[-2:] + ':' + \
            ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return h*3600 + m*60 + s

def to_hms(s):
    h = s//3600
    s -= h*3600
    m = s//60
    s -= m*60
    return h,m,s

def diff(h1,m1,s1,h2,m2,s2):
    t1 = to_sec(h1,m1,s1)
    t2 = to_sec(h2,m2,s2)
    dt = t2 - t1
    dh = (dt // (60*60)) % 24
    dt -= (dh * 60*60)
    dm = (dt // 60) % 60
    dt -= dm*60
    ds = dt % 60
    return dh,dm,dt

def main():
    hms_start = str2hms(input())
    hms_end = str2hms(input())
    dh,dm,ds = diff(hms_start[0],hms_start[1],hms_start[2],hms_end[0],hms_end[1],hms_end[2])
    print(hms2str(dh,dm,ds))

exec(input())