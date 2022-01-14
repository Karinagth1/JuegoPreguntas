import os  
import random 
import urllib.request
textoBaseDePreguntas = ''''''
renglones = []

try:
    urlBDj = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSENkS_yI5lFmANBOJQkZT4Z8nXmKr6lfFQG5qYvlfnPMHBmtUM-C5JB6TFUNeN8UJ-jh2BXpDAcmy8/pub?output=tsv"
    HTTP_response=urllib.request.urlopen(urlBDj)
    for line in HTTP_response:
        renglones.append(line.decode("utf-8").replace("\n","").replace("\r",""))
except:
    print("No hay conexión a internet, no se pudo cargar la BD")
    exit()

num_pregunta = 0

base_de_preguntas = []
cantidadDePreguntas = len(renglones)

pregunta_R = []
eleccion = []
pregunta = ""
respuesta = ""

for i in range(cantidadDePreguntas):
    if(renglones[i] == ""):
        continue
    base_de_preguntas.append(renglones[i].split("\t"))


def borrarCon():
    os.system("cls" if os.name == "nt" else "clear")


def escogerPregunta(n):
    global eleccion, respuesta, pregunta

    pregunta_R = base_de_preguntas[n]
    pregunta = pregunta_R[0]
    respuesta = pregunta_R[1]
    eleccion = pregunta_R[1:]
    for i in range(10):
        random.shuffle(eleccion)
    print(eleccion)
    return pregunta_R


def mostrarPregunta():
    borrarCon()
    print()
    print(pregunta)
    print("A)", eleccion[0])
    print("B)", eleccion[1])
    print("C)", eleccion[2])
    print("D)", eleccion[3])
    print()


def tomarRespuesta():
    respuestaUsuario = ""
    opcValidas = ["a", "b", "c", "d"]
    while True:
        respuestaUsuario = input("ingrese su respuesta > ").lower()
        if not (respuestaUsuario in opcValidas):
            print("La respuesta no valida entre las opciones, vuelva a intentarlo")
            continue
        break
    return opcValidas.index(respuestaUsuario)


def jugar():
    escogerPregunta(num_pregunta)
    mostrarPregunta()
    if(eleccion[tomarRespuesta()]==respuesta ):
        print("Respuesta correcta")
        input("ENTER PARA CONTINUAR")
    else:
        print("Respuesta Incorrecta, la correcta es: "+ respuesta)
        input("ENTER PARA CONTINUAR")

while True:
    try:
        jugar()
    except:
        pass
    num_pregunta += 1
    if(num_pregunta==cantidadDePreguntas):
        borrarCon()
        print("El juego finalizo")
        input("ENTER PARA CONTINUAR")
        break
