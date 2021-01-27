import pymysql
from datetime import datetime
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

Conexion=getConection()

def consultarClientes():
    conection=Conexion
    cursor=conection.cursor()
    cursor.execute("Select * from cliente")
    datos=cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
        
def consultarArtistas():
    conection=Conexion
    cursor = conection.cursor()
    cursor.execute("Select * from artista")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    for fila in datos:
        print(fila)
        
def consultarDatos(dato):
    conection = Conexion
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
            
def CreacionCuentaArtista(correo,contra,nombre,apellido,profesion,descripcion):
    conection =Conexion
    cursor = conection.cursor()
    #OJO con las comillas simples en cada variable
    cursor.execute("call CrearCuentaArtista"+ "('"+correo+"','"+contra+"','"+nombre+"','"+apellido+"','"+profesion+"','"+descripcion+"')");
    #cursor.execute("INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('"+correo+"','"+contra+"','"+nombre+"','"+apellido+"','"+profesion+"','"+descripcion+"')")
    #cursor.execute( "INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('tago@hotmail.com','tago','tumbaco','disenador','un crack')")
    conection.commit()
    cursor.close()
    conection.close()
    print("se pudo")
    
def conversor(tupla):
    cadena=" "
    for elemento in tupla:
        cadena=cadena+(str(elemento)+"  ||||   ")
    return cadena
def consultarEventosViejos(correo):
    conection = Conexion
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
    conection = Conexion
    cursor = conection.cursor()
    # OJO con las comillas simples en cada variable
    cursor.execute(
        "INSERT INTO evento VALUES('"+0+"',"'' + titulo + "','" + descripcion + "','" + duracion + "','" + fechaInicio + "','" + tipo + "','"+costo++ "','"+correo_Artista+"')")
    # cursor.execute( "INSERT INTO Artista(correo,nombre,apellido,profesion,descripcion) VALUES('tago@hotmail.com','tago','tumbaco','disenador','un crack')")
    conection.commit()
    cursor.close()
    conection.close()

def buscarAsistentes(IdEvento):
    conection = Conexion
    cursor = conection.cursor()
    cursor.execute("select cli.correo,cli.nombre,cli.apellido from asistencia as asis join cliente as cli on asis.cliente=cli.correo where asis.evento="+str(IdEvento))
    try:
        datos = cursor.fetchall()
        cursor.close()
        conection.close()
        cont=0
        print(datos)
        print(len(datos))

        for fila in datos:
            cont+=1
            print(conversor(fila))
        if cont==0:
            print("No a asistido ningun cliente a este evento o no existe ningun evento con esta ID")
    except:
        print("No existe ningun evento con esta ID")
        
def VerificarExistencia():
    correo=input("Ingrese correo: ")
    contra=input("Ingrese contraseña: ")
    conection = Conexion
    cursor = conection.cursor()
    cursor2=conection.cursor()
    cursor.execute("select * from cliente where correo='"+correo+"' and contra='"+contra+"'")
    cursor2.execute("select * from artista where correo='"+correo+"' and contra='"+contra+"'")
    datos = cursor.fetchall()
    datos2=cursor2.fetchall()
    if len(datos)==0 and len(datos2)==0:
        #retorna una tupla vacia
        return tuple()
    elif len(datos)!=0:
        #retorna una tupla de los datos del cliente
        return datos[0]
    elif len(datos2)!=0:
        #retorna una tupla de los datos del artista
        return datos2[0]
    else:
        #retorna una tupla vacia
        return tuple()
    cursor2.close()
    cursor.close()
    conection.close()
    
def creacionCuentaCliente(correo,contra, nombre, apellido):
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("call CrearCuentaCliente('"+correo+"', '"+contra+"', '"+nombre+"', '"+apellido+"')")
    conection.commit()
    cursor.close()
    conection.close()
    print("Cuenta Creada")
    
def consultarEventosCliente(correo):
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("Select * from MostrarEvento m where m.correo='"+correo+"'")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
    for fila in datos:
        print(conversor(fila))
        
def Actualidad_Evento(d1):
    #d1 es la fecha de cada ecento respecto a la fecha actual
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    x=datetime.now()
    fecha=str(x.year)+"-"+str(x.month)+"-"+str(x.day)
    d3 = datetime.strptime(fecha, "%Y-%m-%d")
    #print((d1 - d3).days)
    return (d1 - d3).days

def MostrarEventosActuales():
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("select evento.IdEvento,evento.titulo,evento.descripcion,evento.duracion,evento.fechaInicio,evento.tipo,evento.costo,evento.correoArt  from evento")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
    for fila in datos:
        #print(str(fila[4]))
        if Actualidad_Evento(str(fila[4]))>=0:
            print(conversor(fila))
            
def elegirEventoCliente(correo):
    try:
        print("|||||   Asistencia a Evento   |||||")
        MostrarEventosActuales()
        id=input("Elija la ID del evento que desea asistir")
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("call ElegirEventoCliente('"+correo+"','"+id+"'")
        conection.commit()
        cursor.close()
        conection.close()
        print("Asistencia cumplida")
        return True
    except:
        return False
    
def MostrarEventosActualesParaPagar():
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("select evento.IdEvento,evento.titulo,evento.descripcion,evento.duracion,evento.fechaInicio,evento.tipo,evento.costo,evento.correoArt  from evento having evento.costo>0")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
    for fila in datos:
        #print(str(fila[4]))
        if Actualidad_Evento(str(fila[4]))>=0:
            print(conversor(fila))
            
