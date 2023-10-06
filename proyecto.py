
# Importamos el modulo de request
import requests
 
# Creamos el request que queremos con nuestra url de la API
response = requests.get('https://ideihm.covam.es/api-ihm/getmarea?request=gettide&amp;id=42&amp;format=json&amp;month=202310')
 
# Visualizamos el contenido del JSON
print(response.json())

