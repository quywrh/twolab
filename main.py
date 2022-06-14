import math
if __name__ == "__main__":
    a = float(input('Введите коэф. а:'))
    b = float(input('Введите коэф. b:'))
    c = float(input('Введите коэф. c:'))
    d = b**2-4*a*c
    if d >= 0:
        if d == 0:
            x = -b/2*a
            print('x =', x)
        else:
            x1 = (-b-math.sqrt(d))/2*a
            x2 = (-b+math.sqrt(d))/2*a
            print('x1 =', x1, 'x2 =', x2)
    else:
        print('Отрицательный дискриминант')
