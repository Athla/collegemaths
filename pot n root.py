#line
def line ():
    print (35*"-")
#potencia
def pot (z, n, arg):
    print ("Dado z = ||{:.4f}|| . cis({} °), temos que z^{} equivale a:".format(abs(z), arg, n))
    arg2 = arg *n
    if arg2 > 360:
        arg = arg2 - 360
    if arg2 < -360:
        arg = arg2 + 360
    print ("z = z^{} = ||{:.4f}|| . cis({} °)".format(n, pow(abs(z),n), arg*n ))
    
#root
def root (z, arg, n):
    print ("Dado z = ||{:.4f}|| . cis({} °), temos que a raiz {} de z equivale a:".format(abs(z), arg, n))
    k = 1 
    for k in range (0, n, 1):
        line()
        z = abs(z)
        arg_f = ((arg + (k*360))/n)
        if (arg_f > 360):
            quo = arg_f // 360
            correc = quo * 360
            arg_ff = arg_f - correc
            print ("Para k =", k)
            print ("w",k,"=", z**(1/n), "cis(", arg_ff,"°)")
            line()
        elif (arg_f < -360):
            quo = (-arg_f) // 360
            correc = quo * 360
            arg_ff = arg_f + correc
            print ("Para k =", k)
            print ("w",k,"=", z**(1/n), "cis(", arg_ff,"°)")
            line()
            
        print ("Para k =", k)
        print ("w",k,"=", z**(1/n), "cis(", arg_f,"°)")
        line ()
#exe
line()
z = float(input("De o modulo de z: "))
arg = float(input("De o argumento, em graus: "))
line()
print ("1 - Descobrir a potencia de z^n. \n2 - Descobrir a raiz enesima de z")
ch = int(input("Escolha uma opção: "))
if ch == 1:
    n = int(input("De o valor utilizado na potencia: "))
    if n < 0:
        print ("Numero invalido.")
    else:
        pot (z, n, arg)
elif ch == 2:
    n = int(input("De o valor utilizado para a raiz enesima: "))
    if n < 0:
        print ("Numero invalido.")
    else:
        root(z, arg, n)

else:
    print ("Entrada invalida.")
        