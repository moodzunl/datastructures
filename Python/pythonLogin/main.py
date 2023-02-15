import os
import time
from subprocess import call


def mostrar_menu(opciones):
    limpiar()
    # Renderiza la clave y el valor del menú
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    # Toma la respuesta y la retorna
    while (respuesta := input('Opción: ')) not in opciones:
        print('Opción incorrecta. Seleccione una nueva opción')
    return respuesta


def ejecutar_opcion(opcion, opciones):
    limpiar()
    # Con base en la opción leida lo renderiza
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salir):
    limpiar()
    # Función general que actua como conjunto de todas las funciones anteriores
    opcion = None
    while opcion != opcion_salir:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    limpiar()
    # Se hace un objeto de multiples opciones
    opciones = {
        '1': ('Autenticarse', autenticar_cuenta),
        '2': ('Crear cuenta', nueva_cuenta),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, str(len(opciones)))


def autenticar_cuenta():
    limpiar()
    # Maneja el error de un archivo inexistente
    try:
        existeusuario = False
        user = input('Introduce el nombre de tu cuenta: ')
        password = input('Introduce la contraseña de tu cuenta: ')
        animacion()
        with open('data.txt', 'r', 1, encoding='utf-8') as userDocument:
            for line in userDocument:
                # Verifica que se encuentren los parámetros por cada línea del documento
                if (user in line) and (password in line):
                    existeusuario = True
                else:
                    pass
        if existeusuario:
            print('Identidad verificada')
            print('----------------------------')
            input('Presiona enter para acceder. . . ')
        else:
            print('Identidad no existente')
            print('----------------------------')
            input('Presiona enter para continuar. . . ')
    except FileNotFoundError:
        limpiar()
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")


def nueva_cuenta():
    limpiar()
    # Añade al documento un nuevo usuario
    print('Creación de nueva cuenta')
    print('----------------------------')
    user = input('Introduce el nombre de tu cuenta: ')
    password = input('Introduce la contraseña de tu cuenta: ')
    with open('data.txt', 'a', encoding='utf-8') as userDocument:
        userDocument.write(str(user) + ' ' + str(password) + '\n')
    print("Contraseña creada exitosamente")
    input("Presiona enter para continuar. . .")


def salir():
    print("Saliendo. . .")


def limpiar():
    # Limpia pantalla en base al sistema operativo
    _ = call('clear' if os.name == 'posix' else 'cls')


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


if __name__ == '__main__':
    menu_principal()
