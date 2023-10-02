#-----------Ecuación Numerica--------------------
import matplotlib.pyplot as plt
import math

k=9.00*pow(10,9)
densidad=20.0*pow(10,-9)
yi=0.002
qi=densidad*yi
E=[]
sumatoria=0

for x in range(100):
    if x>=2:
        for y in range(32):
            distancia=math.sqrt(((y*yi)**2+x**2))
            trapecio=(2.00*k*qi*y/(distancia**2))*x         #x=cos porque es el eje horizontal del vector r (ver figura)
            sumatoria+=trapecio
        E.append(sumatoria)
        sumatoria=0

x=range(2,100)

#------------------------GRAFICA--------------------------
# Crear la gráfica
plt.figure(figsize=(8, 6))  # Tamaño de la figura

# Agregar los datos a la gráfica
plt.plot(x, E, marker='o')

# Etiquetas de los ejes
plt.xlabel('X (m)')
plt.ylabel('E (N/C)')

# Título de la gráfica
plt.title('Grafico E (N/C) vs X (m) Metodo Numerico')

# Mostrar la gráfica
plt.grid(True)  # Mostrar cuadrícula
plt.show()
