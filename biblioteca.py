# Programa de Biblioteca
# Creado por Nelson Bolaños

import csv
import random
import datetime
import calendar
import time

libros = []
autores = []

with open('Tareas/libros.csv') as f:
    reader = csv.reader(f)
    libros = list(reader)

with open('Tareas/autores.csv') as t:
    autreader = csv.reader(t)
    autores = list(autreader)

def findDay(date):                                                #Obtener el dia segun la fecha
    fecha = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[fecha])

from random import randint

"""

dia = datetime.date(randint(2020, 2020), randint(2, 2), randint(1, 28))
dia_1 = dia.strftime("%Y-%m-%d")

"""
with open('prestamo.csv', 'w') as p:
    write = csv.writer(p)

for a in range(30):
    n = random.randint(0, 10)
    dia = randint(1, 28)
    mes = randint(2, 2)
    year = randint(2020, 2020)
    d2 = datetime.date(year,mes,dia)
    dia_1 = d2.strftime("%Y-%m-%d")  #transforma strings a date

    libro = libros[n]
    autor = autores[n]
    weekday = findDay(dia_1)

    with open('prestamo.csv', 'a') as x:
        writer = csv.writer(x)
        test = [
            [libro,autor,weekday,year,mes,dia]
        ]

        for i in test:
            writer.writerow(i)

while True:
    with open('prestamo.csv') as s:
        text = csv.reader(s)
        datos = list(text)

    l4 = [i for i in datos if len(i) > 0]

    print('Menu de Consultas')
    print('1 - Todos los libros solicitados de un autor')
    print('2 - Dia de la semana mas solicitud de libros')
    print('3 - Autor mas solicitado')
    print('4 - Libro mas solicitado')
    print('5 - Salir','\n')

    opcion=(input('Seleccionar una opcion: '))

    if opcion == '1':
        while True:
            print('1 - Platon')
            print('2 - Epicuro')
            print('11 - Salir Menu Principal')
            autor1= input('Seleccion: ')
            l4 = [i for i in datos if len(i) > 0]
            if autor1 == '1':
                for i in range(30):
                    l3 = l4[i][1]
                    l5 = {l4}
                    pass
#                    if l3 == '[\'Platon\']':


            elif autor1 == '2':
                for i in range(30):
                    l3 = l4[i][1]
                    if l3 == '[\'Epicuro\']':
                        print(l4[i][0])
            else:
                break
        time.sleep(2)

    elif opcion == '2':

        Mon = 0
        Tue = 0
        Wed = 0
        Thu = 0
        Fri = 0
        Sat = 0
        Sun = 0

#Sumar por dia de la semana

        for i in range(30):
            if l4[i][2] == 'Monday':
                Mon += 1
            elif l4[i][2] == 'Tuesday':
                Tue += 1
            elif l4[i][2] == 'Wednesday':
                Wed += 1
            elif l4[i][2] == 'Thursday':
                Thu += 1
            elif l4[i][2] == 'Friday':
                Fri += 1
            elif l4[i][2] == 'Saturday':
                Sat += 1
            else:
                Sun += 1

        l5 = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]
        l6 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
        d1=dict(zip(l6,l5))
        l9 = list()
        itemMaxValue = max(d1.items(), key=lambda x: x[1])  # Obtener los valores mas altos de un diccionario
        for key, value in d1.items():
            if value == itemMaxValue[1]:
                l9.append(key)
        print(l9)
        time.sleep(3)

    elif opcion == '3':

#Suma por Autor

        LaoTse = 0
        Platon = 0
        Aristoteles = 0
        Epicuro = 0
        Descartes = 0
        ThomasHobbes = 0
        DavidHume = 0
        Montesquieu = 0
        ArthurSchopenhauer = 0
        FriedrichNietzsche = 0

        for i in range(30):
            l2=l4[i][1]
            if l2 == '[\'Lao Tse\']':
                LaoTse += 1
            elif l2 == '[\'Platon\']':
                Platon += 1
            elif l2 == '[\'Aristoteles\']':
                Aristoteles += 1
            elif l2 == '[\'Epicuro\']':
                Epicuro += 1
            elif l2 == '[\'Descartes\'':
                Descartes += 1
            elif l2 == '[\'Thomas Hobbes\']':
                ThomasHobbes += 1
            elif l2 == '[\'David Hume\']':
                DavidHume += 1
            elif l2 == '[\'Montesquieu\']':
                Montesquieu += 1
            elif l2 == '[\'Arthur Schopenhauer\']':
                ArthurSchopenhauer += 1
            else:
                FriedrichNietzsche += 1
        l7 = [LaoTse,Platon,Aristoteles,Epicuro,Descartes,ThomasHobbes,DavidHume,Montesquieu,ArthurSchopenhauer,FriedrichNietzsche]
        l8 = ['Lao Tse', 'Platon', 'Aristoteles', 'Epicuro', 'Descartes', 'Thomas Hobbes', 'David Hume', 'Montesquieu', 'Arthur Schopenhauer',
              'Friedrich Nietzsche']
        d3 = dict(zip(l8,l7))
        l9 = list()
        itemMaxValue = max(d3.items(), key=lambda x: x[1])    #Obtener los valores mas altos de un diccionario
        for key, value in d3.items():
            if value == itemMaxValue[1]:
                l9.append(key)
        print(l9)
        time.sleep(3)

    else:
        exit()
