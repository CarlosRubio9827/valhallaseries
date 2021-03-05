from flask import render_template, Response, make_response, request, redirect,url_for, flash, session, json, jsonify, logging, send_file

from datetime import date
from datetime import datetime
from . import kmvertical
from app.db import *
#Configuración de sesion . permanete
@kmvertical.before_request
def session_management():
  session.permanent = True
  

@kmvertical.route('/kmvertical')
def kmverticalI():

  session['entreno'] = False
  session["carrera"] = False
  session['kmVertical'] = True
  session["loggedInKmVertical"] = False

  return redirect(url_for("kmvertical.kmverticalLogin"))


@kmvertical.route('/kmvertical/login')
def kmverticalLogin():
  cur = mysql.connection.cursor()
  messages = []
  session['login'] = "active"
  session['registro'] = ""
  if session["loggedInKmVertical"] == True:
    session['kmVertical'] = False
    nuip = session["nuip"]
    email = session["email"]
    
    cur.execute("SELECT * FROM usuarioskmvertical WHERE correoElectronico = (%s) and numeroIdentificacion = (%s)", (email, nuip))
    usuario = cur.fetchone()
    if usuario:
      usuario = list(usuario)

# 11, 'CArlos', 'Rubio', 5, 33, 'ejemplo@ejemplo.com', 2, '123456', datetime.date(2021, 2, 9),
# 1, '3157873181', 'Palmira', 1, 'Coomeva', 13, '', '', 1, 1, 26, datetime.datetime(2021, 2, 19, 19, 21, 23, 10000)]

      #Tipo Identificación
      tipoIdentificacion = usuario[6]
      cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
      tipoIdentificacion = cur.fetchone()
      tipoIdentificacion = tipoIdentificacion[1]
      usuario[6] = tipoIdentificacion
      
      #Sexos   
      sexo = usuario[9]
      cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
      sexo = cur.fetchone()
      sexo = sexo[1]
      usuario[9] = sexo

      #Distancia
      valorKmvertical = int(usuario[3])
      usuario[3] = valorKmvertical
       
      #Tipo Sangre
      tipoSangre = usuario[12]
      cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
      tipoSangre = cur.fetchone()
      tipoSangre = tipoSangre[1]
        
      usuario[12] = tipoSangre  

      #Talla Camisa
      tallaCamisa = usuario[14]
      cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
      tallaCamisa = cur.fetchone()
      tallaCamisa = tallaCamisa[1]
      usuario[14] = tallaCamisa

      #Categoria
      categoria = usuario[4]
      cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
      categoria = cur.fetchone()
      categoria = categoria[1]
      usuario[4] = categoria

      #Estado Inscripción
      estadoInscripcion = usuario[17]
      cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
      estadoInscripcion = cur.fetchone()
      estadoInscripcion = estadoInscripcion[1]
      usuario[17] = estadoInscripcion
  
      #Estado Kit
      estadoKit = usuario[18]
      cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
      estadoKit = cur.fetchone()
      estadoKit = estadoKit[1]
      usuario[18] = estadoKit

      #Código Equipo
      codigoEquipo = usuario[19]
      cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
      codigoEquipo = cur.fetchone()
      codigoEquipo = codigoEquipo[1]
      usuario[19] = codigoEquipo

      #Fecha de Reistro
      fechaRegistro = str(usuario[20])
      fechaRegistro = fechaRegistro[0:10]
      usuario[20] = fechaRegistro   

      #Inicialización de Cookies para la sesión
      session['loggedInKmVertical'] = True
      session['nuip'] = nuip
      session['email'] = email
      messages = []
      messages.append("info")
      messages.append("Bienvenido al Km Vertical - Valhalla Series")

      return render_template("stateKmvertical.html", messages=messages, usuario=usuario)
  messages.append("0")
  messages.append("1")

  return render_template("loginKmvertical.html", messages=messages)

