print('welcom to bakery , enter your name and answer with "yes" or "no"')
name = str(input('what is your name ? '))
coast = 10000
x = 0
while x < 6:
    x += 1
    if x == 1:
        a = str(input('do you want taftoon ? '))
        if a == 'no':
            coast -= 1000
        elif a == 'yes':
            a = int(input('how many ? '))
            coast += int(a-1) * 1000
        else:
            print('wrong please enter "yes" or "no"')
            break
    elif x == 2:
        b = str(input('do you want barbary ? '))
        if b == 'no':
            coast -= 2000
        elif b == 'yes':
            b = int(input('how many ? '))
            coast += int(b-1) * 2000
        else:
            print('wrong please enter "yes" or "no"')
            break
    elif x == 3:
        c = str(input('do you want lavash ? '))
        if c == 'no':
            coast -= 1500
        elif c == 'yes':
            c = int(input('how many ? '))
            coast += int(c-1) * 1500
        else:
            print('wrong please enter "yes" or "no"')
            break
    elif x == 4:
        d = str(input('do you want toast ? '))
        if d == 'no':
            coast -= 3000
        elif d == 'yes':
            d = int(input('how many ? '))
            coast += int(d-1) * 3000
        else:
            print('wrong please enter "yes" or "no"')
            break
    elif x == 5:
        e = str(input('do you want sangak ? '))
        if e == 'no':
            coast-= 2500
        elif e == 'yes':
            e = int(input('how many ? '))
            coast += int(e-1) * 2500
        else:
            print('wrong please enter "yes" or "no"')
            break
print(f'here is your coast {name}')

print(coast)

print('input something to finish')

input()
    
        
