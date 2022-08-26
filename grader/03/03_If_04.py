number = input()

if len(number)==10 and number[:2] in ['06','09','08']:
    print('Mobile number')
else:
    print('Not a mobile number')