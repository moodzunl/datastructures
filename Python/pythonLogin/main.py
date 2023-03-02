import os
import time

import re
import uuid

# Definir una función para crear una nueva cuenta
def crear_cuenta():
    # Solicitar al usuario que ingrese un nombre de usuario y contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña (debe tener al menos 8 caracteres y símbolos especiales): ")

    # Validar la contraseña
    if len(password) < 8 or not re.search("[!@#$%^&*()_+-=]", password):
        print("Contraseña no válida. La contraseña debe tener al menos 8 caracteres y símbolos especiales.")
        return

    # Generar un ID único para la nueva cuenta
    account_id = str(uuid.uuid4())

    # Guardar las credenciales de inicio de sesión y el ID de la cuenta en el archivo de texto
    with open("credenciales.txt", "a") as file:
        file.write(f"{account_id}:{username}:{password}\n")
    animacion()
    print(f"¡Cuenta creada con éxito! Su nombre de usuario es {username} y su ID de cuenta es {account_id}")

# Definir una función para iniciar sesión en una cuenta existente
def inicio_sesion():
    # Solicitar al usuario que ingrese un nombre de usuario y una contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Verificar si el nombre de usuario y la contraseña coinciden
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

# Bucle principal del programa
while True:
    # Solicitar al usuario que seleccione una acción
    print("¿Qué te gustaría hacer?")
    print("1. Crear una nueva cuenta")
    print("2. Iniciar sesión en una cuenta existente")
    print("3. Salir")
    choice = input()

    # Manejar la acción seleccionada por el usuario
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











    
