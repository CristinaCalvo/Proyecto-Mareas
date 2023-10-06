
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

# print(fichero) #Comprobamos que fichero es realmente los datos que necesitamos

print(type(fichero['mareas']))

# Tratamos el fichero JSON
#for mareas in fichero['mareas']:
 #  print(mareas['puerto'])



   # for datos in mareas_dict['datos']:
    #print(datos['fecha'] + datos['hora'] + datos['altura'] + datos['tipo'])
