import os
import time


# Limpia la pantalla del sistema operativo
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


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
        "[        ]",
    ]
    continuar = True
    i = 0
    while continuar:
        print(animation[i % len(animation)], end="\r")
        time.sleep(0.1)
        i += 1
        if i == 3 * 10:
            break
