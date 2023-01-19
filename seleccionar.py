from conexion import connec

conn = connec()
cursor = conn.cursor()
sql_obtencion ="SELECT * FROM persona"
cursor.execute(sql_obtencion)
for persona in cursor:
    print(persona)


conn.close()