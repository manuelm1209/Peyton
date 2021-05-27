import subprocess


def abrir_notes():
    subprocess.call(['open', '-a', 'TextEdit', "mis_notas.txt"])


abrir_notes()