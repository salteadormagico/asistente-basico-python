from datetime import datetime
from pathlib import Path

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

def funcion_archivos():
	ruta = Path(input("introduce una ruta"))
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
		for elemento in ruta.iterdir():
			if elemento.is_file:
				if elemento.suffix == extension:
					print(elemento)
	e = input("""
		1. número de archivos
		2. nombre de los archivos
		3. número y nombres
		4. filtrar por extensión
				""")
	if e == "1":
		print(contar_archivos(ruta))
	elif e == "2":
		nombre_archivos(ruta)
	elif e == "3":
		nombre_archivos(ruta)
		contar_archivos(ruta)
	elif e == "4":
		buscar_por_extension(ruta)
	else:
		print(no_valido())
#	def que_hacer():
#def funcion_buscar():

def main():
	def funcion_ayuda():
		for comando in comandos:
			print(comando)

	comandos = {
	"dia": funcion_dia,
	"hora": funcion_hora,
	"archivos": funcion_archivos,
	"ayuda": funcion_ayuda
	#"buscar": funcion_buscar
	}


	print("""
		==== MI ASISTENTE ====
		""")
	while True:
		p = input("> ")
		partes = p.split(" ")
		if len(partes) > 1:
			funcion = comandos.get(partes[0])
		else:
			funcion = comandos.get(p)
		if p == "salir":
			break
		elif funcion is None:
			print("Ese comando no existe")
		else:
			funcion()

main()