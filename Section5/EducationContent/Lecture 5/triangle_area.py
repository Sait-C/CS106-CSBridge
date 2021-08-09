b= float(input('Enter base length:  '))
h= float(input('Enter height:  '))
print('')
if b<=0:
    print('Base must be positive!')
else:
    if h<=0:
        print('Height must be positive!')
    else:
        area= b*h/2
        print('Area of triangle with b=',b,'and h=',h,'is',area)