def pagarEventoCliente(correo):
    fecha = datetime.now()
    try:
        print("|||||   Pagar Evento   |||||")
        MostrarEventosActualesParaPagar()
        id=input("Elija la ID del evento que desea pagar")
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("insert into pago values ('"+correo+"','"+id+"','"+fecha+"',TRUE,'Tarjeta')")
        conection.commit()
        cursor.close()
        conection.close()
        print("Asistencia cumplida")
        return True
    except:
        return False
   
def consultarEventoPagadoCliente(correo):
    conection = getConection()
    cursor = conection.cursor()
    cursor.execute("Select * from ConsultarEventosPagados as c where c.correo='"+ correo +"")
    datos = cursor.fetchall()
    cursor.close()
    conection.close()
    print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
    for fila in datos:
        print(conversor(fila))
    
def Menu():
    verdad=True
    correo = ""
    tipo = ""
    while verdad:
        print("******Bienvenido******")

        print("1.|||||  Ingresar  |||||")
        print("2.|||||  Registrar  |||||")

        op=input("Selecciones una opcion:")

        if op=="1":
            tupla=VerificarExistencia()
            if len(tupla)==4:
                tipo="cliente"
                correo=tupla[0]
                verdad=False
            elif len(tupla)==6:
                tipo="artista"
                correo=tupla[0]
                verdad=False
        elif op=="2":
            print("||||||  Creacion de cuenta  |||||")
            print("1. Crear cuenta artista")
            print("2. Crear cuenta cliente")
            op2=input("Elija una opcion: ")
            if op2=="1":
                #Creacion de cuenta artista
                 #CreacionCuentaArtista(correo,nombre,apellido,profesion,descripcion)
                print("|||||  Creacion cuenta artista  |||||")
                verdad2=True
                while(verdad2):
                    try:
                        correo2=input("Ingrese su correo: ")
                        contra=input("Ingrese su contraseña: ")
                        nombre=input("Ingrese su nombre: ")
                        apellido=input("Ingrese su apellido: ")
                        profesion= input("Ingrese su profesion: ")
                        descripcion=input("Ingrese su descripcion: ")
                        CreacionCuentaArtista(correo2,contra,nombre,apellido,profesion,descripcion)
                        print("Su cuenta a sido creada con exito")
                        tipo="artista"
                        correo=correo2
                        verdad2=False
                    except:
                        print("||||||  Este correo ya ha sido registrado  |||||")
            #Falta crear la opcion para creacion de cuenta cliente
            if op2=="2":
                #Creacion de cuenta cliente
                #creacionCuentaCliente(correo,contra, nombre, apellido)
                print("|||||  Creación de cuenta Cliente  |||||")
                bandera = True
                while(bandera):
                    try:
                        correo3=input("Ingrese su correo: ")
                        contra=input("Ingrese contraseña: ")
                        nombre=input("Ingrese su nombre: ")
                        apellido=input("Ingrese su apellido: ")
                        creacionCuentaCliente(correo, contra, nombre, apellido)
                        print("Su cuenta ha sido creada con exito!")
                        tipo="cliente"
                        correo=correo3
                        bandera=False
                    except:
                        print("||||||  Este correo ya ha sido registrado  |||||")
    verdad3=True
    while(verdad3):
        if tipo=="artista":
            print("|||||   Bienvenido Artista   ||||||")
            print("1. Consultar eventos anteriores")
            print("2. Registrar un evento")
            print("3. Consultar el listado de asistentes a un evento")
            print("4. IDK")
            print("5. Salir")
            op3= input("Elija una opcion: ")
            if op3=="1":
                consultarEventosViejos(correo)
            elif op=="2":
                #crearEvento(titulo,descripcion,duracion,fechaInicio,tipo,costo,correo_Artista)
                verdad4=True
                while verdad4:
                    try:
                        print("|||||   Creacion de Eventos   |||||")
                        titulo=input("Ingrese titulo: ")
                        descripcion= input("Ingrese descripcion: ")
                        duracion=input("Ingrese duracion en horas: ")
                        fechaInicio=input("Ingrese Fecha de inicio (Ano-mes-dia): ")
                        tipoEvento= input("Ingrese tipo de evento(Privado/Publico):")
                        costo= input("Ingrese costo: ")

                        crearEvento(titulo, descripcion, float(duracion), fechaInicio, tipoEvento, float(costo), correo)
                        print("El evento a sido creado exitosamente")
                        verdad4=False
                    except:
                        print("Algun dato fue mal ingresado ")
            elif op3=="3":
                try:
                    print("|||||   Visualizacion de Eventos   |||||")
                    consultarEventosViejos(correo)
                    id=input("Ingrese la ID del evento que desea consultar sus asistentes: ")
                    buscarAsistentes(int(id))
                    print("Consulta exitosa****")
                except:
                    print("Esta id no existe es esta lista de eventos")
            elif op3=="5":
                verdad3=False
        #Falta la creacion del if cuando tipo="cliente"
        if tipo=="cliente":
            print("|||||   Bienvenido Cliente   ||||||")
            print("1. Consultar eventos")
            print("2. Elegir un evento")
            print("3. Pagar evento")
            print("4. Consultar eventos pagados")
            print("5. Salir")
            op4= input("Elija una opcion: ")
            if op4=="1":
                 consultarEventosCliente(correo)
            elif op4=="2":
                elegirEventoCliente(correo)
            elif op4=="3":
                pagarEventoCliente(correo)
            elif op4=="4":
                consultarEventoPagadoCliente(correo)
            elif op4=="5":
                verdad3=False
                

    print(tipo)
    print(correo)








#CreacionCuentaArtista("tago2000@hotmail.com","tago","tumbaco","disenador","un crack")
#consultarEventosViejos("thiago@hotmail.com")
#buscarAsistentes(12345)
#menuEasy()
Menu()
