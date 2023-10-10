
# Importamos el modulo de request
import requests

# Importamos el modulo json
import json
 
# Creamos el request que queremos con nuestra url de la API
pagina = requests.get('https://ideihm.covam.es/api-ihm/getmarea?request=gettide&amp;id=42&amp;format=json&amp;month=202310')

# Visualizamos el contenido del JSON
#print(pagina.json()) #Esto ya no lo utilizamos ya que queremos visualizarlo ordenadamente 

# Creamos la variable fichero para meter los datos
fichero = pagina.json()

#Comprobamos que fichero es realmente los datos que necesitamos
#print(fichero) 

#Comprobamos el tipo de objeto que es nuestro fichero para saber si es un diccionario
#print(type(fichero['mareas']['datos']['marea']))

# Tratamos el fichero JSON

# Creamos variable para obtener puerto y el instituto
#puerto = fichero['mareas']['puerto']
#mensaje = f"Puerto: {puerto}"
#print(mensaje)

# Creamos variable para los datos
#datos = fichero['mareas']['datos']['marea']
#for dato in datos:
#    fecha = dato['fecha']
#    hora = dato['hora']
#    altura = dato['altura']
#    tipo = dato['tipo']
#    print(f"Fecha: {fecha} - Hora: {hora} - Altura: {altura} - Tipo: {tipo}") #Cuidado con la tabulación


#CREAMOS EL MENÚ

# Mostrar todo
def op1():
    datos = fichero['mareas']['datos']['marea']
    for dato in datos:
        fecha = dato['fecha']
        hora = dato['hora']
        altura = dato['altura']
        tipo = dato['tipo']
        print(f"Fecha: {fecha} - Hora: {hora} - Altura: {altura} - Tipo: {tipo}")

# Filtrar por fecha
def op2():
    print('Has elegido la opción 2')

# Salir
def op3():
    print('Salir')

# Creamos el menú
menu = {
    '1': ('1.- Mostrar menú',op1),
    '2': ('2.- Filtrar por fecha',op2),
    '3': ('3.- Salir',op3)
}

# Para que el usuario pueda seleccionar opcion
op = input("Seleccione una opcion: ")

# Excepcion o Accion
accion = menu.get(op)
if accion: #si la accion existe que se ejecute
    accion()
else: #si la opcion no existe que de error
    print("Opción no válida")





