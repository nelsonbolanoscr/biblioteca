# Programa de Biblioteca
# Creado por Nelson Bolaños

import csv
import pandas
import time

def leer(nombre):
    with open(nombre, mode = 'r') as t:
        autreader = csv.reader(t)
        return list(autreader)

r1 = leer('autores.csv')
r2 = leer('libros.csv')


with open('prestamo.csv', mode='w', newline='') as File:
    escritor = csv.writer(File)

x=0
while x < 5:
    c1 = 0
    c2 = 0
    autor = (input('Ingrese Autor: '))
    libro = (input('Ingrese Titulo del Libro: '))
    dia = (input('Ingrese Dia de la Semana: '))
    fecha = (input('Ingrese Fecha: '))

    for au in r1:
        for au1 in au:
            c1 += 1
            if au1 == str(autor):
                break

    for li in r2:
        for li1 in li:
            c2 += 1
            if li1 == str(libro):
                break

    if c1 == c2:
        x += 1
        with open('prestamo.csv', 'a', newline='') as t:
            writer = csv.writer(t)
            test = list(libro,autor,dia,fecha)

            for i in test:
                writer.writerow(i)
    else:
        print("wrong")
        pass
"""
    with open('prestamo.csv', 'a', newline='') as s:
        writer = csv.writer(s)
        test = list(autor,libro,dia,fecha)

        for i in test:
            writer.writerow(i)

"""

