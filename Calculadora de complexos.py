#Espaçamento
def line():
    print(60*"—")
#conjugado
def conj (x,y):
    print ("Dado o complexo z = {}+{}i, temos que seu conjugado é z = {}{}i.".format(x, y, x, -y))
#soma de z1 e z2
def soma (x1,x2,y1,y2):
    print ("z1 = {} + ({}i) e z2 = {} + ({}i)".format(x1,y1,x2,y2))
    print ("temos que sua soma é igual a: ")
    print ("z3 = {} + ({}i)".format(x1+x2, y1+y2))
#subtração
def sub (x1,x2,y1,y2):
    print ("z1 = {} +({}i) e z2 = {}+({}i)".format(x1,y1,x2,y2))
    print ("temos que sua soma é igual a: ")
    print ("z3 = {} +({}i)".format(x1-x2, y1-y2))
#multiplicação
def mult (x1,x2,y1,y2):
    print ("z1 = {}+({}i) e z2 = {} +({}i)".format(x1,y1,x2,y2))
    print ("temos que sua multiplicação é igual a: ")
    print ("z3 = {:.4f} + ({:.4f}i)".format( ((x1*x2) - (y1*y2)), ((x1 * y2 )+( x2* y1 )) ))
#divisão
def div (x1,x2,y1,y2):
    print ("z1 = {} {} e z2 = {} {}".format(x1,x2,y1,y2))
    print ("temos que a divisão de z1 por z2 é igual a:")    
    print ("z3 = {:.4f} + ({:.4f}i)".format( ((x1 * x2)+( y1 * y2))/((x2**2)+(y2**2)) , ((x2 * y1)-(x1 * y2))/(x2**2+y2**2)) )

line()
print (" 1 - Conjugar o complexo \n 2 - Somatória de dos complexos z1 e z2, resultando em z.")
print (" 3 - Subtração de z1 e z2, resultando em z. \n 4 - Multiplicação dos complexos z1 e z2, resultando em z.")
print (" 5 - Divisão dos complexos z1 e z2, resultando em z.")
line()

esc = str(input("Selocione a operação que deseja fazer digitando o número correspondente: "))

#conjugado
if esc == "1":
    x = float(input("Dê o valor de x: "))
    y = float(input("Dê o valor de y: "))
    conj(x, y)
#soma
elif esc == "2":
    x1 = float(input("Dê o valor de x1: "))
    y1 = float(input("Dê o valor de y1: "))
    x2 = float(input ("dê o valor de x2: "))
    y2 = float(input ('Dê o valor de y2: '))
    soma(x1, x2, y1, y2)
    line()
#subtração
elif esc == "3":
    x1 = float(input("Dê o valor de x1: ")) 
    y1 = float(input("Dê o valor de y1: "))
    x2 = float(input ("dê o valor de x2: "))
    y2 = float(input ('Dê o valor de y2: '))
    sub(x1, x2, y1, y2)
    line()
#multiplicação
elif esc == "4":
    x1 = float(input("Dê o valor de x1: "))
    y1 = float(input("Dê o valor de y1: "))
    x2 = float(input ("dê o valor de x2: "))
    y2 = float(input ('Dê o valor de y2: '))  
    mult(x1, x2, y1, y2)
    line()
#divisão
elif esc == "5":
    x1 = float(input("Dê o valor de x1: "))
    y1 = float(input("Dê o valor de y1: "))
    x2 = float(input ("dê o valor de x2: "))
    y2 = float(input ('Dê o valor de y2: '))
    div(x1, x2, y1, y2)
    line()
else:
    print ("Entrada incorreta, programa terminado.")
    line()