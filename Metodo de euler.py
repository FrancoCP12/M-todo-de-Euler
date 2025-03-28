from matplotlib import pyplot as plt
import math
def ecuacion( ):
    edo = input("Ingrese la ecuación diferencial: ")
    return lambda x, y: eval(edo)

def euler(ecuacion, x, y, paso):
    x_e = [x]
    y_e = [y]

    for _ in range(300): 
        y = y + paso * ecuacion(x, y)
        x += paso
        x_e.append(x)
        y_e.append(y)    
    
    return x_e, y_e



#Ejercicio 1
#paso = 0.05
# print("Paso = 0.05")
# x_e, y_e = euler(ecuacion(), x=1, y=1, paso=0.05)
# x_real = [x/2 for x in range (32)]
# y_real = [math.exp(((x**2)/10)-(1/10)) for x in x_real]

# for i in zip(x_e, y_e):
#     if round(i[0],1) == 1.5:
#         print(f"Posible valor de y= {i[1]}\nReal = {math.exp(((1.5**2)/10)-(1/10))}")

# plt.plot(x_e, y_e, "b")
# plt.plot(x_real, y_real, "r--")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Aproximación con Método de Euler")
# plt.show()


# #Paso = 0.1
# print("Paso = 0.1")
# x_01, y_01 = euler(ecuacion(), x=1, y=1, paso=0.1)
# for i in zip(x_01, y_01):
#     if round(i[0],1) == 1.5:
#         print(f"Posible valor de y= {i[1]}\nReal = {math.exp(((1.5**2)/10)-(1/10))}")
# plt.plot(x_01, y_01, "g")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Aproximación con Método de Euler")
# plt.show()



#Ejercicio 2

x_e, y_e = euler(ecuacion(), x=0, y=0, paso=0.05)
x_real = [x/2 for x in range (32)]
y_real = [5-(5/(math.exp((3*x)))) for x in x_real]
print(f"Valor real:\n{5-(5/(math.exp((3*0.5))))}\nPosibles valores de y:")
for i in zip(x_e, y_e):
    if round(i[0],1) == 0.5:
        print(f"{i[1]}\n")

plt.plot(x_e, y_e, "b")
plt.plot(x_real, y_real, "r--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Aproximación con Método de Euler")
plt.show()

