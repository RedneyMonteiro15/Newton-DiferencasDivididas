#função que calcula as doferenças dividivas
def DividedDifferences(x, y, valid):
    delta = [item for item in y] #copia os valores das imagens para a lista delta
    cf = [] #cria a lista dos coeficiente vazia
    cf.append(y[0]) #adiciona a imagem do primeiro objeto (x1)
    n = len(y)
    # vai percorrer até o total do polimonio menos um
    for i in range(n - 1): #se sabemos quatro ponto, vamos obter um polimonio do 3ºgrau
        if(valid): #se for para mostrar
            print('-' * 20)
            print(f'\033[7;34;40mOrdem {i + 1}\033[m')
        for j in range(n - 1 - i): #em cada iteração (ordem), calcular as diferenças
            number = delta[j + 1] - delta[j] #calcula o numerador
            denom = x[j + 1 + i] - x[j] #calcula o denominador
            delta[j] = number / denom # calcula a diferença
            if (valid):
                print(f'({delta[j + 1]} - {delta[j]}) / ({x[j + 1 + i]} - {x[j]}) = {delta[j]}')
        cf.append(delta[0]) #adiciona apenas o primeiro valor da ordem que é o um coeficiente do polimonio interpolador
    return cf #retorna os operadores


#função que retorna a expressão do polimonio interpolador
def Equation(x, cf):
    n = len(x)
    equation = '' #começa a expressão vazia
    for i in range(n):
        #em cada valor de xn, adiciona a equação o sinal, seguido do sinal de multiplicação caso tiver um numero ainda colocar na expressão
        equation += f'{cf[i]:+}' + '*'.join([f"(x{-xj:+})" for j, xj, in enumerate(x) if j < i])
    return equation #retorna a expressão


def Menu(x, y):
    cont = True
    valid = True
    while cont:
        x.append(float(input('x = '))) #adiciona o valor de x, recebido na lista
        y.append(float(input('f(x) = '))) #adiciona o valor de y, recebido na lista
        while valid: #enquanto for valido
            resp = input('Quer continuar[S/N]? ').upper() #pergunta-mos e valida-mos
            if(resp[0] == 'N' or resp[0] == 'S'): # se for um opção valida
                valid = False #falso, para sair do ciclo(perguntar se quer continuar)
                if(resp[0] == 'N'): #se for não, sai do ciclo, o utilizador não vai digitar mais numeros
                    cont = False
            else: # se não for vália
                print('\033[31mErro!!! Por favor digite S/N\033[m')
        valid = True
    while valid:
        resp = input('Mostrar as diferenças dividivas[S/N]? ').upper() #perguntar se que mostar as diferenças divididas
        if (resp[0] == 'N' or resp[0] == 'S'): #se for uma opção válida
            if(resp[0] == 'N'): #se for não, retorna falso
                return False
            else: #se for sim, retorna verdadeiro
                return True
        else: #se não for
            print('\033[31mErro!!! Por favor digite S/N\033[m')




#listas dos valore xx' e yy'
x = []
y = []

#chama a função que calcula as diferenças divididas
cf = DividedDifferences(x, y, Menu(x, y))

#chame a função que retorna a expressão do polimonio
equation = Equation(x, cf)
print(f'\n\033[32mp(x) = {equation}\033[m') #mostra a equação









