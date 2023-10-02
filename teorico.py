#------------------Ecuación Teorica-------------------
import matplotlib.pyplot as plt
import math

k=9.00*pow(10,9)
permitiVacio=8.85*pow(10,-12)
densidad=20.0*pow(10,-9)
CampoE=[]

for x in range (100):
    if x>=2:
        operacion=(densidad/(2*math.pi*permitiVacio*x))
        CampoE.append(operacion)
        
x=range(2,100)

#--------------------GRAFICA--------------------
# Crear la gráfica
plt.figure(figsize=(8, 6))  # Tamaño de la figura

# Agregar los datos a la gráfica
plt.plot(x, CampoE, marker='o')

# Etiquetas de los ejes
plt.xlabel('X (m)')
plt.ylabel('E (N/C)')

# Título de la gráfica
plt.title('Grafico E (N/C) vs X (m) - Metodo Teorico')

# Mostrar la gráfica
plt.grid(True)  # Mostrar cuadrícula
plt.show()
