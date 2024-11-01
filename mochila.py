from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

def resolver_mochila(pesos, valores, capacidad):
    # Paso 1: Crear el problema de maximización
    print("\n--- Paso 1: Crear el problema de maximización ---")
    problema_mochila = LpProblem("Problema_de_la_Mochila", LpMaximize)
    
    # Paso 2: Definir las variables de decisión (0 o 1 para cada objeto)
    print("\n--- Paso 2: Definir las variables de decisión ---")
    n = len(pesos)  # Número de objetos
    x = [LpVariable(f"x_{i+1}", cat='Binary') for i in range(n)]
    print("Variables de decisión definidas (0 = no seleccionado, 1 = seleccionado):")
    for i in range(n):
        print(f"x_{i+1} -> Objeto {i+1}")

    # Paso 3: Definir la función objetivo (maximizar el valor total)
    print("\n--- Paso 3: Definir la función objetivo ---")
    problema_mochila += sum(valores[i] * x[i] for i in range(n)), "Valor_total"
    print("Función objetivo formulada: Maximizar el valor total de los objetos seleccionados.")

    # Paso 4: Definir la restricción de capacidad de la mochila
    print("\n--- Paso 4: Definir la restricción de capacidad ---")
    problema_mochila += sum(pesos[i] * x[i] for i in range(n)) <= capacidad, "Capacidad_mochila"
    print(f"Restricción de capacidad formulada: La suma de los pesos no debe exceder {capacidad} kg.")

    # Paso 5: Resolver el problema
    print("\n--- Paso 5: Resolver el problema ---")
    problema_mochila.solve()
    print(f"Estado de la solución: {LpStatus[problema_mochila.status]}")

    # Paso 6: Mostrar los valores óptimos de las variables (objetos seleccionados)
    print("\n--- Paso 6: Mostrar los objetos seleccionados ---")
    for i in range(n):
        print(f"Objeto {i+1}: {'Seleccionado' if x[i].varValue == 1 else 'No seleccionado'} (Peso: {pesos[i]}, Valor: {valores[i]})")

    # Paso 7: Calcular y mostrar el valor total en la mochila y el peso total
    valor_total = sum(valores[i] * x[i].varValue for i in range(n))
    peso_total = sum(pesos[i] * x[i].varValue for i in range(n))
    print(f"\n--- Paso 7: Resultados finales ---")
    print(f"Valor total en la mochila: {valor_total}")
    print(f"Peso total en la mochila: {peso_total}")

# Datos del problema de la mochila
cantObjetos = int(input("Introduzca la cantidad de objetos: "))
pesos = []
valores = []

for i in range(cantObjetos):
    pesos.append(float(input(f"Introduzca el peso del objeto {i+1}: ")))

for i in range(cantObjetos):
    valores.append(float(input(f"Introduzca el valor del objeto {i+1}: ")))

capacidad = float(input("Introduzca la capacidad de la mochila: "))            # Capacidad máxima de la mochila

# Llamar a la función para resolver el problema
resolver_mochila(pesos, valores, capacidad)
