list_nombres = []
list_identificacion = []
list_correo = []
list_contacto = []
list_edad = []
list_experiencia = []
list_profesion = []
list_ciudad = []
list_sexo = []

import os

def fnt_limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def fnt_registrar(nombres, identificacion, correo, contacto, edad, experiencia, profesion, ciudad, sexo):
    if not (25 <= edad <= 35 and (profesion == 'ING. SISTEMAS' or profesion == 'ING. INFORMATICO') and 2 <= experiencia <= 4):
        enter = input('\nError, candidato no cumple con los requisitos\nPresiona <enter> para continuar')
    else:
        list_nombres.append(nombres)
        list_identificacion.append(identificacion)
        list_correo.append(correo)  
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_experiencia.append(experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        enter = input('\nCandidato registrado correctamente\nPresiona <enter> para continuar')

def fnt_consultar():
    fnt_limpiar_pantalla()
    for i in range(len(list_nombres)):
        print(f'Nombre: {list_nombres[i]}, Identificación: {list_identificacion[i]}, Correo: {list_correo[i]}, Contacto: {list_contacto[i]}, Edad: {list_edad[i]}, Experiencia: {list_experiencia[i]}, Profesión: {list_profesion[i]}, Ciudad: {list_ciudad[i]}, Sexo: {list_sexo[i]}')
    enter = input('\nPresiona <enter> para continuar')

def fnt_selector(opcion):
    fnt_limpiar_pantalla()
    if opcion == '1':
        nombres = input('Nombres y apellidos: ')
        identificacion = input('Identificación: ')
        correo = input('Correo electrónico: ')
        contacto = input('Contacto: ')
        edad = int(input('Edad: '))
        experiencia = int(input('Años de experiencia: '))
        profesion = input('Profesión (ING. SISTEMAS / ING. INFORMATICO): ')
        ciudad = input('Ciudad: ')
        sexo = input('Sexo: ')
        fnt_registrar(nombres, identificacion, correo, contacto, edad, experiencia, profesion, ciudad, sexo)
    elif opcion == '2':
        fnt_consultar()
    elif opcion == '3':
        exit()

sw = True
while sw:
    op = input('\n\n<<<<<< MENU PRINCIPAL >>>>>>\n1.REGISTRAR\n2.CONSULTAR\n3.SALIR\n-> ')
    fnt_selector(op)



