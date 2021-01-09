import pymysql
#conection=pymysql.connect(
#    host="localhost",
#    user="root",
#    password="1234",
#    db="aplicattion"
#)
#cursor= conection.cursor()
#sql2="Insert into user values (2,'thiago')"
#cursor.execute(sql2)
#conection.commit()
def getConection():
    conection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="aplicattion"
    )
    return conection


def consultarClientes():
    conection=getConection()
    cursor=conection.cursor()
    cursor.execute("Select * from cliente")
    datos=cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
def consultarArtistas():
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("Select * from artista")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
def consultarDatos(dato):
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("Select * from "+dato)
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
def menuEasy():
    verdad=True
    while(verdad):
        print("**********Consultas***********")
        print("1.Consultar clientes")
        print("2.Consultar artistas")
        print("3.Consultar eventos")
        print("4.Consultar pagos")
        print("5.Consultar asistencia a eventos")
        print("6.Consultar solicitudes de eventos")
        print("7.Consultar calificaciones de los artistas")
        op=input("Elija una opcion: ")
        if(op=="1"):
            consultarDatos("cliente")
            verdad=False
        elif(op=="2"):
            consultarDatos("artista")
            verdad = False
        elif (op == "3"):
            consultarDatos("evento")
            verdad = False
        elif (op == "4"):
            consultarDatos("pago")
            verdad = False
        elif (op == "5"):
            consultarDatos("asistencia")
            verdad = False
        elif (op == "6"):
            consultarDatos("solicitud")
        elif (op == "7"):
            consultarDatos("calificacion")
            verdad = False
def CreacionCuentaArtista(correo,nombre,apellido,profesion,descripcion):
    conection = getConection()
    cursor = conection.cursor()
    #OJO con las comillas simples en cada variable
    cursor.execute("INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('"+correo+"','"+nombre+"','"+apellido+"','"+profesion+"','"+descripcion+"')")
    #cursor.execute( "INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('tago@hotmail.com','tago','tumbaco','disenador','un crack')")
    conection.commit()
    cursor.close()
    conection.close()
    print("se pudo")
def conversor(tupla):
    cadena=" "
    for elemento in tupla:
        cadena=cadena+(str(elemento)+"| ")
    return cadena
def consultarEventosViejos(correo):
    conection = getConection()
    cursor = conection.cursor()

    cursor.execute("Select * from evento where correoArt='"+correo+"'")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
    for fila in datos:
        #print(fila)
        #print(type(fila[0]))
        print(conversor(fila))
def crearEvento(titulo,descripcion,duracion,fechaInicio,tipo,costo,correo_Artista):
    conection = getConection()
    cursor = conection.cursor()
    # OJO con las comillas simples en cada variable
    cursor.execute(
        "INSERT INTO evento VALUES('"+0+"',"'' + titulo + "','" + descripcion + "','" + duracion + "','" + fechaInicio + "','" + tipo + "','"+costo++ "','"+correo_Artista+"')")
    # cursor.execute( "INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('tago@hotmail.com','tago','tumbaco','disenador','un crack')")
    conection.commit()
    cursor.close()
    conection.close()
    print("se pudo")
def buscarAsustentes(IdEvento):
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("select cli.correo,cli.nombre,cli.apellido from asistencia as asis join cliente as cli on asis.cliente=cli.correo where asis.evento="+str(IdEvento))
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
#CreacionCuentaArtista("tago2000@hotmail.com","tago","tumbaco","disenador","un crack")
#consultarEventosViejos("thiago@hotmail.com")
buscarAsustentes(12345)
#menuEasy()
