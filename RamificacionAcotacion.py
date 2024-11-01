from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

class ProblemaOptimizacion:
    def __init__(self):
        # Pedir si es un problema de maximización o minimización
        self.tipo_optimizacion = int(input("Desea maximizar? (-1) o minimizar? (1): "))
        self.problema = LpProblem("Ejemplo_Programacion_Entera", LpMaximize if self.tipo_optimizacion == -1 else LpMinimize)
        self.x = LpVariable('x', lowBound=0, cat='Integer')
        self.y = LpVariable('y', lowBound=0, cat='Integer')
        self._definir_funcion_objetivo()
        self._definir_restricciones()

    def _definir_funcion_objetivo(self):
        # Definir la función objetivo
        coef_x = int(input("Introduzca el coeficiente de x de la funcion objetivo: "))
        coef_y = int(input("Introduzca el coeficiente de y de la funcion objetivo: "))
        self.problema += coef_x * self.x + coef_y * self.y, "Función Objetivo"

    def _definir_restricciones(self):
        # Definir las restricciones
        coef_x1 = int(input("Introduzca el coeficiente de x de la primera restriccion: "))
        coef_y1 = int(input("Introduzca el coeficiente de y de la primera restriccion: "))
        termino_indep1 = int(input("Introduzca el termino independiente de la primera restriccion: "))
        self.problema += coef_x1 * self.x + coef_y1 * self.y <= termino_indep1, "Restriccion_1"

        coef_x2 = int(input("Introduzca el coeficiente de x de la segunda restriccion: "))
        coef_y2 = int(input("Introduzca el coeficiente de y de la segunda restriccion: "))
        termino_indep2 = int(input("Introduzca el termino independiente de la segunda restriccion: "))
        self.problema += coef_x2 * self.x - coef_y2 * self.y <= termino_indep2, "Restriccion_2"

    def resolver(self):
        # Resolver el problema utilizando el solucionador por defecto (CBC)
        self.problema.solve(PULP_CBC_CMD(msg=True))

    def mostrar_resultados(self):
        # Mostrar el estado de la solución
        print(f"Estado de la solución: {LpStatus[self.problema.status]}")
        # Mostrar los valores óptimos de las variables
        print(f"x = {self.x.varValue}")
        print(f"y = {self.y.varValue}")
        # Mostrar el valor óptimo de la función objetivo
        print(f"Valor óptimo de Z = {self.problema.objective.value()}")

# Ejecución del programa
problema = ProblemaOptimizacion()
problema.resolver()
problema.mostrar_resultados()