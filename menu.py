print("Calculadora de programacion entera: ")
print("1. Binaria")
print("2. Ramificacion acotacion")
print("3. mochila")
opcion = input("Elija una opcion: ")

if opcion == "1":
    import Binaria
elif opcion == "2":
    import RamificacionAcotacion
elif opcion == "3":
    import mochila
else:
    print("Opcion no valida")