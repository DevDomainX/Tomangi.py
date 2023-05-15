#!/usr/bin/env python3
# Author: Hans Saldias
# Script solo para mayores de 18 años ya que es un juego para consumo de alcohol
from colorama import init, Fore, Style, Back
import os
from time import sleep
from random import choice
init()

from random import choice



def Ingreso():
    print(Fore.LIGHTCYAN_EX+"                 ****Ingreso de jugadores  ****\n")
    print("""
    Este juago tiene Ingreso de 10 jugadores y 10 tragos

    al no tener 10 solo ingresen los que tengan y en el resto solo dele enter
    
    Create by: Hans Saldias \n
    """.title())
    
    intentos = 0
    jugador1 = input("Ingrese nombre 1: ")
    jugador2 = input("Ingrese nombre 2: ")
    jugador3 = input("Ingrese nombre 3: ")
    jugador4 = input("Ingrese nombre 4: ")
    jugador5 = input("Ingrese nombre 5: ")
    jugador6 = input("Ingrese nombre 6: ")
    jugador7 = input("Ingrese nombre 7: ")
    jugador8 = input("Ingrese nombre 8: ")
    jugador9 = input("Ingrese nombre 9: ")
    jugador10 = input("Ingrese nombre 10: ")
    jugadores = choice([jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8, jugador9, jugador10])
    print("\n"* 3)
    os.system("clear")
    print("          ****  Ingreso de tragos que tienen *****\n")

    trago1 = input("Ingrese primer trago:")
    trago2 = input("Ingrese segundo trago:")
    trago3 = input("Ingrese tercer trago:")
    trago4 = input("Ingrese cuarto trago:")
    trago5 = input("Ingrese quinto trago:")
    trago6 = input("Ingrese cesto trago:")
    trago7 = input("Ingrese septimo trago:")
    trago8 = input("Ingrese octavo trago:")
    trago9 = input("Ingrese noveno trago:")
    trago10 = input("Ingrese decimo trago:")
    tragos = choice([trago1, trago2, trago3, trago4, trago5, trago6, trago7, trago8, trago9, trago10])



    while intentos < 20:
        jugadores = choice([jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8, jugador9, jugador10])
        tragos = choice([trago1, trago2, trago3, trago4, trago5, trago6, trago7, trago8, trago9, trago10])
        op = input("\nElegir uno al asar presiona (Enter) ")
        print("Revolviendo ......\n")
        sleep(5)
        os.system("clear")
        print(f"       **** El jugador {jugadores} debe tomar 1 vaso de {tragos} ******\n\n")
        print("SI deseas salir del juego solo escriba 'salir' ".title())
        if op == "salir":
            print("Gracias por jugar...")
            sleep(4)
            break
        

edad = int(input(Fore.LIGHTGREEN_EX+"\nIngrese su edad: "))

if edad >= 18:
    print("\nEres mayor de edad cargando juego .... ...")
    sleep(5)
    Ingreso()
else:
    print("\nLo siento, este juego es para adultos :(".title())
                     
                 
