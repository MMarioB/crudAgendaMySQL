import pymysql

try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='contactos')
    print("Conexión correcta")

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

cursor = conexion.cursor()


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


def continuar():
    print("*" * 20)
    print("Quieres continuar?")
    print("[1] - Seguir")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def alta():
    nombre = input("Introduce el nombre\n")
    apellidos = input("Introduce el apellido\n")
    telefono = input("Introduce el telefono\n")
    edad = input("Introduce la edad\n")
    consulta = "INSERT INTO contacto VALUES('" + nombre + "','" + apellidos + "'," + "'" + telefono + "'," + edad + ") "
    print(consulta)
    cursor.execute(consulta)
    conexion.commit()


def baja():
    apellido = input("Introduce el apellido del contacto que quieres borrar")
    consulta = "DELETE FROM contacto WHERE apellidos=" + "'" + apellido + "'"
    print(consulta)
    cursor.execute(consulta)
    conexion.commit()


def modificar():
    nombreN = input("Introduce el nombre nuevo del contacto")
    telefonoN = input("Introduce el telefono nuevo del contacto")
    edadN = input("Introduce la edad nueva del contacto")
    apellido = input("Introduce el apellido del contacto que quieres modificar")
    consulta = "UPDATE contacto SET nombre=" + "'" + nombreN + "', " + "telefono=" + "'" + telefonoN + "', " + "edad=" \
               + edadN + " WHERE apellidos='" + apellido + "'"
    print(consulta)
    cursor.execute(consulta)
    conexion.commit()


def buscar():
    apellido = input("Introduce el apellido del contacto que quieres buscar")
    consulta = "SELECT * FROM contacto WHERE apellidos='" + apellido + "'"
    print(consulta)
    dato = cursor.execute(consulta)
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
    consulta = "SELECT * FROM contacto"
    cursor.execute(consulta)
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


print("Empezamos")

salir = False
salirAlta = False
salirBaja = False
salirModificar = False
salirBuscar = False
seguir = ''
while not salir:
    opcion = menu()
    if opcion == 1:
        alta()
        op1 = continuar()
        while op1 != 0:
            alta()
            op1 = continuar()

    elif opcion == 2:
        baja()
        op1 = continuar()
        while op1 != 0:
            baja()
            op1 = continuar()
    elif opcion == 3:
        modificar()
        op1 = continuar()
        while op1 != 0:
            modificar()
            op1 = continuar()
    elif opcion == 4:
        buscar()
        op1 = continuar()
        while op1 != 0:
            buscar()
            op1 = continuar()
    elif opcion == 5:
        mostrar()
    elif opcion == 0:
        op1 = continuar()
        while op1 != 0:
            opcion = menu()
            op1 = continuar()
        salir = True
        conexion.close()
    else:
        print("Introduce un numero entre 0 y 5")

print("FIN")
