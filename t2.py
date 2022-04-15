import math as mt

#Linhas
def line ():
    print (50*"-")

#Código 1

line()
print ("Dê os imaginários e reais para x e y em z = x  +y*i")
line()
x = float(input("De o valor de x: "))
y = float(input("De o valor de y: "))
mod = mt.sqrt((x*x)+(y*y))
line()
print ("Dado o complexo z = {} + ({}i)".format(x, y))
print ("Tem-se que ||z|| = {:.4f}".format(mod))
line()

#código 2

rad = mt.atan(y/x)
dg= (180*rad)/(mt.pi)
print("Argumento Z em radianos = {:.4f} rad".format(rad))
print("Argumento Z em graus = {:.4f} °".format(dg))
line()

#Código 3

print("Sua forma trigonometrica z = {:.4f} [cis({:.4f} °)]".format(mod, dg))
line()

#código 4

print ("Serão realizadas as operações de multiplicação e divisão, insira os valores requisitados.")
line()
z_1 = float(input("Dê  o módulo de Z_1: "))
cs_1 = float(input("Dê a angulação do argumento Z_1, em graus: "))
z_2 = float(input("Dê o módulo de Z_2: "))
cs_2 = float(input("Dê a angulação do argumento Z_2, em graus: "))
z_m = z_1*z_2
cs_m = cs_1 + cs_2
print ("Dado Z_f = Z_1 * Z_2, temos que: ")
print ("Z_f = {:.4f} cis[({:.4f} °)]".format(z_m, cs_m))
line()

#código 5

z_d = z_1/z_2
cs_d = cs_1 - cs_2
print ("Dado Z_f = (Z_1/Z_2), temos que: ")
print ("Z_f = {:.4f} cis[({:.4f} °)]".format(z_d, cs_d))