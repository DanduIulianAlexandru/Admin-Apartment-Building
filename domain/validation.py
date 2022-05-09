from domain.factura import *
from math import fabs

def valideaza_nume_bloc(nume_bloc):
    #functie care valideaza numele blocului primit ca parametru in functia creeaza_factura
    #numele blocului trebuie sa fie format din o majuscula si o cifra
    #input:nume_bloc
    #output: True or False in functie de validarea datelor
    if len(nume_bloc) != 2:
        return False
    if str.isupper(nume_bloc[0]) == False:
        return False
    if nume_bloc[1] == "0":
        return False
    if nume_bloc[1].isdigit() == False:
        return False
    return True

def valideaza_apartament(apartament, scara_bloc):
    #functie care verifica daca apartamentul se afla la scara corecta
    #se verifica daca apartamentul se afla in intervalul [ (scara_bloc - 1) * 10 + 1, scara_bloc * 10]
    #input: numarul apartamentului, scara blocului in caz
    #output: True or False in functie de parametrii
    if apartament == 0:
        return False
    if apartament < (scara_bloc - 1) * 10 + 1:
        return False
    if apartament > scara_bloc * 10:
        return False
    return True

def valideaza_tip_factura(tip_factura):
    #functie care valideaza existenta tipului de factura in lista tipuri_de_facturi
    #input: tipul facturii
    #output: True in caz de gaseste tipul in lista
    #        False in caz de nu o gaseste
    tipuri_de_facturi = ["apa", "canal", "incalzire", "gaz", "altele"]
    for el in tipuri_de_facturi:
        if tip_factura == el:
            return True

    return False

def valideaza_factura(factura):
    #functie care valideaza corectitudinea parametrilor unei poze create:
    #id > 0, nume format din majuscula plus cifra, scara_bloc > 0, apartament aflat in intervalul specific scarii, tip factura existent, suma > 0, ziua apartine [1, 30]
    #output: nimic daca factura e valida
    #raises : Exception cu textul: (1)
    #                   "id factura invalid!\n" daca id < 0
    #                   "nume bloc invalid!\n" daca nume_bloc nu este corect format
    #                   "scara bloc invalida!\n" daca scara_bloc < 0
    #                   "apartament invalid!\n" daca apartament nu se afla in intervalul corect
    #                   "tip factura invalida!\n"  daca tipul facturii nu se afla in lista existenta
    #                   "suma invalida!\n" daca suma < 0
    #                   "ziua invalida!\n" daca ziua nu apartine [1, 30]
    err = ""
    if get_id_factura(factura) <= 0:
        err += "id factura invalid!\n"
    if valideaza_nume_bloc(get_nume_bloc(factura)) == False:
        err += "nume bloc invalid!\n"
    if get_scara_bloc(factura) < 1:
        err += "scara bloc invalida!\n"
    if valideaza_apartament(get_apartament(factura), get_scara_bloc(factura)) == False:
        err += "apartament invalid!\n"
    if valideaza_tip_factura(get_tip_factura(factura)) == False:
        err += "tip factura invalida!\n"
    if get_suma(factura) < 0:
        err += "suma invalida!\n"
    if get_ziua(factura) < 1 or get_ziua(factura) > 30:
        err += "ziua invalida!\n"

    if len(err) > 0:
        raise Exception(err)