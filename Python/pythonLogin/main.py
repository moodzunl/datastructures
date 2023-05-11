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


def eliminar_cuenta():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    try:
        with open("credenciales.txt", "r") as cred_file, open(
            "usuario.txt", "r"
        ) as user_file, open("contrasena.txt", "r") as pass_file, open(
            "pregunta.txt", "r"
        ) as quest_file, open(
            "respuesta.txt", "r"
        ) as ans_file:
            cred_lines = cred_file.readlines()
            user_lines = user_file.readlines()
            pass_lines = pass_file.readlines()
            quest_lines = quest_file.readlines()
            ans_lines = ans_file.readlines()

        found = False
        for i, cred_line in enumerate(cred_lines):
            cred_fields = cred_line.strip().split(":")
            if len(cred_fields) != 5:
                print("El archivo de credenciales es inválido")
                return

            if cred_fields[1] == username and cred_fields[2] == password:
                print(f"Eliminando, {username}")
                print("----------------------------")
                input("Presiona enter para acceder. . . ")
                found = True
                break

        if not found:
            print("Nombre de usuario o contraseña no válidos")
            return

        del cred_lines[i]
        del user_lines[i]
        del pass_lines[i]
        del quest_lines[i]
        del ans_lines[i]

        with open("credenciales.txt", "w") as cred_file, open(
            "usuario.txt", "w"
        ) as user_file, open("contrasena.txt", "w") as pass_file, open(
            "pregunta.txt", "w"
        ) as quest_file, open(
            "respuesta.txt", "w"
        ) as ans_file:
            cred_file.writelines(cred_lines)
            user_file.writelines(user_lines)
            pass_file.writelines(pass_lines)
            quest_file.writelines(quest_lines)
            ans_file.writelines(ans_lines)

    except FileNotFoundError:
        print("Alguno de los archivos no se encontró")
    except Exception as e:
        print(f"Ocurrió un error al leer o escribir los archivos: {str(e)}")


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
    with open("usuario.txt", "a", encoding="utf-8") as file:
        file.write(f"{id_cuenta}:{username}\n")
    with open("contrasena.txt", "a", encoding="utf-8") as file:
        file.write(f"{id_cuenta}:{password}\n")
    with open("pregunta.txt", "a", encoding="utf-8") as file:
        file.write(f"{id_cuenta}:{security_question}\n")
    with open("respuesta.txt", "a", encoding="utf-8") as file:
        file.write(f"{id_cuenta}:{security_answer}\n")
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
                    return  # Regresa después de un inicio de sesión exitoso

            # Si se ha recorrido todo el archivo y no se ha devuelto nada, las credenciales son incorrectas
            print("Nombre de usuario o contraseña incorrectos.")
            input("Presiona enter para continuar. . . ")
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
        with open("credenciales.txt", "r") as cred_file, open(
            "contrasena.txt", "r"
        ) as pass_file:
            animacion()
            cred_lines = cred_file.readlines()
            pass_lines = pass_file.readlines()

            found = False
            for i, cred_line in enumerate(cred_lines):
                cred_fields = cred_line.strip().split(":")
                if len(cred_fields) != 5:
                    print("El archivo de credenciales es inválido")
                    return

                if (
                    cred_fields[1] == username
                    and cred_fields[3] == security_question
                    and cred_fields[4] == security_answer
                ):
                    print(f"Respuesta correcta. Bienvenido, {username}")
                    new_password = input("¿Cuál será tu nueva contraseña?: ")
                    cred_fields[2] = new_password
                    cred_lines[i] = ":".join(cred_fields) + "\n"
                    pass_fields = pass_lines[i].strip().split(":")
                    pass_fields[1] = new_password
                    pass_lines[i] = ":".join(pass_fields) + "\n"
                    found = True
                    break

            if not found:
                print("Nombre de usuario, pregunta o respuesta incorrectas.")
                input("Presiona enter para continuar. . . ")
                return

        # Reabrir los archivos para escritura
        with open("credenciales.txt", "w") as cred_file, open(
            "contrasena.txt", "w"
        ) as pass_file:
            cred_file.writelines(cred_lines)
            pass_file.writelines(pass_lines)

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
    print("4. Eliminar cuenta")
    print("5. Salir")
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
        eliminar_cuenta()
        limpiar()
    elif choice == "5":
        limpiar()
        salir()
        break
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
