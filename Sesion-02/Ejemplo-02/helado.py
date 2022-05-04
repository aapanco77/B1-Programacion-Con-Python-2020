# 1. Imprimir la lista de opciones en la pantalla
# 2. Leer la opción elegida por el usuario
# 3. En base a la opción del usuario imprimir el valor del helado

menu = (
    (1, "Helado con Oreo"),
    (2, "Helado con M&Ms"),
    (3, "Helado con Fresas"),
    (4, "Helado con Brownie"),
)

print("----------------------")
print(f"{menu[0] [0]}.- {menu[0][1]}")
print(f"{menu[1] [0]}.- {menu[1][1]}")
print(f"{menu[2] [0]}.- {menu[2][1]}")
print(f"{menu[3] [0]}.- {menu[3][1]}")
print("----------------------")


opcion_str = input("Elige el topping: ")
opcion = int(opcion_str)

if opcion == 1:
    precio = 19
elif opcion == 2:
    precio = 25
elif opcion == 3:
    precio = 22
elif opcion == 4:
    precio = 28
else:
    precio = 0

if precio == 0:
    print("El Helado elegido no existe!")
else:
    # print("El valor del helado es ${:.2f} M.N.".format(precio))
    print(f"El valor del helado es ${precio:.2f} M.N.")