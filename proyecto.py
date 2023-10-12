
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


# Creamos filtrado por fecha
#fechaSelecionada = input("Seleccione una fecha de Octubre(2023-10-02): ")
#incorrecto = True
#datos = fichero['mareas']['datos']['marea']
#for dato in datos:
#   fecha = dato['fecha']
#   hora = dato['hora']
#   altura = dato['altura']
#   tipo = dato['tipo']   
#
#   if(fechaSelecionada==fecha):
#       print(f"Fecha: {fecha} - Hora: {hora} - Altura: {altura} - Tipo: {tipo}")
#       incorrecto = False
#
#if(incorrecto==True):
#   print("Fecha incorrecta")


# Creamos prediccion de mareas
import datetime

vfecha = input("Introduce una fecha como en el ejemplo '2023-10-02'(Octubre): ")
vhora = input("Introduce una hora como en el ejemplo '10:40': ")

# Si no seleccionas nada  
if not vfecha:
   ifecha = datetime.datetime.now() # Se pone la hora del sistema
else:

    # Si seleccionas fecha y hora
    try:
        ifecha = datetime.datetime.strptime(vfecha + ' ' + vhora, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Fecha u hora incorrecta.")
        exit()

datos = fichero['mareas']['datos']['marea']
for i in range(len(datos)):
    fecha = datos[i]['fecha']
    hora = datos[i]['hora']
    tipo = datos[i]['tipo']
    
    # Convierte la fecha y hora actual en datetime para compararlos(tanto día como hora)
    fechact = datetime.datetime.strptime(fecha + ' ' + hora, '%Y-%m-%d %H:%M')

    # Compara si la fecha y hora actual es mayor a la ingresada
    if fechact > ifecha:
        sfecha = fechact
        shora = hora
        stipo = tipo
        break

if sfecha and shora:
    print("Fecha: ", ifecha.strftime('%Y-%m-%d %H:%M')) #Con .strftime puedes coger una parte el día o la hora

    if(stipo=="pleamar"):
        print("En el día", sfecha.strftime('%Y-%m-%d'), "la marea estará subiendo hasta las", shora, )
    else:
        print("En el día", sfecha.strftime('%Y-%m-%d'), "la marea estará bajando hasta las", shora, )

else:
    print("No se encontró una fecha y hora siguientes en los datos.")


#CREAMOS EL MENÚ
# Mostrar todo
#def op1():
#    print('Has elegido la opción 1')

# Filtrar por fecha
#def op2():
#    print('Has elegido la opción 2')

# Salir
#def op3():
#    print('Salir')

# Creamos el menú
#menu = {
#   '1': ('1.- Mostrar menú',op1),
#   '2': ('2.- Filtrar por fecha',op2),
#   '3': ('3.- Salir',op3)
#}

# Para que el usuario pueda seleccionar opcion
#op = input("Seleccione una opcion: ")

# Excepcion o Accion
#accion = menu.get(op)
#if accion: #si la accion existe que se ejecute
#   accion()
#else: #si la opcion no existe que de error
#   print("Opción no válida")





