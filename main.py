def DividedDifferences(x, y):
    delta = [item for item in y]
    cf = []
    cf.append(y[0])
    n = len(y)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            number = delta[j + 1] - delta[j]
            denom = x[j + 1 + i] - x[j]
            delta[j] = number / denom
            print(f'({delta[j + 1]} - {delta[j]}) / ({x[j + 1 + i]} - {x[j]}) = {delta[j]}')
        cf.append(delta[0])
    return cf


def Equation(x, cf):
    n = len(x)
    equation = ''
    for i in range(n):
        equation += f'{cf[i]:+}' + '*'.join([f"(x{-xj:+})" for j, xj, in enumerate(x) if j < i])
    return equation


def Menu(x, y):
    cont = True
    valid = True
    while cont:
        x.append(float(input('x = ')))
        y.append(float(input('f(x) = ')))
        while valid:
            resp = input('Quer continuar[S/N]? ').upper()
            if(resp[0] == 'N' or resp[0] == 'S'):
                valid = False
                if(resp[0] == 'N'):
                    cont = False
            else:
                print('\033[31mErro!!! Por favor digite S/N\033[m')
        valid = True




x = []
y = []
Menu(x, y)



cf = DividedDifferences(x, y)
print(cf)

equation = Equation(x, cf)
print(equation)








