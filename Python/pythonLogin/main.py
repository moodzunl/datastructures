import os
import time
import re

# Definir una lista para almacenar los IDs de cuenta existentes
ids_existentes = []


# Leer el archivo de texto y agregar los IDs existentes a la lista
with open("credenciales.txt", "r") as file:
    for line in file:
        fields = line.strip().split(":")
        ids_existentes.append(int(fields[0]))


# Definir una función para crear una nueva cuenta
def crear_cuenta():
    global ids_existentes

    # Solicitar al usuario que ingrese un nombre de usuario y contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña (debe tener al menos 8 caracteres y símbolos especiales): ")

    # Validar la contraseña
    if len(password) != 8 or not re.search("[!@#$%^&*()_+-=]", password):
        print("Contraseña no válida. La contraseña de ser de 8 caracteres y símbolos especiales.")
        print('----------------------------')
        input('Presiona enter para continuar. . . ')
        return

    # Generar un nuevo ID único para la cuenta
    id_cuenta = max(ids_existentes) + 1 if ids_existentes else 1
    while id_cuenta in ids_existentes:
        id_cuenta += 1

    # Guardar las credenciales de inicio de sesión y el ID de la cuenta en el archivo de texto
    with open("credenciales.txt", "a") as file:
        file.write(f"{id_cuenta}:{username}:{password}\n")
    print(f"¡Cuenta creada con éxito! Su nombre de usuario es {username} y su ID de cuenta es {id_cuenta}")
    print('----------------------------')
    input('Presiona enter para continuar. . . ')
    
    # Agregar el nuevo ID a la lista de IDs existentes
    ids_existentes.append(id_cuenta)


# Inicia sesión en una cuenta existente
def inicio_sesion():
    # Solicita al usuario que ingrese un nombre de usuario y una contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Verifica si el nombre de usuario y la contraseña coinciden
    try:
        with open("credenciales.txt", "r") as file:
            animacion()
            for line in file:
                fields = line.strip().split(":")
                if fields[1] == username and fields[2] == password:
                    print(f"¡Inicio de sesión exitoso! Bienvenido, {username}")
                    print('----------------------------')
                    input('Presiona enter para acceder. . . ')
                    return
        print("Nombre de usuario o contraseña no válidos")
    except FileNotFoundError:
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")


# Sale del programa
def salir():
    print("Saliendo. . .")


# Limpia la pantalla del sistema operativo
def limpiar():
    os.system('cls')


# Crea la animacion de la busqueda de usuarios
def animacion():
    animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]"
    ]
    continuar = True
    i = 0
    while continuar:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
        if i == 3 * 10:
            break

# Bucle de ejecución
while True:
    # Solicita al usuario que seleccione una acción
    limpiar()
    print("¿Qué te gustaría hacer?")
    print("1. Crear una nueva cuenta")
    print("2. Iniciar sesión en una cuenta existente")
    print("3. Salir")
    choice = input()

    # Menú
    if choice == "1":
        limpiar()
        crear_cuenta()
    elif choice == "2":
        limpiar()
        inicio_sesion()
    elif choice == "3":
        limpiar()
        salir()
        break
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")











    
