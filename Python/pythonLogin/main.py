import re
from login import logged
from funciones_auxiliares import limpiar, animacion

# Definir una lista para almacenar los IDs de cuenta existentes
ids_existentes = []


# Leer el archivo de texto y agregar los IDs existentes a la lista
try:
    with open("credenciales.txt", "r") as file:
        for line in file:
            fields = line.strip().split(":")
            ids_existentes.append(int(fields[0]))
except FileNotFoundError:
    print("\n")
    print("El archivo no se encontró")
    input("Presiona enter para continuar. . .")


# Definir una función para crear una nueva cuenta
def crear_cuenta():
    # Solicitar al usuario que ingrese un nombre de usuario y contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input(
        "Ingrese su contraseña (debe tener al menos 8 caracteres y símbolos especiales): "
    )
    security_question = input(
        "Escribe una pregunta de seguridad (p. ej., ¿Cuál es el nombre de tu mascota?): "
    )
    security_answer = input("Escribe la respuesta a la pregunta de seguridad: ")

    # Validar la contraseña
    if len(password) != 8 or not re.search("[!@#$%^&*()_+-=]", password):
        print(
            "Contraseña no válida. La contraseña de ser de 8 caracteres y símbolos especiales."
        )
        print("----------------------------")
        input("Presiona enter para continuar. . . ")
        return

    # Generar un nuevo ID único para la cuenta
    id_cuenta = max(ids_existentes) + 1 if ids_existentes else 1
    while id_cuenta in ids_existentes:
        id_cuenta += 1

    # Guardar las credenciales de inicio de sesión, la pregunta de seguridad y su respuesta, y el ID de la cuenta en el archivo de texto
    with open("credenciales.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{id_cuenta}:{username}:{password}:{security_question}:{security_answer}\n"
        )
    print(
        f"¡Cuenta creada con éxito! Su nombre de usuario es {username} y su ID de cuenta es {id_cuenta}"
    )
    print("----------------------------")
    input("Presiona enter para continuar. . . ")

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
                if len(fields) != 5:
                    print("El archivo de credenciales es inválido")
                    return

                if fields[1] == username and fields[2] == password:
                    print(f"¡Inicio de sesión exitoso! Bienvenido, {username}")
                    print("----------------------------")
                    input("Presiona enter para acceder. . . ")
                    logged(fields[0])

            print("Nombre de usuario o contraseña no válidos")
    except FileNotFoundError:
        print("El archivo de credenciales no se encontró")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo de credenciales: {str(e)}")


def recuperar_contrasena():
    # Preguntar por el username y validar si existe en el registro
    username = input("Ingrese su nombre de usuario: ")
    security_question = input(
        "Escribe una pregunta de seguridad (p. ej., ¿Cuál es el nombre de tu mascota?): "
    )
    security_answer = input("Escribe la respuesta a la pregunta de seguridad: ")
    try:
        with open("credenciales.txt", "r+") as file:
            animacion()
            found = False
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                fields = line.strip().split(":")
                if len(fields) != 5:
                    print("El archivo de credenciales es inválido")
                    return

                if (
                    fields[1] == username
                    and fields[3] == security_question
                    and fields[4] == security_answer
                ):
                    print(f"Respuesta correcta. Bienvenido, {username}")
                    new_password = input("¿Cuál será tu nueva contraseña?: ")
                    fields[2] = new_password
                    found = True
                file.write(f"{':'.join(fields)}\n")

            if not found:
                print("Nombre de usuario, pregunta o respuesta incorrectas.")
                return

            print("Contraseña cambiada correctamente")
            print("----------------------------")
            input("Presiona enter para acceder. . . ")
    except FileNotFoundError:
        print("El archivo de credenciales no se encontró")
    except Exception as e:
        print(f"Ocurrió un error al leer/escribir el archivo de credenciales: {str(e)}")


# Leer el archivo de texto y agregar los IDs existentes a la lista
try:
    with open("credenciales.txt", "r") as file:
        for line in file:
            fields = line.strip().split(":")
            ids_existentes.append(int(fields[0]))
except FileNotFoundError:
    print("\n")
    print("El archivo no se encontró")
    input("Presiona enter para continuar. . .")


# Sale del programa
def salir():
    print("Saliendo. . .")


# Bucle de ejecución
while True:
    # Solicita al usuario que seleccione una acción
    limpiar()
    print("¿Qué te gustaría hacer?")
    print("1. Crear una nueva cuenta")
    print("2. Iniciar sesión en una cuenta existente")
    print("3. Olvide mi contraseña")
    print("4. Salir")
    choice = input()

    # Menú
    if choice == "1":
        limpiar()
        crear_cuenta()
    elif choice == "2":
        limpiar()
        inicio_sesion()
    elif choice == "3":
        recuperar_contrasena()
        limpiar()
    elif choice == "4":
        limpiar()
        salir()
        break
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
