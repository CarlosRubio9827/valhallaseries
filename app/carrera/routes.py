from flask import render_template, Response, make_response, request, redirect,url_for, flash, session, json, jsonify, logging, send_file

from datetime import date
from datetime import datetime
from . import carrera
from app.db import *
#Configuración de sesion . permanete
@carrera.before_request
def session_management():
  session.permanent = True

@carrera.route('/carrera')
def carreraI():
  session["loggedin"] = False
  return redirect(url_for("carrera.carreraLogin"))

@carrera.route('/carrera/login')
def carreraLogin():
  cur = mysql.connection.cursor()
  messages = []
  session['login'] = "active"
  session['registro'] = ""
  if session["loggedin"] == True:
    nuip = session["nuip"]
    email = session["email"]
    
    cur.execute("SELECT * FROM usuarios WHERE correoElectronico = (%s) and numeroIdentificacion = (%s)", (email, nuip))
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

      #Distancia
      distancia = usuario[3]
      cur.execute("SELECT * FROM distancias WHERE iddistancias = (%s)", [distancia])
      distancia = cur.fetchone()
      usuario[3] = distancia
       
      #Tipo Sangre
      tipoSangre = usuario[14]
      cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
      tipoSangre = cur.fetchone()
      tipoSangre = tipoSangre[1]
      usuario[14] = tipoSangre  

      #Talla Camisa
      tallaCamisa = usuario[16]
      cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
      tallaCamisa = cur.fetchone()
      tallaCamisa = tallaCamisa[1]
      usuario[16] = tallaCamisa

      #Categoria
      categoria = usuario[4]
      cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
      categoria = cur.fetchone()
      categoria = categoria[1]
      usuario[4] = categoria

      #Estado Inscripción
      estadoInscripcion = usuario[19]
      cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
      estadoInscripcion = cur.fetchone()
      estadoInscripcion = estadoInscripcion[1]
      usuario[19] = estadoInscripcion
  
      #Estado Kit
      estadoKit = usuario[20]
      cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
      estadoKit = cur.fetchone()
      estadoKit = estadoKit[1]
      usuario[20] = estadoKit

      #Código Equipo
      codigoEquipo = usuario[21]
      cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
      codigoEquipo = cur.fetchone()
      codigoEquipo = codigoEquipo[1]
      usuario[21] = codigoEquipo

      #Fecha de Reistro
      fechaRegistro = str(usuario[22])
      fechaRegistro = fechaRegistro[0:10]
      usuario[22] = fechaRegistro   

      #Inicialización de Cookies para la sesión
      session['loggedin'] = True
      session['nuip'] = nuip
      session['email'] = email
      messages = []
      messages.append("info")
      messages.append("Bienvenido a la carrera de Valhalla Series")
      return render_template("stateCarrera.html", messages=messages, usuario=usuario)
  messages.append("0")
  messages.append("1")

  return render_template("loginCarrera.html", messages=messages)

