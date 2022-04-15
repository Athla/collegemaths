import math

x=float(input("Insira o valor de X:"))
y=float(input("Insira o valor de Y:"))

print(60*"-")

modulo=math.sqrt((x*x)+(y*y))
print("O modulo de Z é:\n ||z|| = ", modulo)
print(60*"-")

if (x>0 and y>0):
    rad = math.atan(y/x)
    graus= (180*rad)/(math.pi)
    print("O argumento principal de Z em radianos é: ",rad)
    print("O argumento principal de Z em graus é: ",graus)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",graus,"°)]")
    print(60*"-")
    
elif (x<0 and y>0):
    rad = math.atan(y/x)
    radf= math.pi + rad
    graus= (180*rad)/(math.pi)
    grauf = 180 + graus
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")

elif (x<0 and y<0):
    rad = math.atan(y/x)
    radf=  math.pi + rad
    graus= (180*rad)/(math.pi)
    grauf = 180 + graus
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")

elif (x>0 and y<0):
    rad = math.atan(y/x)
    radf=  (2*math.pi) + rad
    graus= (180*rad)/(math.pi)
    grauf = 360 + graus
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")
    
elif (x==0 and y<0):
    rad = math.atan(0)
    radf= (3*math.pi)/2
    grauf = 270
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")
elif (x==0 and y>0):
    rad = math.atan(0)
    radf=  math.pi/2
    graus= (180*rad)/(math.pi)
    grauf = 90
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")
elif (x>0 and y==0):
    rad = math.atan(0)
    radf=  0
    graus= (180*rad)/(math.pi)
    grauf = 0
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")
elif (x<0 and y==0):
    rad = math.atan(0)
    radf=  math.pi
    graus= (180*rad)/(math.pi)
    grauf = 180
    print("O argumento principal de Z em radianos é: ",radf)
    print("O argumento principal de Z em graus é: ",grauf)
    print(60*"-")
    print("A forma trigonometrica z = ||z||.cis(θ) é:\n z = ",modulo, "[cis(",grauf,"°)]")
    print(60*"-")

else:
    print("Seu programa será finalizado.")
    quit()
print("ATÉ AQUI O SENTIDO ADOTADO PARA OS ÂNGULOS FOI O SENTIDO ANTI-HORÁRIO (positivo)")
print(60*"-")

z1=float(input("Insira o valor do módulo ||z1||:"))
cis1=float(input("Insira o valor do argumento cis(θ1) em graus:"))
z2=float(input("Insira o valor do módulo ||z2||:"))
cis2=float(input("Insira o valor do argumento cis(θ2) em graus:"))
print(60*"-")

zm= z1*z2
cism= cis1 + cis2
zd= z1/z2
cisd= cis1 - cis2

if (cism >360 and cis1>=0 and cis2>=0 or cism >360 and cis1>=0 and cis2<0 or cism >360 and cis1<0 and cis2>=0):
    q=cism // 360
    sub= q*360
    cis1f= cism - sub
    print("O valor z = z1.z2 é \n z =", z1,".",z2,".[cis(",cis1,"+",cis2,")]\n z = ",zm,".[cis(",cis1f,"°)]")
    print(60*"-")

elif (cism<0 and cis1<0 and cis2<0):
    q=(-cism) // 360
    sub= q*360
    cis1f= cism + sub
    print("O valor z = z1.z2 é \n z =", z1,".",z2,".[cis(",cis1,"+",cis2,")]\n z = ",zm,".[cis(",cis1f,"°)]")
    print(60*"-")
 
elif (cism<0 and cis1>=0 and cis2<0 or cism<0 and cis1<0 and cis2>=0 ):
    q=(-cism) // 360
    sub= q*360
    cis1f= cism + sub
    print("O valor z = z1.z2 é \n z =", z1,".",z2,".[cis(",cis1,"+",cis2,")]\n z = ",zm,".[cis(",cis1f,"°)]")
    print(60*"-")

else:
        print("O valor z = z1.z2 é \n z =", z1,".",z2,".[cis(",cis1,"+",cis2,")]\n z = ",zm,".[cis(",cism,"°)]")
        print(60*"-")

     
if (cisd >360 and cis1>=0 and cis2>=0):
    q=cisd // 360
    sub= q*360
    cis2f= cisd - sub
    print("O valor z = z1.z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cis2f,"°)]")
    print(60*"-")

elif (cisd >360 and cis1<0 and cis2<0 and cis1>cis2):
    q=cisd // 360
    sub= q*360
    cis2f= cisd - sub
    print("O valor z = z1.z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cis2f,"°)]")
    print(60*"-")
 
elif (cisd<-360 and cis1<0 and cis2<0):
    q=(-cisd) // 360
    sub= q*360
    cis2f= cisd + sub
    print("O valor z = z1.z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cis2f,"°)]")
    print(60*"-")

elif (cisd<-360 and cis1<0 and cis2>0):
    q=(-cisd) // 360
    sub= q*360
    cis2f= cisd + sub
    print("O valor z = z1.z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cis2f,"°)]")
    print(60*"-")

elif (cisd<-360 and cis1>0 and cis2>0):
    q=(-cisd) // 360
    sub= q*360
    cis2f= cisd + sub
    print("O valor z = z1.z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cis2f,"°)]")
    print(60*"-")

else:
    print("O valor z = z1/z2 é \n z =", z1,"/",z2,".[cis(",cis1,"-",cis2,")]\n z = ",zd,".[cis(",cisd,"°)]")