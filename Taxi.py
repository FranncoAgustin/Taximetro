"""
Enunciado
Nuestro amigo y taxista Ruben ORTiz nos solicita que le desarrollemos un sistema para poder registrar y 
obtener información sobre sus viajes diarios.
Cada vez que comienza un viaje Rubén debe ingresar la distancia del viaje. 
(‘C’(corto),’M’(mediano),’L’(Largo)).
El día de Rubén finaliza cuando llega a los 30 viajes diarios o cuando ingresa distancia ‘Z’(fin de datos).
Por cada viaje se ingresa:
• Cantidad de pasajeros (>0 y <4)
• Importe a cobrar + bajada de bandera ($80) 
Y por cada pasajero de ese viaje:
• Nombre
• Edad (>18 y <120)
Se desea saber por cada viaje cual es la persona mas grande y su nombre.
Al finalizar el día de trabajo de Rubén de debe informar:
• Cantidad de viajes por cada categoría(‘C’,’M’,’L’)
• Recaudación total.
• Promedio de valor por viaje.
• El porcentaje de viajes Cortos con respecto al total de los viajes realizados.
Todos los datos ingresados por parte del usuario deben ser validados antes de procesarse
    global L
    global M
    global C
"""
from os import system


datos_pasajeros=[]
recaudacion=0


C=0
M=0
L=0
def taxi():
    global recaudacion
    global L
    global M
    global C
    print("Distancia = C=Corto, M=Mediano, L=Largo")
    distancia =input(f'Seleccione distancia a viajar c, m, l:  ')
    if (distancia.upper())=='C':
            C+=1
    if (distancia.upper())=='M':
            M+=1
    if (distancia.upper())=='L':
            L+=1
    if (distancia.upper())!='C' and (distancia.upper())!='M' and (distancia.upper())!='L':
        print("Usted no ingreso los datos correctamente")
        return        
    pasajeros = int(input("Pasajeros a viajar:  "))
    if pasajeros>4 or pasajeros<1:
        print("No se permiten mas de 4 pasajeros")
        return 
    cobro = int(input("El valor del viaje es:  "))
    if cobro>=1:
            recaudacion+=cobro+80
    bandera= print("Se le informa al señor pasajero que al valor del viaje se le suma la bajada de bandera($80)")
    persona=0
    for i in range(0,pasajeros):
        datos=[]
        persona+=1
        pasajero_edad = int(input(f'Años del pasajero {persona}:  '))
        if pasajero_edad<18 :
            print("El taxi solo permite mayores de 18 anios")
        elif pasajero_edad>120:
            print("Usted no ingreso la edad correctamente, vuelva a intentar")
            return
        else:   
            pasajero_nombre = input(f'Ingrese nombre del pasajero {persona} :  ')
            datos.append(pasajero_nombre)
            datos.append(pasajero_edad)
            datos_pasajeros.append(datos)


viajes=0
terminar_el_proceso =True
producto = 1
while terminar_el_proceso or viajes>=30 :   # while terminar_el_proceso == False:
    taxi()
    terminar=(input("Si desea ingresar un nuevo viaje presione enter, de lo contrario presione 'z':  "))
    if terminar=='z':
        terminar_el_proceso = False
    viajes+=1
promedio=recaudacion/viajes
system('cls')
print("Datos del dia:")
print(f'Se realizaron: {C} viajes cortos, {M} viajes medianos, {L} viajes largos ')
print(f'Se realizaron {viajes} viajes y la recaudacion es: {recaudacion}')
print("El promedio de valor por viaje es: " ,promedio)
print("Datos de pasajeros:" ,datos_pasajeros)



        






