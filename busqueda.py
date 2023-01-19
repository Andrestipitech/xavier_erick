from conexion import connec
# la busqueda por id con sql
conn = connec()
cursor = conn.cursor()
slq_busqqueda = "SELECT * FROM persona WHERE idpersona ='1104'"
cursor.execute(slq_busqqueda)

for persona in cursor:
    print(persona)

conn.close()