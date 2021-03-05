from flask import render_template, Response, make_response, request, redirect,url_for, flash, session, json, jsonify, logging, send_file

from datetime import date
from datetime import datetime
from . import public
from app.db import *
#Configuración de sesion . permanete
@public.before_request
def session_management():
  session.permanent = True


@public.route('/')
def home():
  
  session["loggedAdmin"] = False
  messages=[]
  usuario=[]
  messages.append("0")
  messages.append("1")
  return render_template("home.html", messages=messages, usuario=usuario)

@public.route("/informacion")
def info():
  messages=[]
  usuario=[]
  messages.append("0")
  messages.append("1")
  return render_template("informacion.html", messages=messages, usuario=usuario)
