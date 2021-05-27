from camisetas import cargar_camisetas, cargar_hoodies
from slack_peyton import chat_slack
import os
import datetime
import shutil


def run_peyton():
    seleccion = "1"
    # seleccion = input("++ Hola soy Peyton ++\nSelecciona una tarea:\n1. Subir diseños a la plataforma.\n"
    #                   "2. Crear Afiliado.\n3. Crear página afiliado.\n0. Salir.\nR/: ")
    if seleccion == "1":

        archivos_txt = []
        carpetas_mover = []
        reporte_slack = []
        reporte_errores = ""
        for root, dirs, files in os.walk('/Volumes/D/ITE/Peyton/Subir'):
            for file in files:
                if file.endswith(".txt"):
                    # Ignorar archivos ocultos.
                    if file[0] != ".":
                        archivos_txt.append([root, file])
                        if os.path.isdir(root):
                            if root not in carpetas_mover:
                                carpetas_mover.append(root)

        for i in range(len(archivos_txt)):

            # Abrir archivo de texto.
            with open((archivos_txt[i][0] + "/" + archivos_txt[i][1]), "r", encoding='ISO-8859-1') as archivo_txt:
                # Leer primera fila del txt para ver que tipo de artículo es.
                archivo_txt.seek(0)
                if archivo_txt.readlines()[0][:-1] == "1":
                    cargar_camisetas("Peyton1984Manning1984", "O7C95GW%0lVu3w&l9ykKHhkD", archivos_txt, i)
                    archivo_txt.seek(0)
                    reporte_slack.append(("Camiseta", archivo_txt.readlines()[1][:-1]))
                    archivo_txt.seek(0)
                else:
                    archivo_txt.seek(0)
                if archivo_txt.readlines()[0][:-1] == "2":
                    # reporte_errores = (cargar_hoodies("Peyton1984Manning1984", "O7C95GW%0lVu3w&l9ykKHhkD", archivos_txt, i))
                    cargar_hoodies("Peyton1984Manning1984", "O7C95GW%0lVu3w&l9ykKHhkD", archivos_txt, i)
                    archivo_txt.seek(0)
                    reporte_slack.append(("Hoodie", archivo_txt.readlines()[1][:-1]))
                    archivo_txt.seek(0)
                    print(reporte_errores)
                else:
                    archivo_txt.seek(0)
                #elif archivo_txt.readlines()[0][:-1] == "3":
                    #crear_pagina_afiliado("Peyton1984Manning1984", "O7C95GW%0lVu3w&l9ykKHhkD")
                if int(archivo_txt.readlines()[0][:-1]) > 3:
                    print("Tipo de archivo no encontrado.")
                    archivo_txt.seek(0)

# REPORTE SLACK Y MOVER CARPETA
###############################
        chat_slack("imprimetuestilocol@gmail.com", "O7C95GW%0lVu3w&l9ykKHhkD", reporte_slack)

        if os.path.isdir("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today())):
            for j in range(len(carpetas_mover)):
                shutil.move(carpetas_mover[j], "/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
        else:
            os.mkdir("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
            for j in range(len(carpetas_mover)):
                shutil.move(carpetas_mover[j], "/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
######################


    elif seleccion == "0":
        print("\nChao!!!")
    else:
        print("Opción no valida\n")
        run_peyton()

run_peyton()