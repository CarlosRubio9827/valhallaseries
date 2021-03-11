from flask import render_template, Response, make_response, request, redirect,url_for, flash, session, json, jsonify, logging, send_file
import re
import pdfkit
import io
import xlwt
from datetime import date
from datetime import datetime
from . import private
from app.db import *
#Configuración de sesion . permanete
@private.before_request
def session_management():
  session.permanent = True


@private.route("/loginAdmin")
def adminLogin():
  
 
  messages= []
  if session["loggedAdmin"] == True:
    email = session["email"]
    contraseña = session["contraseña"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
    usuario = cur.fetchone()
    if usuario:
      
      messages.append("0")
      messages.append("1")
      return render_template("dashboard.html", usuario=usuario, messages = messages)
      

      # if "messages" in session:
      #   messagesNew = session['messages']
      #   messages.append("success")
      #   messages.append(messagesNew[1])  
      # else:
      #   messages.append("0")
      #   messages.append("1")
      # return render_template("dashboard/estado.html", usuario=usuario, usuarios=usuarios,messages = messages)
    
  else:
    messages.append("0")  
    messages.append("1")
    return render_template("loginAdmin.html", messages = messages)

@private.route("/loginAdmin", methods=["POST"])
def adminLoginPost():
  messages = []
  email = request.form["email"]
  contraseña = request.form["numeroIdentificacion"]
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
  usuario = cur.fetchone()
  if usuario:
    
    
    session["loggedAdmin"] = True
    session["email"] = email
    session["contraseña"] = contraseña
    messages.append("info")
    messages.append("Bienvenido a la consulta de datos - Valhalla Series")
    return render_template("dashboard.html", usuario=usuario, messages = messages)
  else:
    messages.append("error")
    messages.append("Credenciales Incorrectos")
    return render_template("loginAdmin.html", messages=messages)

@private.route("/loginAdmin/entreno")
def adminLoginEntreno():
  messages= []
  if session["loggedAdmin"] == True:
    email = session["email"]
    contraseña = session["contraseña"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
    usuario = cur.fetchone()

    if usuario:
      cur.execute("SELECT * FROM usuariosentreno")
      usuarios = cur.fetchall()
      usuarios = list(usuarios)
      
      cur.execute("SELECT * FROM eventos WHERE nombre = (%s)", ["entreno"])
      evento = cur.fetchone()
      disponible = False
      if evento[2] == "Disponible":
        disponible = True
      else:
        disponible = False
        
      if "confirmarPago" in session:
        messagesNew = session['confirmarPago']
        messages.append("success")
        messages.append(messagesNew[1])
        session.pop('confirmarPago',None)
      else:
        messages.append("0")
        messages.append("1")
      print(disponible)
      return render_template("eventos/entreno.html",usuarios=usuarios, usuario=usuario, messages = messages, disponible=disponible)
    else:
      messages.append("error")
      messages.append("Credenciales Incorrectos")
      return render_template("loginAdmin.html", messages=messages)
  else:
    return redirect(url_for("private.adminLogin"))

@private.route("/loginAdmin/entreno/confirmarPago/<string:id>", methods=["POST"])
def loginAdminConfirmarPagoEntreno(id):
    cur = mysql.connection.cursor()
    
    cur.execute("UPDATE usuariosentreno SET estado=(%s) WHERE id = (%s)", ("Registrado", id))
    mysql.connection.commit()
    messages = []
    messages.append("confirmarPago")
    messages.append("¡Se ha guardado el pago correctamente!")
    session["confirmarPago"] = messages
     
    return redirect(url_for("private.adminLoginEntreno"))

@private.route("/loginAdmin/cambiarEstEvento/<string:evento>/<string:estado>", methods=["POST"])
def loginAdminCambiarEstadoEntreno(evento, estado):
    cur = mysql.connection.cursor()
    if evento == "kmvertical":
      evento = "Km Vertical"
    elif evento == "carrera":
      evento = "Carrera"
    
    # UPDATE `eventos` SET `estado` = 'No Disponible' WHERE `eventos`.`id` = 1;
    if estado == "desactivar":
      estado = "No Disponible"
      cur.execute("UPDATE eventos SET estado=(%s) WHERE nombre = (%s)", (estado, evento))
      mysql.connection.commit()
      messages = []
      messages.append("confirmarPago")
      messages.append("¡Se ha cambiado el estado del evento correctamente!")
      session["confirmarPago"] = messages

      if evento == "entreno":
        return redirect(url_for("private.adminLoginEntreno"))
      elif evento == "Km Vertical":
        return redirect(url_for("private.adminLoginKmVertical"))
      else:
        return redirect(url_for("private.adminLoginCarrera"))
      
    elif estado == "activar":
      estado = "Disponible"
      cur.execute("UPDATE eventos SET estado=(%s) WHERE nombre = (%s)", (estado, evento))
      mysql.connection.commit()
      messages = []
      messages.append("confirmarPago")
      messages.append("¡Se ha cambiado el estado del evento correctamente!")
      session["confirmarPago"] = messages

      if evento == "entreno":
        return redirect(url_for("private.adminLoginEntreno"))
      elif evento == "Km Vertical":
        return redirect(url_for("private.adminLoginKmVertical")) 
      else:
        return redirect(url_for("private.adminLoginCarrera"))

# Exportar PDF
@private.route("/loginAdmin/entreno/exportarPdf")
def entrenoExportarPdf():
  
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuariosentreno` ORDER BY `usuariosentreno`.`fecharegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
  now = datetime.now()
  fecha = []
  fecha.append(now.year)
  fecha.append(now.month)
  fecha.append(now.day)
  fecha.append(now.hour)
  fecha.append(now.minute)
  fecha.append(now.second)
  
  rendered = render_template("export/entrenoPdf.html", usuarios=usuarios, fecha=fecha)

  config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

  pdf = pdfkit.from_string(rendered, False, configuration=config)
  response = make_response(pdf)
  response.headers["Content-Type"] = "application/pdf"
  response.headers["Content-Disposition"] = "inline; filename=output.pdf"
  return response
  
   
# Ruta para exportar a Excel
@private.route("/loginAdmin/entreno/exportarExcel")
def entrenoExportarExcel():
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuariosentreno` ORDER BY `usuariosentreno`.`fecharegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
 
  #output in bytes
  output = io.BytesIO()
  #create WorkBook object
  workbook = xlwt.Workbook()
  #add a sheet
  sh = workbook.add_sheet('Reporte de Usuarios')
   
  #add headers
  sh.write(0, 0, 'Id')
  sh.write(0, 1, 'Nombre')
  sh.write(0, 2, 'Apellido')
  sh.write(0, 3, 'Correo')
  sh.write(0, 4, 'Teléfono')
  sh.write(0, 5, 'Estado Insc.')
  sh.write(0, 6, 'Fecha Reg.')
  

  idx = 0
  for user in usuarios:
    
    fechaInsc = str(user[5])
    sh.write(idx+1, 0, idx+1)
    sh.write(idx+1, 1, user[1])
    sh.write(idx+1, 2, user[2])
    sh.write(idx+1, 3, user[3])
    sh.write(idx+1, 4, user[4])
    sh.write(idx+1, 5, user[6])
    sh.write(idx+1, 6, fechaInsc)
    idx += 1
    
  workbook.save(output)
  output.seek(0)
  now = datetime.now()
  

  nameFile = "Valhalla Series - Entreno - " + str(now)
  return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename="+nameFile+".xls"})

# Km Vertical ---------------------------------------------------------------------------------------------------------------------------------------
@private.route("/loginAdmin/kmvertical")
def adminLoginKmVertical():
  messages= []
  if session["loggedAdmin"] == True:
    email = session["email"]
    contraseña = session["contraseña"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
    usuario = cur.fetchone()

    if usuario:
      cur.execute("SELECT * FROM usuarioskmvertical")
      usuarios = cur.fetchall()
      usuarios = list(usuarios)
    
      usuarios2 = []
      for x in range(0, len(usuarios)):
        user = list(usuarios[x])
        
        #Tipo Identificación
        tipoIdentificacion = user[6]
        cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
        tipoIdentificacion = cur.fetchone()
        tipoIdentificacion = tipoIdentificacion[1]
        user[6] = tipoIdentificacion
            
        #Sexo
        sexo = user[9]
        cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
        sexo = cur.fetchone()
        sexo = sexo[1]
        user[9] = sexo
    
          
        #Tipo Sangre
        tipoSangre = user[12]  
        cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
        tipoSangre = cur.fetchone()     
        tipoSangre = tipoSangre[1]
        user[12] = tipoSangre  

        #Talla Camisa
        tallaCamisa = user[14]
        cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
        tallaCamisa = cur.fetchone()
        tallaCamisa = tallaCamisa[1]
        user[14] = tallaCamisa

        #Categoria
        categoria = user[4]
        cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
        categoria = cur.fetchone()
        categoria = categoria[1]
        user[4] = categoria

        #Estado Inscripción
        estadoInscripcion = user[17]
        cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
        estadoInscripcion = cur.fetchone()
        estadoInscripcion = estadoInscripcion[1]
        user[17] = estadoInscripcion
        
        #Estado Kit
        estadoKit = user[18]
        cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
        estadoKit = cur.fetchone()
        estadoKit = estadoKit[1]
        user[18] = estadoKit
      
        #Código Equipo
        codigoEquipo = user[19]     
        cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
        codigoEquipo = cur.fetchone()
        codigoEquipo = codigoEquipo[1]
        user[19] = codigoEquipo

        #Fecha de Reistro
        fechaRegistro = str(user[20])
        fechaRegistro = fechaRegistro[0:10]
        user[20] = fechaRegistro
        usuarios2.append(user)
      usuarios = usuarios2  
      
      cur.execute("SELECT * FROM eventos WHERE nombre = (%s)", ["Km Vertical"])
      evento = cur.fetchone()
      disponible = False
      if evento[2] == "Disponible":
        disponible = True
      else:
        disponible = False
        
      if "confirmarPago" in session:
        messagesNew = session['confirmarPago']
        messages.append("success")
        messages.append(messagesNew[1])
        session.pop('confirmarPago',None)
      else:
        messages.append("0")
        messages.append("1")

      return render_template("eventos/kmVertical.html",usuarios=usuarios, usuario=usuario, messages = messages, disponible=disponible)
    else:
      messages.append("error")
      messages.append("Credenciales Incorrectos")
      return render_template("loginAdmin.html", messages=messages)
  else:
    return redirect(url_for("private.adminLogin"))



#Mostrar Usuario KmVertical

@private.route("/loginAdmin/kmvertical/mostrarUsuario/<string:id>")
def mostrarUsuarioKmVertical(id):
    if session["loggedAdmin"] == True:
      messages= []
      if session["loggedAdmin"] == True:
        email = session["email"]
        contraseña = session["contraseña"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
        usuario = cur.fetchone()

      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM usuarioskmvertical WHERE idusuarios=(%s)", [id])
      usuariokm = cur.fetchone()
      if usuariokm:
        usuariokm = list(usuariokm)

        #Tipo Identificación
        tipoIdentificacion = usuariokm[6]
        cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
        tipoIdentificacion = cur.fetchone()
        tipoIdentificacion = tipoIdentificacion[1]
        usuariokm[6] = tipoIdentificacion
        
        #Sexos   
        sexo = usuariokm[9]
        cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
        sexo = cur.fetchone()
        sexo = sexo[1]
        usuariokm[9] = sexo

        # #Distancia
        # distancia = usuario[3]
        # cur.execute("SELECT * FROM distancias WHERE iddistancias = (%s)", [distancia])
        # distancia = cur.fetchone()
        # usuario[3] = distancia
        
        #Tipo Sangre
        tipoSangre = usuariokm[12]
        cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
        tipoSangre = cur.fetchone()
        tipoSangre = tipoSangre[1]
        usuariokm[12] = tipoSangre  

        #Talla Camisa
        tallaCamisa = usuariokm[14]
        cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
        tallaCamisa = cur.fetchone()
        tallaCamisa = tallaCamisa[1]
        usuariokm[14] = tallaCamisa

        #Categoria
        # categoria = usuario[4]
        # cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
        # categoria = cur.fetchone()
        # categoria = categoria[1]
        # usuario[4] = categoria

        #Estado Inscripción
        estadoInscripcion = usuariokm[17]
        cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
        estadoInscripcion = cur.fetchone()
        estadoInscripcion = estadoInscripcion[1]
        usuariokm[17] = estadoInscripcion
    
        #Estado Kit
        # estadoKit = usuario[20]
        # cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
        # estadoKit = cur.fetchone()
        # estadoKit = estadoKit[1]
        # usuario[20] = estadoKit

        #Código Equipo
        # codigoEquipo = usuario[21]
        # cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
        # codigoEquipo = cur.fetchone()
        # codigoEquipo = codigoEquipo[1]
        # usuario[21] = codigoEquipo

        #Fecha de Reistro
        fechaRegistro = str(usuariokm[20])
        fechaRegistro = fechaRegistro[0:10]
        usuariokm[20] = fechaRegistro 
        messages = []
        messages.append("info")
        messages.append("Información de "+usuariokm[1]+" "+usuariokm[2]) 
        return render_template("info/mostrarUsuarioKmVertical.html", messages=messages, usuariokm=usuariokm, usuario=usuario)
      else:
        return redirect(url_for("private.adminLoginEntreno"))
    else:
      return redirect(url_for("private.adminLoginEntreno"))
#confirmar PAgo
@private.route("/loginAdmin/kmvertical/confirmarPago/<string:id>", methods=["POST"])
def loginAdminConfirmarPagoKmvertical(id):
    cur = mysql.connection.cursor()
    
    cur.execute("UPDATE usuarioskmvertical SET estadoInscripcion_idestadoInscripcion=(%s) WHERE idusuarios = (%s)", ("2", id))
    mysql.connection.commit()
    messages = []
    messages.append("confirmarPago")
    messages.append("¡Se ha guardado el pago correctamente!")
    session["confirmarPago"] = messages
     
    return redirect(url_for("private.adminLoginKmVertical"))


# Exportar PDF
@private.route("/loginAdmin/kmvertical/exportarPdf")
def kmVerticalExportarPdf():
  
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuarioskmvertical` ORDER BY `usuarioskmvertical`.`fechaRegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
  usuarios2 = []
  for x in range(0, len(usuarios)):
    user = list(usuarios[x])
        
        #Tipo Identificación
    tipoIdentificacion = user[6]
    cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
    tipoIdentificacion = cur.fetchone()
    tipoIdentificacion = tipoIdentificacion[1]
    user[6] = tipoIdentificacion
            
        #Sexo
    sexo = user[9]
    cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
    sexo = cur.fetchone()
    sexo = sexo[1]
    user[9] = sexo
    
          
        #Tipo Sangre
    tipoSangre = user[12]  
    cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()     
    tipoSangre = tipoSangre[1]
    user[12] = tipoSangre  

        #Talla Camisa
    tallaCamisa = user[14]
    cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
    tallaCamisa = cur.fetchone()
    tallaCamisa = tallaCamisa[1]
    user[14] = tallaCamisa

        #Categoria
    categoria = user[4]
    cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
    categoria = cur.fetchone()
    categoria = categoria[1]
    user[4] = categoria

        #Estado Inscripción
    estadoInscripcion = user[17]
    cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
    estadoInscripcion = cur.fetchone()
    estadoInscripcion = estadoInscripcion[1]
    user[17] = estadoInscripcion
        
        #Estado Kit
    estadoKit = user[18]
    cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
    estadoKit = cur.fetchone()
    estadoKit = estadoKit[1]
    user[18] = estadoKit
      
        #Código Equipo
    codigoEquipo = user[19]     
    cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
    codigoEquipo = cur.fetchone()
    codigoEquipo = codigoEquipo[1]
    user[19] = codigoEquipo

        #Fecha de Reistro
    fechaRegistro = str(user[20])
    fechaRegistro = fechaRegistro[0:10]
    user[20] = fechaRegistro
    usuarios2.append(user)
  usuarios = usuarios2  

  now = datetime.now()
  fecha = []
  fecha.append(now.year)
  fecha.append(now.month)
  fecha.append(now.day)
  fecha.append(now.hour)
  fecha.append(now.minute)
  fecha.append(now.second)
  
  rendered = render_template("export/kmVerticalPdf.html", usuarios=usuarios, fecha=fecha)

  config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

  pdf = pdfkit.from_string(rendered, False, configuration=config)
  response = make_response(pdf)
  response.headers["Content-Type"] = "application/pdf"
  response.headers["Content-Disposition"] = "inline; filename=output.pdf"
  return response
  
   
# Ruta para exportar a Excel
@private.route("/loginAdmin/kmvertical/exportarExcel")
def kmVerticalExportarExcel():
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuarioskmvertical` ORDER BY `usuarioskmvertical`.`fechaRegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
  usuarios2 = []
  for x in range(0, len(usuarios)):
    user = list(usuarios[x])
    
    #Tipo Identificación
    tipoIdentificacion = user[6]
    cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
    tipoIdentificacion = cur.fetchone()
    tipoIdentificacion = tipoIdentificacion[1]
    user[6] = tipoIdentificacion
        
    #Sexo
    sexo = user[9]
    cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
    sexo = cur.fetchone()
    sexo = sexo[1]
    user[9] = sexo
        
      
    #Tipo Sangre
    tipoSangre = user[12]  
    cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()     
    tipoSangre = tipoSangre[1]
    user[12] = tipoSangre  

    # #Talla Camisa
    # tallaCamisa = user[14]
    # cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
    # tallaCamisa = cur.fetchone()
    # tallaCamisa = tallaCamisa[1]
    # user[14] = tallaCamisa

    #Categoria
    # categoria = user[4]
    # cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
    # categoria = cur.fetchone()
    # categoria = categoria[1]
    # user[4] = categoria

    #Estado Inscripción
    estadoInscripcion = user[17]
    cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
    estadoInscripcion = cur.fetchone()
    estadoInscripcion = estadoInscripcion[1]
    user[17] = estadoInscripcion
    
    #Estado Kit
    # estadoKit = user[20]
    # cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
    # estadoKit = cur.fetchone()
    # estadoKit = estadoKit[1]
    # user[20] = estadoKit
  
    # #Código Equipo
    # codigoEquipo = user[21]     
    # cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
    # codigoEquipo = cur.fetchone()
    # codigoEquipo = codigoEquipo[1]
    # user[21] = codigoEquipo

    #Fecha de Reistro
    fechaRegistro = str(user[20])
    fechaRegistro = fechaRegistro[0:10]
    user[20] = fechaRegistro
    usuarios2.append(user)
  usuarios = usuarios2
 
  #output in bytes
  output = io.BytesIO()
  #create WorkBook object
  workbook = xlwt.Workbook()
  #add a sheet
  sh = workbook.add_sheet('Reporte de Usuarios')
   
  #add headers
  sh.write(0, 0, 'Id')
  sh.write(0, 1, 'Nombre')
  sh.write(0, 2, 'Apellido')
  sh.write(0, 3, 'Tipo Id.')
  sh.write(0, 4, 'Número Id.')
  sh.write(0, 5, 'Fecha Nac.')
  sh.write(0, 6, 'Sexo')
  sh.write(0, 7, 'Teléfono')
  sh.write(0, 8, 'Correo')
  sh.write(0, 9, 'Ciudad')
  sh.write(0, 10, 'Tipo Sangre')
  sh.write(0, 11, 'Entidad Salud')
  sh.write(0, 12, 'Contacto Emergencia')
  sh.write(0, 13, 'Estado Inscripción')
  sh.write(0, 14, 'Fecha Registro')
  
  idx = 0
  for user in usuarios:
    
    fechaInsc = str(user[20])
    sh.write(idx+1, 0, idx+1)
    sh.write(idx+1, 1, user[1])
    sh.write(idx+1, 2, user[2])
    sh.write(idx+1, 3, user[6])
    sh.write(idx+1, 4, user[7])
    sh.write(idx+1, 5, str(user[8]))
    sh.write(idx+1, 6, user[9])
    sh.write(idx+1, 7, user[10])
    sh.write(idx+1, 8, user[5])
    sh.write(idx+1, 9, user[11])
    sh.write(idx+1, 10, user[12])
    sh.write(idx+1, 11, user[13])
    sh.write(idx+1, 12, user[15]+" "+user[16])
    sh.write(idx+1, 13, user[17])
    sh.write(idx+1, 14, fechaInsc)
    idx += 1
    
  workbook.save(output)
  output.seek(0)
  now = datetime.now()
  

  nameFile = "Valhalla Series - KmVertical - " + str(now)
  return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename="+nameFile+".xls"})


# Carrera ----------------------------------------------------------------------------------------------------

@private.route("/loginAdmin/carrera")
def adminLoginCarrera():
  messages= []
  if session["loggedAdmin"] == True:
    email = session["email"]
    contraseña = session["contraseña"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
    usuario = cur.fetchone()

    if usuario:
      cur.execute("SELECT * FROM `usuarios` ORDER BY `usuarios`.`fechaRegistro` DESC")
      usuarios = cur.fetchall()
      usuarios = list(usuarios)
    
      usuarios2 = []
      for x in range(0, len(usuarios)):
        user = list(usuarios[x])
        
        #Sexo
        sexo = user[9]
        cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
        sexo = cur.fetchone()
        sexo = sexo[1]
        user[9] = sexo
    
        #Estado Inscripción
        estadoInscripcion = user[19]
        cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
        estadoInscripcion = cur.fetchone()
        estadoInscripcion = estadoInscripcion[1]
        user[19] = estadoInscripcion
        
        #Estado Kit
        estadoKit = user[20]
        cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
        estadoKit = cur.fetchone()
        estadoKit = estadoKit[1]
        user[20] = estadoKit

        #Fecha de Reistro
        fechaRegistro = str(user[22])
        fechaRegistro = fechaRegistro[0:10]
        user[22] = fechaRegistro
        usuarios2.append(user)
      usuarios = usuarios2  
      
      cur.execute("SELECT * FROM eventos WHERE nombre = (%s)", ["Carrera"])
      evento = cur.fetchone()
      disponible = False
      if evento[2] == "Disponible":
        disponible = True
      else:
        disponible = False
        
      if "confirmarPago" in session:
        messagesNew = session['confirmarPago']
        messages.append("success")
        messages.append(messagesNew[1])
        session.pop('confirmarPago',None)
      else:
        messages.append("0")
        messages.append("1")

      return render_template("eventos/carrera.html",usuarios=usuarios, usuario=usuario, messages = messages, disponible=disponible)
    else:
      messages.append("error")
      messages.append("Credenciales Incorrectos")
      return render_template("loginAdmin.html", messages=messages)
  else:
    return redirect(url_for("private.adminLogin"))



#Mostrar Usuario KmVertical

@private.route("/loginAdmin/carrera/mostrarUsuario/<string:id>")
def mostrarUsuarioCarrera(id):
    if session["loggedAdmin"] == True:
      messages= []
      if session["loggedAdmin"] == True:
        email = session["email"]
        contraseña = session["contraseña"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarioadministrador WHERE correoElectronico = (%s) and contraseña = (%s)", (email, contraseña))
        usuario = cur.fetchone()

      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM usuarioskmvertical WHERE idusuarios=(%s)", [id])
      usuariokm = cur.fetchone()
      if usuariokm:
        usuariokm = list(usuariokm)

        #Tipo Identificación
        tipoIdentificacion = usuariokm[6]
        cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
        tipoIdentificacion = cur.fetchone()
        tipoIdentificacion = tipoIdentificacion[1]
        usuariokm[6] = tipoIdentificacion
        
        #Sexos   
        sexo = usuariokm[9]
        cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
        sexo = cur.fetchone()
        sexo = sexo[1]
        usuariokm[9] = sexo

        # #Distancia
        # distancia = usuario[3]
        # cur.execute("SELECT * FROM distancias WHERE iddistancias = (%s)", [distancia])
        # distancia = cur.fetchone()
        # usuario[3] = distancia
        
        #Tipo Sangre
        tipoSangre = usuariokm[12]
        cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
        tipoSangre = cur.fetchone()
        tipoSangre = tipoSangre[1]
        usuariokm[12] = tipoSangre  

        #Talla Camisa
        tallaCamisa = usuariokm[14]
        cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
        tallaCamisa = cur.fetchone()
        tallaCamisa = tallaCamisa[1]
        usuariokm[14] = tallaCamisa

        #Categoria
        # categoria = usuario[4]
        # cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
        # categoria = cur.fetchone()
        # categoria = categoria[1]
        # usuario[4] = categoria

        #Estado Inscripción
        estadoInscripcion = usuariokm[17]
        cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
        estadoInscripcion = cur.fetchone()
        estadoInscripcion = estadoInscripcion[1]
        usuariokm[17] = estadoInscripcion
    
        #Estado Kit
        # estadoKit = usuario[20]
        # cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
        # estadoKit = cur.fetchone()
        # estadoKit = estadoKit[1]
        # usuario[20] = estadoKit

        #Código Equipo
        # codigoEquipo = usuario[21]
        # cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
        # codigoEquipo = cur.fetchone()
        # codigoEquipo = codigoEquipo[1]
        # usuario[21] = codigoEquipo

        #Fecha de Reistro
        fechaRegistro = str(usuariokm[20])
        fechaRegistro = fechaRegistro[0:10]
        usuariokm[20] = fechaRegistro 
        messages = []
        messages.append("info")
        messages.append("Información de "+usuariokm[1]+" "+usuariokm[2]) 
        return render_template("info/mostrarUsuarioKmVertical.html", messages=messages, usuariokm=usuariokm, usuario=usuario)
      else:
        return redirect(url_for("private.adminLoginEntreno"))
    else:
      return redirect(url_for("private.adminLoginEntreno"))
#confirmar PAgo
@private.route("/loginAdmin/carrera/confirmarPago/<string:id>", methods=["POST"])
def loginAdminConfirmarPagoCarrera(id):
    cur = mysql.connection.cursor()
    
    cur.execute("UPDATE usuarios SET estadoInscripcion_idestadoInscripcion=(%s) WHERE idusuarios = (%s)", ("2", id))
    mysql.connection.commit()
    messages = []
    messages.append("confirmarPago")
    messages.append("¡Se ha guardado el pago correctamente!")
    session["confirmarPago"] = messages
     
    return redirect(url_for("private.adminLoginCarrera"))

#Confirma Entrega de Kit
@private.route("/loginAdmin/carrera/confirmarEntregaKit/<string:id>", methods=["POST"])
def loginAdminConfirmarEntregaKit(id):
    cur = mysql.connection.cursor()
    
    cur.execute("UPDATE usuarios SET estadoKit_idestadoKit=(%s) WHERE idusuarios = (%s)", ("2", id))
    mysql.connection.commit()
    messages = []
    messages.append("confirmarPago")
    messages.append("¡Se ha guardado ha entregado el kit correctamente!")
    session["confirmarPago"] = messages
     
    return redirect(url_for("private.adminLoginCarrera"))

# Exportar PDF
@private.route("/loginAdmin/carrera/exportarPdf")
def carreraExportarPdf():
  
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuarios` ORDER BY `usuarios`.`fechaRegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
  usuarios2 = []
  for x in range(0, len(usuarios)):
    user = list(usuarios[x])
        
    #Tipo Identificación
    tipoIdentificacion = user[6]
    cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
    tipoIdentificacion = cur.fetchone()
    tipoIdentificacion = tipoIdentificacion[1]
    user[6] = tipoIdentificacion
            
        #Sexo
    sexo = user[9]
    cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
    sexo = cur.fetchone()
    sexo = sexo[1]
    user[9] = sexo
    
          
        #Tipo Sangre
    tipoSangre = user[14]  
    cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()     
    tipoSangre = tipoSangre[1]
    user[14] = tipoSangre  

        #Talla Camisa
    tallaCamisa = user[16]
    cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
    tallaCamisa = cur.fetchone()
    tallaCamisa = tallaCamisa[1]
    user[16] = tallaCamisa

        #Categoria
    categoria = user[4]
    cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
    categoria = cur.fetchone()
    categoria = categoria[1]
    user[4] = categoria

        #Estado Inscripción
    estadoInscripcion = user[19]
    cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
    estadoInscripcion = cur.fetchone()
    estadoInscripcion = estadoInscripcion[1]
    user[19] = estadoInscripcion
        
        #Estado Kit
    estadoKit = user[20]
    cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
    estadoKit = cur.fetchone()
    estadoKit = estadoKit[1]
    user[20] = estadoKit
      
        #Código Equipo
    codigoEquipo = user[21]     
    cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
    codigoEquipo = cur.fetchone()
    codigoEquipo = codigoEquipo[1]
    user[21] = codigoEquipo

        #Fecha de Reistro
    fechaRegistro = str(user[22])
    fechaRegistro = fechaRegistro[0:10]
    user[22] = fechaRegistro
    usuarios2.append(user)
  usuarios = usuarios2  

  now = datetime.now()
  fecha = []
  fecha.append(now.year)
  fecha.append(now.month)
  fecha.append(now.day)
  fecha.append(now.hour)
  fecha.append(now.minute)
  fecha.append(now.second)
  print("Carrera")
  rendered = render_template("export/carreraPdf.html", usuarios=usuarios, fecha=fecha)

  config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

  pdf = pdfkit.from_string(rendered, False, configuration=config)
  response = make_response(pdf)
  response.headers["Content-Type"] = "application/pdf"
  response.headers["Content-Disposition"] = "inline; filename=output.pdf"
  return response
  
   
# Ruta para exportar a Excel
@private.route("/loginAdmin/carrera/exportarExcel")
def carreraExportarExcel():
  cur = mysql.connection.cursor()
  
  cur.execute("SELECT * FROM `usuarios` ORDER BY `usuarios`.`fechaRegistro` ASC")
  usuarios = cur.fetchall()
  usuarios = list(usuarios)
  usuarios2 = []
  for x in range(0, len(usuarios)):
    user = list(usuarios[x])
    print(user)
        
    #Tipo Identificación
    tipoIdentificacion = user[6]
    cur.execute("SELECT * FROM tipoIdentificacion WHERE idtipoIdentificacion = (%s)", [tipoIdentificacion])
    tipoIdentificacion = cur.fetchone()
    tipoIdentificacion = tipoIdentificacion[1]
    user[6] = tipoIdentificacion
            
        #Sexo
    sexo = user[9]
    cur.execute("SELECT * FROM sexo WHERE idsexo = (%s)", [sexo])
    sexo = cur.fetchone()
    sexo = sexo[1]
    user[9] = sexo
    
          
        #Tipo Sangre
    tipoSangre = user[14]  
    cur.execute("SELECT * FROM tiposangre WHERE idtipoSangre = (%s)", [tipoSangre])
    tipoSangre = cur.fetchone()     
    tipoSangre = tipoSangre[1]
    user[14] = tipoSangre  

        #Talla Camisa
    tallaCamisa = user[16]
    cur.execute("SELECT * FROM tallacamisa WHERE idtallaCamisa = (%s)", [tallaCamisa])
    tallaCamisa = cur.fetchone()
    tallaCamisa = tallaCamisa[1]
    user[16] = tallaCamisa

        #Categoria
    categoria = user[4]
    cur.execute("SELECT * FROM categorias WHERE idcategorias = (%s)", [categoria])
    categoria = cur.fetchone()
    categoria = categoria[1]
    user[4] = categoria

        #Estado Inscripción
    estadoInscripcion = user[19]
    cur.execute("SELECT * FROM estadoinscripcion WHERE idestadoInscripcion = (%s)", [estadoInscripcion])
    estadoInscripcion = cur.fetchone()
    estadoInscripcion = estadoInscripcion[1]
    user[19] = estadoInscripcion
        
        #Estado Kit
    estadoKit = user[20]
    cur.execute("SELECT * FROM estadokit WHERE idestadoKit = (%s)", [estadoKit])
    estadoKit = cur.fetchone()
    estadoKit = estadoKit[1]
    user[20] = estadoKit
      
        #Código Equipo
    codigoEquipo = user[21]     
    cur.execute("SELECT * FROM equipos WHERE idequipos = (%s)", [codigoEquipo])
    codigoEquipo = cur.fetchone()
    codigoEquipo = codigoEquipo[1]
    user[21] = codigoEquipo

        #Fecha de Reistro
    fechaRegistro = str(user[22])
    fechaRegistro = fechaRegistro[0:10]
    user[22] = fechaRegistro
    usuarios2.append(user)
  usuarios = usuarios2  
 
  #output in bytes
  output = io.BytesIO()
  #create WorkBook object
  workbook = xlwt.Workbook()
  #add a sheet
  sh = workbook.add_sheet('Reporte de Usuarios')
   
  #add headers
  sh.write(0, 0, 'Id')
  sh.write(0, 1, 'Nombre')
  sh.write(0, 2, 'Apellido')
  sh.write(0, 3, 'Tipo Id.')
  sh.write(0, 4, 'Número Id.')
  sh.write(0, 5, 'Fecha Nac.')
  sh.write(0, 6, 'Sexo')
  sh.write(0, 7, 'Teléfono')
  sh.write(0, 8, 'Correo')
  sh.write(0, 9, 'Ciudad')
  sh.write(0, 10, 'Departamento')
  sh.write(0, 11, 'País')
  sh.write(0, 12, 'Tipo Sangre')
  sh.write(0, 13, 'Entidad Salud')
  sh.write(0, 14, 'Contacto Emergencia')
  sh.write(0, 15, 'Talla Camisa')
  sh.write(0, 16, 'Estado Inscripción')
  sh.write(0, 17, 'Estado Kit')
  sh.write(0, 18, 'Fecha Registro')
  
  idx = 0
  for user in usuarios:
    
    fechaInsc = str(user[22])
    sh.write(idx+1, 0, idx+1)
    sh.write(idx+1, 1, user[1])
    sh.write(idx+1, 2, user[2])
    sh.write(idx+1, 3, user[6])
    sh.write(idx+1, 4, user[7])
    sh.write(idx+1, 5, str(user[8]))
    sh.write(idx+1, 6, user[9])
    sh.write(idx+1, 7, user[10])
    sh.write(idx+1, 8, user[5])
    sh.write(idx+1, 9, user[13])
    sh.write(idx+1, 10, user[12])
    sh.write(idx+1, 11, user[11])
    sh.write(idx+1, 12, user[14])
    sh.write(idx+1, 13, user[15])
    sh.write(idx+1, 14, user[17]+" "+user[18])
    sh.write(idx+1, 15, user[16])
    sh.write(idx+1, 16, user[19])
    sh.write(idx+1, 17, user[20])
    sh.write(idx+1, 18, fechaInsc)
    idx += 1
    
  workbook.save(output)
  output.seek(0)
  now = datetime.now()
  

  nameFile = "Valhalla Series - Carrea - " + str(now)
  return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename="+nameFile+".xls"})


@private.route("/loginAdmin/logout", methods=["POST"])
def estado():
  if request.method == "POST":
    session['loggedAdmin'] = False
    
    return  redirect(url_for("private.adminLogin"))
    