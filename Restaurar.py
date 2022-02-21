import os
global lista
lista = list()

class Agenda:
    codigo = ""
    nombre = ""
    carrera = ""
    telefono = ""

def agregar(n, datos):
    alumno = Agenda()

    if n == 1:
        alumno.codigo = input("Codigo: ")
        alumno.nombre = input("Nombre: ")
        alumno.carrera = input("Carrera: ")
        alumno.telefono = input("Telefono: ")
    elif n == 2:
        alumno.codigo = datos[0]
        alumno.nombre = datos[1]
        alumno.carrera = datos[2]
        alumno.telefono = datos[3]

    lista.append(alumno)

def imprimir():
    print("2) DESPLEGAR AGENDA\n")

    for alumno in lista:
        print(alumno.codigo, "|", alumno.nombre, "|", alumno.carrera, "|", alumno.telefono)

def buscar():
    print("3) BUSCAR\n")

    codigo = input("Codigo del alumno: ")

    for alumno in lista:
        if(alumno.codigo == codigo):
            print(alumno.codigo, "|", alumno.nombre, "|", alumno.carrera, "|", alumno.telefono)

def eliminar():
    print("4) ELIMINAR\n")

    codigo = input("Codigo del alumno: ")

    for alumno in lista:
        if(alumno.codigo == codigo):
            lista.remove(alumno)

def guardar():
    print("5) GUARDAR\n")

    archivo = open("agenda.txt", 'w')

    for alumno in lista:
        archivo.write(alumno.codigo)
        archivo.write(" ")
        archivo.write(alumno.nombre)
        archivo.write(" ")
        archivo.write(alumno.carrera)
        archivo.write(" ")
        archivo.write(alumno.telefono)
        archivo.write("\n")

    archivo.close()
    print("Se guardo al disco correctamente.")

def cargar():

    print("6) CARGAR\n")
    archivo = open("agenda.txt", 'r')

    linea = archivo.readline()  # Lee la primera linea
    datos = linea.split()       # Guarda la linea como lista

    while linea != '':
        # Se capturan los datos
        agregar(2, datos)   # Se manda a llamar la funcion agregar y se manda la lista
        linea = archivo.readline()
        datos = linea.split()

    print("Se leyo del disco correctamente.")
    archivo.close()

def menu():
        print('''		Agenda
        1) Agregar
        2) Desplegar agenda
        3) Buscar
        4) Eliminar
        5) Guardar agenda
        6) Cargar agenda
        0) Salir
        ''')

def main():

    try:
        continuar = True

        while continuar:
            os.system("cls")
            menu()
            o = int(input("Selecciona una opcion: "))

            if o == 1:
                os.system("cls")
                print("1) AGREGAR\n")
                agregar(1,0)
            
            elif o == 2:
                os.system("cls")
                imprimir()

            elif o == 3:
                os.system("cls")
                buscar()

            elif o == 4:
                os.system("cls")
                eliminar()

            elif o == 5:
                os.system("cls")
                guardar()
            
            elif o == 6:
                os.system("cls")
                cargar()
            
            elif o == 0:
                continuar = False

            else:
                print("Opcion no valida.")
            
            input("\nPresione ENTER para continuar...")
            
    except:
        guardar()
        print("Ocurrio un error")
            

if "__name__ == __main__":
    main()