import pymysql


# Metodos

def menu():
    print("*" * 20)
    print("- Menú Agenda -")
    print("[1] - Alta")
    print("[2] - Baja")
    print("[3] - Modificar")
    print("[4] - Buscar")
    print("[5] - Mostrar Todo")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def lee_entero():
    while True:
        entrada = input("Introduce una opcion: ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("Error!! Has introducido algo que no es un numero")


def validarEdad():
    while True:
        entrada = input("Introduce una edad\n ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("Error!! Has introducido algo que no es una edad")


def continuar():
    print("*" * 20)
    print("Quieres continuar?")
    print("[1] - Seguir")
    print("[0] - Salir")
    print("*" * 20)
    opc = lee_entero()
    while True:
        if opc > 1:
            opc = lee_entero()
        else:
            return opc


def alta():
    nombre = input("Introduce el nombre\n")
    while True:
        if not nombre:
            print("Cadena vacia")
            nombre = input("Introduce el nombre\n")
        else:
            break
    apellido = input("Introduce el apellido\n")
    while True:
        if not apellido:
            print("Cadena vacia")
            apellido = input("Introduce el apellido\n")
        else:
            break
    telefono = input("Introduce el telefono\n")
    while True:
        if telefono.isdigit():
            break
        else:
            telefono = input("Introduce el telefono de nuevo\n")
    validaEdad = validarEdad()
    edad = str(validaEdad)
    consulta = "INSERT INTO agenda_db.contacto VALUES('" + nombre + "','" + apellido + "'," + "'" + telefono + "'," + edad + ") "
    cursor.execute(consulta)
    if cursor.execute(consulta) == 0:
        print("No hay registros a los que aplicar esta consulta")
    else:
        print("Consulta realizada")
    conexion.commit()


def baja():
    apellido = input("Introduce el apellido del contacto que quieres borrar")
    while True:
        if not apellido:
            print("Cadena vacia")
            apellido = input("Introduce el apellido de nuevo\n")
        else:
            break
    consulta = "DELETE FROM agenda_db.contacto WHERE apellido=" + "'" + apellido + "'"
    cursor.execute(consulta)
    if cursor.execute(consulta) == 0:
        print("No hay registros a los que aplicar esta consulta")
    else:
        print("Consulta realizada")
    conexion.commit()


def modificar():
    nombreN = input("Introduce el nombre nuevo del contacto")
    while True:
        if not nombreN:
            print("Cadena vacia")
            nombreN = input("Introduce el nombre de nuevo\n")
        else:
            break
    telefonoN = input("Introduce el telefono nuevo del contacto")
    while True:
        if telefonoN.isdigit():
            break
        else:
            telefonoN = input("Introduce el telefono de nuevo\n")
    validaEdad = validarEdad()
    edadN = str(validaEdad)
    apellido = input("Introduce el apellido del contacto que quieres modificar")
    while True:
        if not apellido:
            print("Cadena vacia")
            apellido = input("Introduce el apellido de nuevo\n")
        else:
            break
    consulta = "UPDATE agenda_db.contacto SET nombre=" + "'" + nombreN + "', " + "telefono=" + "'" + telefonoN + "', " + "edad=" \
               + edadN + " WHERE apellido='" + apellido + "'"
    cursor.execute(consulta)
    if cursor.execute(consulta) == 0:
        print("No hay registros a los que aplicar esta consulta")
    else:
        print("Consulta realizada")
    conexion.commit()


def buscar():
    apellido = input("Introduce el apellido del contacto que quieres buscar")
    while True:
        if not apellido:
            print("Cadena vacia")
            apellido = input("Introduce el apellido de nuevo\n")
        else:
            break
    consulta = "SELECT * FROM agenda_db.contacto WHERE apellido='" + apellido + "'"
    if cursor.execute(consulta) == 0:
        print("No hay registros a los que aplicar esta consulta")
    else:
        print("Consulta realizada")
    registros = cursor.fetchall()
    for registro in registros:
        print("***********************************")
        print(" -- CONTACTO -- ")
        print("- Nombre", registro[0])
        print("- Apellidos", registro[1])
        print("- Telefono", registro[2])
        print("- Edad", registro[3])
        print("***********************************")
    conexion.commit()


def mostrar():
    consulta = "SELECT * FROM agenda_db.contacto"
    cursor.execute(consulta)
    if cursor.execute(consulta) == 0:
        print("No hay registros a los que aplicar esta consulta")
    else:
        print("Consulta realizada")
    registros = cursor.fetchall()
    for registro in registros:
        print("***********************************")
        print(" -- CONTACTO -- ")
        print("- Nombre:", registro[0])
        print("- Apellidos:", registro[1])
        print("- Telefono:", registro[2])
        print("- Edad:", registro[3])
        print("***********************************")
    conexion.commit()


# Programa
print("Empezamos")

# Conexion
try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='')
    conexion.cursor().execute("CREATE DATABASE IF NOT EXISTS agenda_db;")
    print("Conexión correcta")

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS agenda_db.contacto (nombre TEXT, apellido TEXT, telefono TEXT, edad INT)")

# Menu
salir = False
while not salir:
    opcion = menu()
    if opcion == 1:
        while True:
            alta()
            op1 = continuar()
            if op1 == 0:
                break
            elif op1 == 1:
                alta()
            else:
                print("Has introducido", op1, " Seguimos")

    elif opcion == 2:
        while True:
            baja()
            op1 = continuar()
            if op1 == 0:
                break
            elif op1 == 1:
                baja()
    elif opcion == 3:
        while True:
            modificar()
            op1 = continuar()
            if op1 == 0:
                break
            elif op1 == 1:
                modificar()
    elif opcion == 4:
        while True:
            buscar()
            op1 = continuar()
            if op1 == 0:
                break
            elif op1 == 1:
                buscar()
    elif opcion == 5:
        mostrar()
    elif opcion == 0:
        salir = True
        conexion.close()
    else:
        print("Introduce un numero entre 0 y 5")

print("FIN")
