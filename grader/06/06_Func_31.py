def read_date():
    return [e for e in input().split()]

def month_to_int(s):
    months = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return months.index(s)

def zodiac(d,m):
    if   d >= 22 and m==3  or d <=21 and m==4  : z = "Aries"
    elif d >= 22 and m==4  or d <=21 and m==5  : z = "Taurus"
    elif d >= 22 and m==5  or d <=21 and m==6  : z = "Gemini"
    elif d >= 22 and m==6  or d <=21 and m==7  : z = "Cancer"
    elif d >= 22 and m==7  or d <=21 and m==8  : z = "Leo"
    elif d >= 22 and m==8  or d <=21 and m==9  : z = "Virgo"
    elif d >= 22 and m==9  or d <=21 and m==10 : z = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1  : z = "Capricorn"
    elif d >= 21 and m==1  or d <=20 and m==2  : z = "Aquarius"
    elif d >= 21 and m==2  or d <=21 and m==3  : z = "Pisces"
    return z

def days_in_feb(y):
    y+=


exec(input())