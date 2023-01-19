from conexion import connec
#from MySQLdb import IntegrityError
#from mysql.connector import Error
'''conn = connec()
cursor = conn.cursor()
try:
    dni = input("ingrese el numero de cedula: ")
    name = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    edad = int(input("ingrese su edad: "))
    email = input("ingrese el correo: ")
    estatura = float(input("ingrese su altuta. "))
    #sql_insertar = f"INSERT INTO persona(idpersona, nombre, apellido, edad, correo, altura)VALUES('1105', 'Insert_python','sql_py', '25', 'prueba5@gmail.com', '1.84')"
    sql_insertar = f"INSERT INTO persona(idpersona, nombre, apellido, edad, correo, altura)VALUES('{dni}', '{name}','{apellido}', '{edad}', '{email}', '{estatura}')"    
    cursor.execute(sql_insertar)
    conn.commit()
    print(f"se realizo {cursor.rowcount} registros")
except Exception as e:
    print("surio el siguiente error", type(e).__name__)
    if('IntegrityError' == type(e).__name__):
        print("la cedula ya existe")
conn.close()'''
def insertar_persona(dni, name, apellido, edad, email, estatura):
    conn = connec()
    cursor = conn.cursor()
    try:
        sql_insertar = f"INSERT INTO persona(idpersona, nombre, apellido, edad, correo, altura)VALUES('{dni}', '{name}','{apellido}', '{edad}', '{email}', '{estatura}')"    
        cursor.execute(sql_insertar)
        conn.commit()
        print(f"se realizo {cursor.rowcount} registros")
    except Exception as e:
        print("surio el siguiente error", type(e).__name__)
        if('IntegrityError' == type(e).__name__):
            print("la cedula ya existe")
    conn.close()