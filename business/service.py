from domain.factura import *
from domain.validation import *
from math import fabs

def adauga_factura_in_lista(l, factura):
    #functie care adauga facturi intr-o lista l unic identificabile pa baza id-ului
    #input:l - lista de facturi unic identificabile
    #      factura - o factura
    #output: - daca factura a fost introdusa cu succes in lista
    #raises: Exception cu textul (2) "factura cu id existent!\n" daca exista deja o factura cu id-ul respectiv in lista l
    for _factura in l:
        if facturi_egale(factura, _factura):
            raise Exception("factura cu id existent!\n")

    l.append(factura)

def srv_adauga_in_lista(l, id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua):
    #functie care creeaza o factura cu id-ul id_factura, nume bloc nume_bloc, scara scara_bloc, apartament apartament,
    #tipul ei tip_factura, suma de plata suma
    #valideaza factura si daca e valida o adauga in lista de facturi unic identificabile daca in lista nu exita deja acel id
    #input: l - lista de facturi, celelalte sunt ca la creeaza_factura
    #output: - daca totul decurge cu succes
    #raises: Exception cu textul (1) si (2)

    factura = creeaza_factura(id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua)
    valideaza_factura(factura)
    adauga_factura_in_lista(l, factura)