#Método de login
@carrera.route("/carrera/login", methods=["POST"])
def carreraLoginPost():
  
  if request.method == "POST":
    email = request.form["email"] 
    nuip = request.form["numeroIdentificacion"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE correoElectronico = (%s) and numeroIdentificacion = (%s)", (email, nuip))
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

      #Distancia
      distancia = usuario[3]
      cur.execute("SELECT * FROM distancias WHERE iddistancias = (%s)", [distancia])
      distancia = cur.fetchone()
      usuario[3] = distancia
       
      #Tipo Sangre
      tipoSangre = usuario[14]
      cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
      tipoSangre = cur.fetchone()
      tipoSangre = tipoSangre[1]
      usuario[14] = tipoSangre  

      #Talla Camisa
      tallaCamisa = usuario[16]
      cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
      tallaCamisa = cur.fetchone()
      tallaCamisa = tallaCamisa[1]
      usuario[16] = tallaCamisa

      #Categoria
      categoria = usuario[4]
      cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
      categoria = cur.fetchone()
      categoria = categoria[1]
      usuario[4] = categoria

      #Estado Inscripción
      estadoInscripcion = usuario[19]
      cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
      estadoInscripcion = cur.fetchone()
      estadoInscripcion = estadoInscripcion[1]
      usuario[19] = estadoInscripcion
      
      #Estado Kit
      estadoKit = usuario[20]
      cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
      estadoKit = cur.fetchone()
      estadoKit = estadoKit[1]
      usuario[20] = estadoKit

      #Código Equipo
      codigoEquipo = usuario[21]
      cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
      codigoEquipo = cur.fetchone()
      codigoEquipo = codigoEquipo[1]
      usuario[21] = codigoEquipo

      #Fecha de Reistro
      fechaRegistro = str(usuario[22])
      fechaRegistro = fechaRegistro[0:10]
      usuario[22] = fechaRegistro   

      #Inicialización de Cookies para la sesión
      session['loggedin'] = True
      session['nuip'] = nuip
      session['email'] = email
      messages = []
      messages.append("info")
      messages.append("Bienvenido a la piedra del Canadá")
      return render_template("stateCarrera.html", messages=messages, usuario=usuario)
    else:
      messages = []
      messages.append("error")
      messages.append("Credenciales Incorrectas") 
      return render_template("loginCarrera.html", messages=messages)

@carrera.route("/carrera/logout", methods=["POST"])
def estado():
  if request.method == "POST":
    session['loggedin'] = False
    
    return  redirect(url_for("public.home"))
    

#Ruta registro
@carrera.route("/carrera/registro")
def carreraRegistro():
  #Conexión a la base de datos
  cur = mysql.connection.cursor()

  session['registro'] = "active"
  session['login'] = ""
  messages = []
  if session["loggedin"] == True:
    return  redirect(url_for("carrera.carreraLogin"))
    
  messages.append("0")
  messages.append("1")

  #Consutal Distancias
  cur.execute("SELECT * FROM distancias")
  distancias = cur.fetchall()
  
  
  #Consutal Sexo
  cur.execute("SELECT * FROM sexo")
  sexos = cur.fetchall()
  
  #Consutal Tallas camisa
  cur.execute("SELECT * FROM tallacamisa")
  tallaCamisas = list(cur.fetchall())
  tallaCamisas.pop()
  
  #Consutal Tipo identificación
  cur.execute("SELECT * FROM tipoidentificacion")
  tiposIdentificacion = cur.fetchall()
  
  #Consutal Tipo Sangre
  cur.execute("SELECT * FROM tiposangre")
  tiposSangre = list(cur.fetchall())
  tiposSangre.pop()

  # Consultar Estado Evento - Entreno
  cur.execute("SELECT * FROM eventos where nombre = (%s)",["Carrera"])
  estadoEntreno = cur.fetchone()
  estadoEntreno = estadoEntreno[2]
  
  return render_template("registroCarrera.html", messages=messages,distancias=distancias,sexos=sexos,tallaCamisas=tallaCamisas,tiposIdentificacion=tiposIdentificacion,tiposSangre=tiposSangre,estadoEntreno=estadoEntreno)

#Método de Registro
@carrera.route("/carrera/registro", methods=["POST"])
def carreraRegistroPost():
  if request.method == "POST":
    cur = mysql.connection.cursor()
    nombre = request.form['nombre']
    apellidos = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    pais = request.form['pais']
    departamento = request.form['departamento']
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
    distancia = request.form['distancia']
    cur.execute("SELECT * FROM distancias WHERE nombreDistancia = (%s)", [distancia])
    distancia = cur.fetchone()
    distancia2 = distancia[1]
    distancia = distancia[0]
    
    #Tipo Sangre
    tipoSangre = request.form['tipoSangre']
    cur.execute("SELECT * FROM tiposangre WHERE nombreTipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()
    tipoSangre = tipoSangre[0]  

    #Talla Camisa
    tallaCamisa = request.form['tallaCamisa']
    cur.execute("SELECT * FROM tallacamisa WHERE tamañoTalla = (%s)", [tallaCamisa])
    tallaCamisa = cur.fetchone()
    tallaCamisa = tallaCamisa[0]

    #Categoria
    now = datetime.now()    
    fechaNacimiento = int(fechaNacimiento[0:4])
    edad = (int(format(now.year)) - int(fechaNacimiento))
    fechaNacimiento = request.form['fechaNacimiento']
    cur.execute("SELECT * FROM categorias WHERE rangoMin <= (%s) and rangoMax > (%s) and sexo = (%s) and distancia = (%s)", (edad,edad, sexo2, distancia2))
    categoria = cur.fetchone()
    categoria = categoria[0]
    
    #Código Equipo
    codigoEquipo = request.form["codigoGrupo"]
    cur.execute("SELECT * FROM equipos WHERE codigoEquipo = (%s)", [codigoEquipo])
    codigoEquipo = cur.fetchone()
    codigoEquipo = codigoEquipo[0]

    # cur.execute("SET NAMES utf8;")
    # cur.execute("SET CHARACTER SET utf8;")
    # cur.execute("SET character_set_connection=utf8;")
    sql = """INSERT INTO usuarios (nombreUsuario,apellidosUsuario,distancias_iddistancias,categorias_idcategorias,correoElectronico,
    tipoIdentificacion_idtipoIdentificacion,numeroIdentificacion,fechaNacimiento,sexo_idsexo,telefono,pais,departamento,ciudad, 
    tipoSangre_idtipoSangre,entidadSalud,tallaCamisa_idtallaCamisa,contactoEmergenciaNombre,contactoEmergenciaApellido,
    estadoInscripcion_idestadoInscripcion,estadoKit_idestadoKit,equipos_idequipos,fechaRegistro)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (nombre,apellidos,str(distancia),str(categoria),email,str(tipoIdentificacion),numeroIdentificacion,
    fechaNacimiento,str(sexo),telefono,pais,departamento,ciudad,str(tipoSangre),entidadSalud,
    str(tallaCamisa),nombreContactoEmergencia,telefonoContactoEmergencia,(1),(1),str(codigoEquipo),str(now))
     
    cur.execute(sql, values)
    mysql.connection.commit()
    cur.execute("SELECT * FROM usuarios WHERE numeroIdentificacion = (%s) and correoElectronico = (%s)", (numeroIdentificacion, email))
    data = cur.fetchall()
    usuario = data[0]   
      
    if usuario:
      session["loggedin"] = True
      session["email"] = email
      session["nuip"] = numeroIdentificacion
      return  redirect(url_for("carrera.carreraLogin"))
    #Limpiar session
    
    return redirect(url_for("carrera.carreraRegistro"))


#Verificar código de equipo y número de identificación
@carrera.route("/carrera/verificacionRegistro", methods=["POST"])
def carreraVerificacionRegistro():
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