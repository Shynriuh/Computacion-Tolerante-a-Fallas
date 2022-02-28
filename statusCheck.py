import os
import sys

def check_arguments():
    if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)

def get_targets():

    targets = sys.argv[1:]

    i = 0
    while i < len(targets):
        #Si no termina con .exe, se lo agrega
        if not targets[i].endswith('.exe'):
            targets[i] = targets[i] + '.exe'

        i += 1

    return targets

def getTasks(target):
    #Se leen las tareas en ejecucion
    r = os.popen('tasklist /v').read().strip().split('\n')

    for i in range(len(r)):
        #Si se encuentra en ejecucion el .exe
        if target in r[i]:
            return r[i]
    return []


if __name__ == '__main__':

    check_arguments()           #Verfica que el programa tenga argumentos
    targets = get_targets()

    while True:
        for target in targets:
            r=getTasks(target)

            #Si no esta el exe en ejecucion, lo pone en ejecucion
            if not r:
                os.startfile("D:/karen/Desktop/Programming/Python/Formulario/dist/Formulario/Formulario.exe")
                
