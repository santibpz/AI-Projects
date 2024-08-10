# Santiago Benitez Perez
# A01782813

'''
    Regresion lineal simple (de una variable)
'''

import matplotlib.pyplot as plt

# Funcion Gradiente Descendiente
def gradienteDescendiente(X,Y,theta,alpha=0.01,iteraciones=1500):
    # numero de datos
    m = len(X)

    # valores de theta
    current_theta0, current_theta1 = theta

    # arreglo para calcular costos
    costs = []

    # iterar hasta encontrar los valores de theta0 y theta1 que minimizan el error total
    for i in range(iteraciones):
        # variable que almacena la suma del error
        e_sum = 0
        # suma los errores
        for i in range(1, m + 1):
            e_sum += (current_theta0 + current_theta1 * X[i-1]) - Y[i-1]
        
        # almacena temporalmente la variable del nuevo valor de theta 0 para poder calcular de manera correcta el valor del theta 1
        temp_theta0 = current_theta0 - alpha*(e_sum/m)

        # iguala e_sum a 0
        e_sum = 0
        #suma los errores
        for i in range(1, m + 1):
            e_sum += ((current_theta0 + current_theta1 * X[i-1]) - Y[i-1])*X[i-1]
        
        temp_theta1 = current_theta1 - alpha*(e_sum/m)

        # Actualiza los valores de theta 0 y theta 1
        current_theta0 = temp_theta0 
        current_theta1 = temp_theta1

        # calcula el costo con estos valores de theta 0 y theta 1
        cost = calculaCosto(X,Y,[current_theta0, current_theta1])
        costs.append(cost)
    
    # regresa los valores finales de theta 0 y theta 1
    return [current_theta0, current_theta1], costs

# Funcion para graficar datos
def graficaDatos(X,Y,theta):
    # Crea el gráfico
    plt.scatter(X, Y)

    # arreglo para calcular los valores de y en base a nuestra función de hipótesis y = theta0 + theta1*x
    y = []
    # calcula los valores de y
    for i in range(len(X)):
        y_temp = theta[0] + theta[1]*X[i]
        y.append(y_temp)

    # grafica la función hipótesis
    plt.plot(X, y, color="red")

    # Añade etiquetas y título
    plt.xlabel('Cantidad de Población')
    plt.ylabel('Ganancias del carrito')
    plt.title('Gráfico de Población VS Ganancia')
    plt.grid(True)

    # Muestra el gráfico
    plt.show()

# Funcion para calcular costo
def calculaCosto(X,Y, theta):
    # número de datos
    m = len(X)

    # valores de theta
    theta0, theta1 = theta

    # variable para almacenar la suma del error 
    e_sum = 0

    # suma los errores
    for i in range(1, m+1):
        e_sum += ((theta0 + theta1*X[i-1]) - Y[i-1])**2
    
    #regresa el costo con los valores de theta 0 y theta 1
    return e_sum/(2*m)

# Función para graficar el Costo
def graficaCosto(costs):
    # grafica el costo
    plt.plot(costs)
    plt.title('Costo')
    plt.show()

# Funcion para leer archivo
def leer_datos_archivo(filename):
   # Arreglos X y Y para almacenar la informacion
    X = []
    Y = []

    with open(filename, 'r') as file:
        for line in file:
            # Elimina los espacios en blanco y divide la línea en elementos
            elements = line.strip().split(',')
            # Almacena el primer elemento en X y el segundo en Y
            X.append(float(elements[0]))  # Se convierte a float por si los datos son números
            Y.append(float(elements[1]))  # Se convierte a float por si los datos son números
    
    return X, Y

# Función main
def main():
    # lee el archivo
    X, Y = leer_datos_archivo("ex1data1.txt")

    # inicializa vector theta en Ceros
    theta = [0,0] 

    #cost inicial
    i_cost = calculaCosto(X,Y,theta)
    print(f"Costo inicial es: {i_cost} con vector inicial theta [{theta[0]},{theta[1]}]")

    # vector final y costos
    theta, costs = gradienteDescendiente(X, Y, [0,0])

    # costo final
    f_cost = calculaCosto(X,Y,theta)
    print(f"Costo final es: {f_cost} con vector final theta [{theta[0]},{theta[1]}]")

    # grafica datos
    graficaDatos(X,Y, theta)

    # grafica costo
    graficaCosto(costs[1:])
   
# invocación de la funcion main
main()