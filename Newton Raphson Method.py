import math as mt
#Função 
def func(x):
    return 25*x**2 +mt.log(x)
#Função derivada
def funcDeriv(x):
    return 50*x + (1/x)
#Método genérico
def newt(x0):
    return (x0) - ((func(x0)/funcDeriv(x0)))
#error
def erro(x1,x0):
    return (abs(x1 - x0)/abs(x1))
#inputs
condition = 0
x0 = float(input('Initial number to start (please use dot, not comma): '))
k = 0
step = 0
e = float(input("Maximum tolerable error (please use dot, not comma): "))
n = int(input('Max number of steps: '))
if funcDeriv(x0) == 0.0:
    print ("invalid derivate")
#repetição
while condition == 0:
    
    x1 = newt(x0)
    print ('Iteration {} \tf(x{})= {:.4f}'.format(step,k, x1))
    error = erro(x1, x0)
    if error < e:
        print ('Number of iterations realized {} \t Zero of the function = {:.4f} '.format(k,x1))
        condition = 1
        break
    elif error > e:
        x0 = x1
        step = step + 1
        k = k +1
        x1 = newt(x0)
        error = erro(x1, x0)
    else:
        print ('Number of iterations exceeded.')
        break
    
       
            
        
    

            


