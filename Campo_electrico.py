
import matplotlib.pyplot as plt
import math
k=9.00*pow(10,9)
densidad=20.0*pow(10,-9)
yi=0.002
qi=densidad*yi

E=[]
sumatoria=0

#primera ecuacion corregida
for x in range(100):

    if x>=2:
        
        for y in range(32):
            distancia=math.sqrt(((y*yi)**2+x**2))
            trapecio=(2.00*k*qi*y/(distancia**2))*x         #x=cos porque es el eje horizontal del vector r (ver figura)
            sumatoria+=trapecio

        E.append(sumatoria)
        sumatoria=0
print(E[0])
print(E[len(E)-1])
print("------------------------")




#segunda ecuacion que mostró
E1=[]

for x in range(100):

    if x>=2:
        
        for y in range(200):
            distancia=(((y*yi)**2+x**2))
            trapecio=(2.00*k*densidad*x/(pow(distancia,1.5)))         #x=cos porque es el eje horizontal del vector r (ver figura)
            sumatoria+=trapecio

        E1.append(sumatoria)
        sumatoria=0
   



print(E1[0])
print(E1[len(E)-1])
print("------------------------")



#teorica

permitiVacio=8.85*pow(10,-12)
CampoE=[]
for x in range (100):
    if x>=2:
        operacion=(densidad/(2*math.pi*permitiVacio*x))
        CampoE.append(operacion)

    
print(CampoE[0])
print(CampoE[len(CampoE)-1])




x=range(2,100)

# Crear la gráfica
plt.figure(figsize=(8, 6))  # Tamaño de la figura

# Agregar los datos a la gráfica
plt.plot(x, E, marker='o')
plt.plot(x, CampoE, marker='o')



# Etiquetas de los ejes
plt.xlabel('X (m)')
plt.ylabel('E (N/C)')

# Título de la gráfica
plt.title('Grafico E (N/C) vs X (m)')

plt.legend(["Metodo numérico", "Metodo teórico"])

# Mostrar la gráfica
plt.grid(True)  # Mostrar cuadrícula
plt.show()