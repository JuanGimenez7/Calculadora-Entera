from pulp import LpMinimize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

class OptimizacionEstaciones:
    def __init__(self, distancias, umbral_distancia=40):
        """
        Inicializa el problema de optimización para la construcción mínima de estaciones.
        
        :param distancias: Matriz de distancias entre ciudades (una lista de listas).
        :param umbral_distancia: Distancia máxima permitida entre una ciudad y una estación (default=40).
        """
        self.distancias = distancias
        self.umbral_distancia = umbral_distancia
        self.num_ciudades = len(distancias)
        self.problema = LpProblem("Minimizar_Numero_Estaciones", LpMinimize)
        self.variables = [LpVariable(f"x{i}", cat='Binary') for i in range(self.num_ciudades)]
        self._definir_funcion_objetivo()
        self._definir_restricciones()

    def _definir_funcion_objetivo(self):
        # La función objetivo es minimizar la suma de las estaciones instaladas
        self.problema += sum(self.variables), "Minimizar_Estaciones"

    def _definir_restricciones(self):
        # Para cada ciudad, se asegura que haya al menos una estación en un radio de 40 minutos
        for i in range(self.num_ciudades):
            # Crear una lista de variables de ciudades que cumplen la restricción de distancia
            ciudades_cercanas = [
                self.variables[j] for j in range(self.num_ciudades) if self.distancias[i][j] <= self.umbral_distancia
            ]
            # Asegurar que al menos una estación esté en el rango de cada ciudad
            self.problema += sum(ciudades_cercanas) >= 1, f"Restriccion_Ciudad_{i}"

    def resolver(self):
        # Resolver el problema de optimización
        self.problema.solve(PULP_CBC_CMD(msg=True))

    def mostrar_resultados(self):
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.problema.status]}")
        # Mostrar las ciudades en las que se instalarán estaciones
        for i, var in enumerate(self.variables):
            print(f"Ciudad {i+1}: {'Estación' if var.varValue == 1 else 'Sin estación'}")
        # Mostrar el número mínimo de estaciones
        print(f"Número mínimo de estaciones necesarias: {sum(var.varValue for var in self.variables)}")

def solicitar_matriz_distancias(num_ciudades):
    """
    Solicita al usuario que ingrese la distancia entre cada par de ciudades para crear la matriz de distancias.
    
    :param num_ciudades: Número total de ciudades
    :return: Matriz de distancias entre las ciudades (lista de listas)
    """
    distancias = []
    print(f"Ingrese las distancias entre cada par de ciudades (en minutos):")
    for i in range(num_ciudades):
        fila = []
        for j in range(num_ciudades):
            if i == j:
                fila.append(0)  # La distancia de una ciudad a sí misma es 0
            else:
                distancia = int(input(f"Distancia de la ciudad {i+1} a la ciudad {j+1}: "))
                fila.append(distancia)
        distancias.append(fila)
    return distancias

# Ejemplo de uso

num_ciudades = 10  # Número de ciudades en el problema
distancias = solicitar_matriz_distancias(num_ciudades)

problema = OptimizacionEstaciones(distancias)
problema.resolver()
problema.mostrar_resultados()
