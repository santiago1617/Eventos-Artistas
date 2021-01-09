    def getConection():
        conection = pymysql.connect(
            host="local",
            user="root",
            password="Tu3st4sl0c0@",
            db="application"
        )
        return conection

    def conversor(tupla):
        cadena = " "
        for elemento in tupla:
            cadena = cadena + (str(elemento) + "| ")
        return cadena

    def creacionCuentaCliente(correo, nombre, apellido):
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute(
            "INSERT INTO Artista(correo,nombre,apellido)  VALUES(('" + correo + "','" + nombre + "','" + apellido + "')")
        conection.commit()
        cursor.close()
        conection.close()
        print("Cuenta Creada")

    def consultarEventosCliente(correo):
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("Select * "
                       "from evento join asistencia on evento.IdEvento=asistencia.evento"
                       "join cliente on asistencia.cliente=cliente.correo"
                       "where cliente.correo='" + correo + "' and asistencia.asiste")
        datos = cursor.fetchall()
        cursor.close()
        conection.close()
        print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
        for fila in datos:
            print(conversor(fila))

    def elegirEventoCliente(evento):
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("Select * from evento Where evento.IdEvento='" + evento + "'")
        conection.commit()
        cursor.close()
        conection.close()
        print("Evento seleccionado")

    ''' def pagoTarjetaCredito(evento):
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("Select * from evento join Where evento.IdEvento='" + evento + "'")
'''

    def consultarEventosPagados(evento, correo):
        conection = getConection()
        cursor = conection.cursor()
        cursor.execute("Select * from evento join pago on evento.IdEvento=pago.evento"
                       "join cliente pago.cliente=cliente.correo "
                       "Where evento.IdEvento='" + evento + "'"
                        "and pago.correo='" + correo + "' and pagado=TRUE ")
        datos = cursor.fetchall()
        cursor.close()
        conection.close()
        print("ID_Evento/  Titulo/   Descripcion/    Duracion/   FechaInicio/   Tipo/   Costo/   Correo_Artista")
        for fila in datos:
            print(conversor(fila))