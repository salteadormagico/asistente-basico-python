from datetime import datetime
from pathlib import Path
import platform
import os
import socket

def funcion_dia():
	now = datetime.now()
	dia = now.day
	mes = now.month
	año = now.year
	print(str(dia) + "/" + str(mes) + "/" + str(año))
def funcion_hora():
	now = datetime.now()
	hora = now.strftime("%H:%M")
	print(hora)
def no_valido():
	return "formato de respuesta no válido, inténtalo de nuevo"
def contar_archivos(ruta):
	numero_archivos = 0
	for elemento in ruta.iterdir():
		if elemento.is_file():
			numero_archivos += 1
	return numero_archivos

def nombre_archivos(ruta):
	for elemento in ruta.iterdir():
		if elemento.is_file():
			print(elemento)
def buscar_por_extension(ruta):
	extension = input("que extensión buscas?: ")
	extension = extension.lower()
	if not extension.startswith("."):
		extension = "." + extension
	for elemento in ruta.iterdir():
		if elemento.is_file():
			if elemento.suffix == extension:
				print(elemento)

def funcion_archivos(ruta):
	ruta = Path(ruta)
	print(ruta)

	while True:
		e = input("""
			1. número de archivos
			2. nombre de los archivos
			3. número y nombres
			4. filtrar por extensión
			5. volver
					""")
		try:
			if e == "1":
				print(contar_archivos(ruta))
				break
			elif e == "2":
				nombre_archivos(ruta)
				break
			elif e == "3":
				nombre_archivos(ruta)
				print(contar_archivos(ruta))
				break
			elif e == "4":
				buscar_por_extension(ruta)
				break
			elif e == "5":
				break
			else:
				print(no_valido())
		except FileNotFoundError:
			print("Esa carpeta no existe")

def funcion_sistema():
	os = platform.system()
	version = platform.release()
	arquitectura = platform.machine()
	procesador = platform.processor()
	nombre_pc = platform.node()
	print(
		"Sistema operativo: ", os, version,
		"\nArquitectura: ", arquitectura,
		"\nProcesador: ", procesador,
		"\nNombre del equipo: ", nombre_pc		
		)

def funcion_buscar(ruta):
	ruta = Path(ruta)
	busqueda = input("¿Qué archivo buscas?: ")
	try:
		for elemento in ruta.iterdir():
			if busqueda.lower() in elemento.name.lower():
				print(elemento)
	except FileNotFoundError:
		print("Esa carpeta no existe")
def funcion_abrir(ruta):
	ruta = Path(ruta)
	try:
		os.startfile(ruta)
	except FileNotFoundError:
		print("Ese archivo no existe")

def funcion_ip():
	nombre = socket.gethostname()
	ip = socket.gethostbyname(nombre)
	print(ip)

def interpretar_comando(comando):
	partes = comando.split(" ", 1)
	if len(partes) > 1:
		funcion = comandos.get(partes[0])
		argumento = partes[1]
		if funcion is None:
			print("Ese comando no existe")
		else:
			funcion(argumento)
	elif comando == "salir":
		return True
	else:
		funcion = comandos.get(comando)
		if funcion is None:
			print("Ese comando no existe")
		elif comando == "archivos" or comando == "buscar" or comando == "abrir":
			print("Debes ingresar una ruta")
		else:
			funcion()
	return False
def funcion_ayuda():
	for comando in comandos:
		print(comando)

comandos = {
	"dia": funcion_dia,
	"hora": funcion_hora,
	"archivos": funcion_archivos,
	"ayuda": funcion_ayuda,
	"sistema": funcion_sistema,
	"buscar": funcion_buscar,
	"abrir": funcion_abrir,
	"ip": funcion_ip
	}
def main():


	print("""
		==== MI ASISTENTE ====
		""")
	while True:
		p = input("> ")
		salir = interpretar_comando(p)
		if salir:
			break
main()