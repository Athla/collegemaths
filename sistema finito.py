''' f(x) = [ln(x)]^(x+3)'''
import math
def f_x (x):
    func = (math.log(x, math.exp(1)))**(x+3)
    return func
def line():
    print(25*'-')
    return
line()

h = float(input("De o valor de h: "))
x = float(input("Dê o valor de x: "))
line()
print('MENU')
line()
print ('1-Diferença finita atrasada \n2-Diferença finita centrada \n3-Diferença finita avançada \n4-Sair')
esc = int(input("Escolha uma opção das mostradas acima: "))
line()
while esc != 4:
    if esc ==1:
        dif = (f_x(x) - f_x(x-h))/h      
        print ("Dada a função f(x) = [ln(x)]^(x+3)], temos que sua derivada, pelo método das diferenças finitas atrasadas é: ")
        print ("f'({}) = {:.6f}".format(x, dif))
        print ('1-Diferença finita atrasada \n2-Diferença finita centrada \n3-Diferença finita avançada \n4-Sair')
        esc = int(input("Escolha uma opção das mostradas acima: "))
        line()
    if esc == 2:
        dif = (f_x(x+h) - f_x(x-h))/(2*h)
        print ("Dada a função f(x) = [ln(x)]^(x+3)], temos que sua derivada, pelo método das diferenças finitas centradas é: ")
        print ("f'({}) = {:.6f}".format(x, dif))
        line()
        print ('1-Diferença finita atrasada \n2-Diferença finita centrada \n3-Diferença finita avançada \n4-Sair')
        esc = int(input("Escolha uma opção das mostradas acima: "))
        line()
    if esc == 3:
        dif = (f_x(x+h) - f_x(x))/(h)
        print ("Dada a função f(x) = [ln(x)]^(x+3)], temos que sua derivada, pelo método das diferenças finitas avançadas é: ")
        print ("f'({}) = {:.6f}".format(x, dif))
        line()
        print ('1-Diferença finita atrasada \n2-Diferença finita centrada \n3-Diferença finita avançada \n4-Sair')
        esc = int(input("Escolha uma opção das mostradas acima: "))
        line()
    else:
        print ("entrada inválida, programa encerrado.")
        break
if esc ==4:
    print ("programa encerrado.")