h= int(input('What hour is it?  '))
if h>=0 and h<5 or h>=21 and h<24:
    print('Good night')
elif h>=5 and h<12:
    print('Good morning')
elif h>=12 and h<18:
    print('Good afternoon')
elif h>=18 and h<21:
    print('Good evening')
else:
    print('Are you living on Mars???') 