import math
def line():
    return print (35*"-")

line()
print ("As seguintes operações serão exibidas em série: ")
print ("1 - e^z \n2 - sin(z) \n3 - cos(z) \n4 - tg(z)")
line()
x = float(input("De o valor da parte real z: "))
y = float(input("De o valor da parte imaginaria de z: "))
line()

#Exercício 01 — exponencial complexa
print ('dado o complexo z = {}+{}i, temos que e^z e igual a:'.format(x,y))
print('e^z = e ^{}  * cis [{}], para o argumento em radianos'.format(x,y))   
arg_deg = (y*180)/(math.pi)
print ("e^z = e^{} * cis[{:.4f}], para o argumento em graus.".format(x, arg_deg))

#Exercícios 02 — seno complexo
print ("dado o complexo z = {} + ({})i, temos que sen(z) e igual a".format(x,y))
e_s1 =(( (math.exp(-y) + math.exp(y)) * math.sin(x))/2)
e_s2 =(( (math.exp(-y) - math.exp(y)) * math.cos(x))/2)
seno = e_s1 - e_s2

#Exercício 03 — cosseno
print ("sen (z) = sen ({} + ({})i) = {:.4f}i".format(x,y, seno))
e_c1 = (( (math.exp(-y) - math.exp(y)) * math.sin(x))/2)
e_c2 = (( (math.exp(-y) + math.exp(y)) * math.cos(x))/2)
cos = e_c1 + e_c2
print ("cos (z) = cos({} + ({})i) = {:.4f} ".format(x,y,cos))

#Exercício 04 — tangente
print ("dado o complexo z = {} + ({})i, temos que tan(z) e igual a: ".format(x,y))
tg = (seno)/(cos)
print ("tg (z) = tg({} + ({})i) = {:.4f}i".format(x,y,tg))