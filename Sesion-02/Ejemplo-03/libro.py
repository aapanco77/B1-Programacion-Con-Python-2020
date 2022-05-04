#esto es una Tupla
libros = (
    "El señor de los anillos",
    "El árte de la guerra",
    "Triptofanito",
    "La Meta",
    "El árte de la guerra",
    "La Meta",
)

# Eliminando duplicados
c_libros = set(libros)

# Ordenando
l_libros = list(c_libros)
l_libros.sort()

# Uniendo lineas de texto, en una sola línea de texto:
texto = "\n".join(l_libros)

# Imprimiendo la lista final
print(texto)