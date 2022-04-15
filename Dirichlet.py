''' sendo dy/dx = 3, têm-se que f(x) = y = 3x'''
def line():
    print('-'*20)
f_0 = f_f = 10
line()
n = int(input("Insira o número de pontos desejados, sabendo que serão adicionados dois pontos ao mesmo: "))
n_total = n+2
if n < 0:
    print ("Valor inválido.")

h  = 1/(n+1)
n_local = 0
line()
while n_local<= 1:
    if n_local == 1:
        print ('posição de contorno atingida, programa encerrado.')
        break
    fx = 3*h + f_0
    print ('Dado o valor {:.4f} de h  ponto n = {:.4f}, temos que o valor da derivada de x neste ponto é igual:\n '.format(h,n_local))
    print ('f({:.4f}) = {:.4f}'.format(n_local, fx))
    line()

    f_0 = fx
    n_local += h

    