import os
import datetime
import shutil

if int(archivo_txt.readlines()[0][:-1]) > 3:
    print("Tipo de archivo no encontrado.")
    archivo_txt.seek(0)


# archivos_txt = []
# carpetas_mover = []
# for root, dirs, files in os.walk('/Volumes/D/ITE/Peyton/Subir'):
#     for file in files:
#         if file.endswith(".txt"):
#             if file[0] != ".":
#                 archivos_txt.append([root, file])
#                 if os.path.isdir(root):
#                     if root not in carpetas_mover:
#                         carpetas_mover.append(root)
#
# print(archivos_txt)
# print(carpetas_mover)
# print("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
#
# if os.path.isdir("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today())):
#     for i in range(len(carpetas_mover)):
#         shutil.move(carpetas_mover[i], "/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
# else:
#     os.mkdir("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
#     for i in range(len(carpetas_mover)):
#         shutil.move(carpetas_mover[i], "/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()))
#
#         #os.rename("/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.date.today()), "/Volumes/D/ITE/Peyton/Hecho/" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second) + "-" +str(datetime.datetime.now().microsecond))