#Método de login
@kmvertical.route("/kmvertical/login", methods=["POST"])
def kmverticalLoginPost():
  
  if request.method == "POST":
    email = request.form["email"] 
    nuip = request.form["numeroIdentificacion"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarioskmvertical WHERE correoElectronico = (%s) and numeroIdentificacion = (%s)", (email, nuip))
    usuario = cur.fetchone()
    if usuario:
      usuario = list(usuario)

      #Tipo Identificación
      tipoIdentificacion = usuario[6]
      cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
      tipoIdentificacion = cur.fetchone()
      tipoIdentificacion = tipoIdentificacion[1]
      usuario[6] = tipoIdentificacion
      
      #Sexos   
      sexo = usuario[9]
      cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
      sexo = cur.fetchone()
      sexo = sexo[1]
      usuario[9] = sexo
      
      # Valor Km VErtical
      valorKmvertical = int(usuario[3])
      usuario[3] = valorKmvertical
      
      #Tipo Sangre
      tipoSangre = usuario[12]
      cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
      tipoSangre = cur.fetchone()
      tipoSangre = tipoSangre[1]
      usuario[12] = tipoSangre  

      #Talla Camisa
      tallaCamisa = usuario[14]
      cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
      tallaCamisa = cur.fetchone()
      tallaCamisa = tallaCamisa[1]
      usuario[14] = tallaCamisa

      #Categoria
      categoria = usuario[4]
      cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
      categoria = cur.fetchone()
      categoria = categoria[1]
      usuario[4] = categoria

      #Estado Inscripción
      estadoInscripcion = usuario[17]
      cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
      estadoInscripcion = cur.fetchone()
      estadoInscripcion = estadoInscripcion[1]
      usuario[17] = estadoInscripcion
      
      #Estado Kit
      estadoKit = usuario[18]
      cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
      estadoKit = cur.fetchone()
      estadoKit = estadoKit[1]
      usuario[18] = estadoKit

      #Código Equipo
      codigoEquipo = usuario[19]
      cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
      codigoEquipo = cur.fetchone()
      codigoEquipo = codigoEquipo[1]
      usuario[19] = codigoEquipo

      #Fecha de Reistro
      fechaRegistro = str(usuario[20])
      fechaRegistro = fechaRegistro[0:10]
      usuario[20] = fechaRegistro   

      #Inicialización de Cookies para la sesión
      session['loggedInKmVertical'] = True
      session['kmVertical'] = False
      session['nuip'] = nuip
      session['email'] = email
      messages = []
      messages.append("info")
      messages.append("Bienvenido al Kmvertical - Valhalla Series")
      return render_template("stateKmvertical.html", messages=messages, usuario=usuario)
    else:
      messages = []
      messages.append("error")
      messages.append("Credenciales Incorrectas") 
      return render_template("loginKmvertical.html", messages=messages)

@kmvertical.route("/kmvertical/logout", methods=["POST"])
def estado():
  if request.method == "POST":
    session['loggedInKmVertical'] = False
    session['kmVertical'] = True
    
    return  redirect(url_for("public.home"))
    

#Ruta registro
@kmvertical.route("/kmvertical/registro")
def kmverticalRegistro():
  #Conexión a la base de datos
  cur = mysql.connection.cursor()

  session['registro'] = "active"
  session['login'] = ""
  messages = []
  if session["loggedInKmVertical"] == True:
    return  redirect(url_for("kmvertical.kmverticalLogin"))
    
  messages.append("0")
  messages.append("1")

  
  #Consutal Sexo
  cur.execute("SELECT * FROM sexo")
  sexos = cur.fetchall()
  
  #Consutal Tallas camisa
  cur.execute("SELECT * FROM tallacamisa")
  tallaCamisas = cur.fetchall()
  
  #Consutal Tipo identificación
  cur.execute("SELECT * FROM tipoidentificacion")
  tiposIdentificacion = cur.fetchall()
  
  #Consutal Tipo Sangre
  cur.execute("SELECT * FROM tiposangre")
  tiposSangre = cur.fetchall()
  tiposSangre = list(tiposSangre)
  tiposSangre.pop()

  # Consultar Estado Evento - Entreno
  cur.execute("SELECT * FROM eventos where nombre = (%s)",["Km Vertical"])
  estadoEntreno = cur.fetchone()
  estadoEntreno = estadoEntreno[2]

  
  return render_template("registroKmvertical.html", messages=messages,sexos=sexos,tallaCamisas=tallaCamisas,tiposIdentificacion=tiposIdentificacion,tiposSangre=tiposSangre,estadoEntreno=estadoEntreno)

#Método de Registro
@kmvertical.route("/kmvertical/registro", methods=["POST"])
def kmverticalRegistroPost():
  if request.method == "POST":
    cur = mysql.connection.cursor()
    nombre = request.form['nombre']
    apellidos = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    ciudad = request.form['ciudad']
    entidadSalud = request.form['seguroMedico']
    nombreContactoEmergencia = request.form['nombreContactoEmergencia']
    telefonoContactoEmergencia = request.form['numeroContactoEmergencia']
    fechaNacimiento = request.form['fechaNacimiento']
    numeroIdentificacion = request.form['numeroIdentificacion']
    
    #Tipo Identificación
    tipoIdentificacion = request.form['tipoIdentificacion']
    cur.execute("SELECT * FROM tipoIdentificacion WHERE inicialesTipoIdentificacion = (%s)", [tipoIdentificacion])
    tipoIdentificacion = cur.fetchone()
    tipoIdentificacion = tipoIdentificacion[0]

    #Sexos
    sexo = request.form['sexo']
    cur.execute("SELECT * FROM sexo WHERE nombreSexo = (%s)", [sexo])
    sexo = cur.fetchone()
    sexo2 = sexo[1]
    sexo = sexo[0]

    #Distancia
    valorKmvertical = "60000"
    
    #Tipo Sangre
    tipoSangre = request.form['tipoSangre']
    cur.execute("SELECT * FROM tiposangre WHERE nombreTipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()
    tipoSangre = tipoSangre[0]  

    #Talla Camisa
    tallaCamisa = "No aplica"
    cur.execute("SELECT * FROM tallacamisa WHERE tamañoTalla = (%s)", [tallaCamisa])
    tallaCamisa = cur.fetchone()
    tallaCamisa = tallaCamisa[0]

    #Categoria
    now = datetime.now()    
    fechaNacimiento = int(fechaNacimiento[0:4])
    edad = (int(format(now.year)) - int(fechaNacimiento))
    fechaNacimiento = request.form['fechaNacimiento']
    # cur.execute("SELECT * FROM categorias WHERE rangoMin <= (%s) and rangoMax > (%s) and sexo = (%s) and distancia = (%s)", (edad,edad, sexo2, distancia2))
    # categoria = cur.fetchone()
    categoria = "33"
    
    #Código Equipo
    codigoEquipo = ""
    cur.execute("SELECT * FROM equipos WHERE codigoEquipo = (%s)", [codigoEquipo])
    codigoEquipo = cur.fetchone()
    codigoEquipo = codigoEquipo[0]

    # cur.execute("SET NAMES utf8;")
    # cur.execute("SET CHARACTER SET utf8;")
    # cur.execute("SET character_set_connection=utf8;")
    sql = """INSERT INTO usuarioskmvertical (nombreUsuario,apellidosUsuario,valorKmvertical,categorias_idcategorias,correoElectronico,
    tipoIdentificacion_idtipoIdentificacion,numeroIdentificacion,fechaNacimiento,sexo_idsexo,telefono,ciudad, 
    tipoSangre_idtipoSangre,entidadSalud,tallaCamisa_idtallaCamisa,contactoEmergenciaNombre,contactoEmergenciaApellido,
    estadoInscripcion_idestadoInscripcion,estadoKit_idestadoKit,equipos_idequipos,fechaRegistro)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (nombre,apellidos,str(valorKmvertical),str(categoria),email,str(tipoIdentificacion),numeroIdentificacion,
    fechaNacimiento,str(sexo),telefono,ciudad,str(tipoSangre),entidadSalud,
    str(tallaCamisa),nombreContactoEmergencia,telefonoContactoEmergencia,(1),(1),str(codigoEquipo),str(now))
     
    cur.execute(sql, values)
    mysql.connection.commit()
    cur.execute("SELECT * FROM usuarioskmvertical WHERE numeroIdentificacion = (%s) and correoElectronico = (%s)", (numeroIdentificacion, email))
    data = cur.fetchall()
    usuario = data[0]   
      
    if usuario:
      session["loggedInKmVertical"] = True
      session["email"] = email
      session["nuip"] = numeroIdentificacion
      return  redirect(url_for("kmvertical.kmverticalLogin"))
    #Limpiar session
    
    return redirect(url_for("kmvertical.kmverticalRegistro"))


#Verificar código de equipo y número de identificación
@kmvertical.route("/kmvertical/verificacionRegistro", methods=["POST"])
def verificacionRegistro():
  if request.method == "POST":

    try:
      nuip = request.form["nuip"]
      cod = request.form["cod"]
      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM equipos WHERE codigoEquipo = (%s)", [cod])
      dataCodigo = cur.fetchall()
      #print(dataCodigo[0])
            
      cur.execute("SELECT * FROM usuarios WHERE numeroIdentificacion = (%s)", [nuip])
      dataNuip = cur.fetchall()
      
      if dataCodigo and (not dataNuip):
        return jsonify({
          "status":200,
          "existeTodo": True,
          "existeNuip": True,
          "existeCod": True
        })
      elif dataNuip:
        return jsonify({
          "status":200,
          "existeTodo": False,
          "existeNuip": True,
          "existeCod": False
        })
      elif not dataCodigo:
        return jsonify({
          "status":200,
          "existeTodo": False,
          "existeNuip": False,
          "existeCod": False
        })
#Fin de try        
    except expression as identifier:
      return jsonify({
        "status": 500
      })