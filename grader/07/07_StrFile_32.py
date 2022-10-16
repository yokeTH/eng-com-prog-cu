from string import punctuation

def no_lowercase(t):
    for i in t:
        if i.islower():
            return False
    return True

def no_uppercase(t):
    for i in t:
        if i.isupper():
            return False
    return True

def no_number(t):
    for i in t:
        if i.isdigit():
            return False
    return True

def no_symbol(t:str):
    for i in t:
        if i in punctuation:
            return False
    return True

def character_repetition(t):
    for i in 
    return t[0] == t[1] == t[2] == t[3]

def number_sequence(t):
    seq = []
    for i in range(10):
        seq.append(str(i%10) + str((i+1)%10) + str((i+2)%10)+ str((i+3)%10))
        seq.append(str(i%10) + str((i-1)%10) + str((i-2)%10)+ str((i-3)%10))
    print(seq)
    for i in range(len(t)-4):
        if i[t:t+4] in seq:
            return True
    return False
def letter_sequence(t): ...
def keyboard_pattern(t): ...
# #----------------------------- passw = input().strip()
# errors = []
# if len(passw) < 8:
# errors.append("Less than 8 characters")
# if no_lowercase(passw): errors.append("No lowercase letters")
# if no_uppercase(passw):
# ...
# if len(errors) == 0: ...
# else: ...

character_repetition('')