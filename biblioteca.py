# Programa de Biblioteca
# Creado por Nelson Bolaños

import csv
import random
import datetime
import calendar

libros = []
autores = []

with open('Tareas/libros.csv') as f:
    reader = csv.reader(f)
    libros = list(reader)

with open('Tareas/autores.csv') as t:
    autreader = csv.reader(t)
    autores = list(autreader)

def findDay(date):
    fecha = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[fecha])

from random import randint

"""

dia = datetime.date(randint(2020, 2020), randint(2, 2), randint(1, 28))
dia_1 = dia.strftime("%Y-%m-%d")

"""
with open('prestamo.csv', 'w') as p:
    write = csv.writer(p)

for a in range(20):
    n = random.randint(0, 9)
    dia = randint(1, 28)
    mes = randint(2, 2)
    year = randint(2020, 2020)
    d2 = datetime.date(year,mes,dia)
    dia_1 = d2.strftime("%Y-%m-%d")

    libro = libros[n]
    autor = autores[n]
    weekday = findDay(dia_1)

    pass

    with open('prestamo.csv', 'a') as x:
        writer = csv.writer(x)
        test = [
            [libro,autor,weekday,year,mes,dia]
        ]

        for i in test:
            writer.writerow(i)
            pass


pass

while True:
    print('Menu de Consultas')
    print('1 - Todos los libros solicitados de un autor')
    print('2 - Dia de la semana mas solicitud de libros')
    print('3 - Autor mas solicitado')
    print('4 - Libro mas solicitado')
    print('5 - Salir','\n')

    opcion=(input('Seleccionar una opcion: '))

    if opcion == '1':
        with open('prestamo.csv') as s:
            text = csv.reader(s)
            datos = list(text)
        print('1 - Platon')
        autor1= input('Seleccion: ')
        while autor1 == '1':
            for i in range(20):
                l3 = datos[i][1]
#                if l3 == '[\'Platon\']':
#                   print(datos[i][0])1
        print(l3)

        #exm = datos[0][1]
        #print(exm)
    elif opcion == '2':
        with open('prestamo.csv') as s:
            text = csv.reader(s)
            datos = list(text)

        Mon = 0
        Tue = 0
        Wed = 0
        Thu = 0
        Fri = 0
        Sat = 0
        Sun = 0

        for i in range(20):
            if datos[i][2] == 'Monday':
                Mon += 1
            elif datos[i][2] == 'Tuesday':
                Tue += 1
            elif datos[i][2] == 'Wednesday':
                Wed += 1
            elif datos[i][2] == 'Thursday':
                Thu += 1
            elif datos[i][2] == 'Friday':
                Fri += 1
            elif datos[i][2] == 'Saturday':
                Sat += 1
            else:
                Sun += 1
            pass
        print('still')
    elif opcion == '3':
        print('nada')
    else:
        exit()
