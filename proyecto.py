
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

# Creamos variable para obtener puerto y poner "Puerto:"
puerto = fichero['mareas']['puerto']
mensaje = f"Puerto: {puerto}"
print(mensaje)

# Creamos variable para los datos
datos = fichero['mareas']['datos']['marea']
for fecha in datos:print(fecha)