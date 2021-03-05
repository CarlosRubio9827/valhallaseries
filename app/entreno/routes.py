from flask import render_template, Response, make_response, request, redirect,url_for, flash, session, json, jsonify, logging, send_file

from datetime import date
from datetime import datetime
from . import entreno
from app.db import *
#Configuración de sesion . permanete
@entreno.before_request
def session_management():
  session.permanent = True


@entreno.route('/entreno')
def entrenoI():
  session["registered"] = False
  session['registro'] = ""
  session['login'] = ""
  session['entreno'] = True
  return redirect(url_for("entreno.entrenoRegistro"))

#Ruta registro
@entreno.route("/entreno/registro")
def entrenoRegistro():
  #Conexión a la base de datos
  cur = mysql.connection.cursor()
  messages = []

  #Consutal Tipo identificación
  cur.execute("SELECT * FROM tipoidentificacion")
  tiposIdentificacion = cur.fetchall()

  # Consultar Estado Evento - Entreno
  cur.execute("SELECT * FROM eventos where nombre = (%s)",["entreno"])
  estadoEntreno = cur.fetchone()
  estadoEntreno = estadoEntreno[2]


  if session["registered"] == True:
    messages.append("info")
    messages.append("Se ha registrado correctamente en el entreno")
    session["registered"] = False
    return render_template("registroEntreno.html", messages=messages,tiposIdentificacion=tiposIdentificacion,estadoEntreno=estadoEntreno)
  
  messages.append("0")
  messages.append("1")
  return render_template("registroEntreno.html", messages=messages,tiposIdentificacion=tiposIdentificacion,estadoEntreno=estadoEntreno)

#Método de Registro
@entreno.route("/entreno/registro", methods=["POST"])
def entrenoRegistroPost():
  if request.method == "POST":
    cur = mysql.connection.cursor()
    nombre = request.form['nombre']
    apellidos = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    estado = "Pendiente"
    
    now = datetime.now()   
    # cur.execute("SET NAMES utf8;")
    # cur.execute("SET CHARACTER SET utf8;")
    # cur.execute("SET character_set_connection=utf8;")
    sql = """INSERT INTO usuariosentreno (nombre,apellidos,email,telefono,fecharegistro, estado)
    VALUES (%s,%s,%s,%s,%s,%s)"""
    values = (nombre,apellidos,email,telefono,str(now),estado)
     
    cur.execute(sql, values)
    mysql.connection.commit()
    cur.execute("SELECT * FROM usuariosentreno WHERE nombre = (%s) and apellidos = (%s) and email = (%s)", (nombre, apellidos, email))
    data = cur.fetchall()
    usuario = data[0]   
      
    if usuario:
      session["registered"] = True
      return  redirect(url_for("entreno.entrenoRegistro"))
    #Limpiar session
    
    return redirect(url_for("entreno.entrenoRegistro"))


#Verificar código de equipo y número de identificación
@entreno.route("/verificacionRegistroEntreno", methods=["POST"])
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
