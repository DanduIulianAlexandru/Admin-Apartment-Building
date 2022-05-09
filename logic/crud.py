from domain.factura import *
from domain.validation import *
from math import fabs
from business.service import *
from time import sleep

def afiseaza_cautari_1(l):
    try:
        suma_data = float(input("Introduce suma data:"))
    except ValueError:
        print("valoare numerica invalida pentru suma!")
        time.sleep(3)
        return

    for factura in l:
        if get_suma(factura) > suma_data:
            print("Adresa: Bloc " + get_nume_bloc(factura) + ", scara " + str(get_scara_bloc(factura)) + ", apartament " + str(get_apartament(factura)))

def afiseaza_cautari_2(l):
    tipuri_de_facturi = ["apa", "canal", "incalzire", "gaz", "altele"]
    tipul_facturii = input(">>>Tipul de factura cautat: ")

    ok = False
    for x in tipuri_de_facturi:
        if x == tipul_facturii:
            ok = True

    if ok == False:
        print("tip de factura inexistent!")
        time.sleep(3)
        return

    for factura in l:
        if get_tip_factura(factura) == tipul_facturii:
            to_str_factura(factura)

def afiseaza_cautari_3(l, zi_data, suma_data):
    st = ""
    if zi_data > 30 or zi_data < 1:
        st += "valoare numerica invalida pentru zi!"
        return st

    for _factura in l:
        if get_suma(_factura) > suma_data and get_ziua(_factura) < zi_data:
            st += return_str_factura(_factura)

    return st

def afiseaza_rapoarte_1(l):
    tipuri_de_facturi = ["apa", "canal", "incalzire", "gaz", "altele"]
    tipul_facturii = input(">>>Tipul de factura cautat: ")

    ok = False
    for x in tipuri_de_facturi:
        if x == tipul_facturii:
            ok = True

    if ok == False:
        print("tip de factura inexistent!")
        time.sleep(3)
        return

    sum = 0

    for factura in l:
        if get_tip_factura(factura) == tipul_facturii:
            sum += get_suma(factura)

    print(sum)
    return


def afiseaza_rapoarte_3(l, nume_bloc, scara_bloc, apartament):
    st = ""
    for _factura in l:
        if get_nume_bloc(_factura) == nume_bloc and get_scara_bloc(_factura) == scara_bloc and get_apartament(_factura) == apartament:
            st += str(get_tip_factura(_factura)) + " -> " + str(get_suma(_factura)) + "\n"

    if len(st) == 0:
        st += "Nu au fost gasite cheltuieli pentru apartamentul cautat"
    return st

def afiseaza_filtre_1(l):
    tipuri_de_facturi = ["apa", "canal", "incalzire", "gaz", "altele"]
    tipul_facturii = input(">>>Tipul de factura cautat: ")

    ok = False
    for x in tipuri_de_facturi:
        if x == tipul_facturii:
            ok = True

    if ok == False:
        print("tip de factura inexistent!")
        time.sleep(3)
        return

    for _factura in l:
        if get_tip_factura(_factura) != tipul_facturii:
            to_str_factura(_factura)


def afiseaza_filtre_2(l, suma_data):
    str = ""

    for _factura in l:
        if get_suma(_factura) > suma_data:
            str += return_str_factura(_factura)
    return str

def stergere_1(l, nume_bloc, scara_bloc, apartament, sterse, undo):
    ok = False
    i = 0
    while i < len(l):
        if get_nume_bloc(l[i]) == nume_bloc and get_scara_bloc(l[i]) == scara_bloc and get_apartament(l[i]) == apartament:
            adauga_factura_in_lista(sterse, l[i])
            l.remove(l[i])
            i = i - 1
            ok = True
        i = i + 1

    if ok == False:
        return("Nu au fost gasite facturi pentru apartamentul cautat")
    else:
        undo.append("adauga")
        return("Facturi eliminate cu succes!")


def stergere_2(l, nume_bloc, scara_bloc, apartament1, apartament2, sterse, undo):
    ok = False
    i = 0
    while i < len(l):
        if get_nume_bloc(l[i]) == nume_bloc and get_scara_bloc(l[i]) == scara_bloc:
            if get_apartament(l[i]) <= apartament2 and get_apartament(l[i]) >= apartament1:
                adauga_factura_in_lista(sterse, l[i])
                l.remove(l[i])
                i = i - 1
                ok = True
        i = i + 1

    if ok == False:
        return("Nu au fost gasite facturi pentru apartamentele cautate")
    else:
        undo.append("adauga")
        return("Facturi eliminate cu succes!")

def stergere_3(l, sterse, undo):
    tipuri_de_facturi = ["apa", "canal", "incalzire", "gaz", "altele"]
    tipul_facturii = input(">>>Tipul de factura de sters: ")

    okk = False
    for x in tipuri_de_facturi:
        if x == tipul_facturii:
            okk = True

    if okk == False:
        print("tip de factura inexistent!")
        time.sleep(3)
        return

    ok = False
    i = 0

    while i < len(l):
        if get_tip_factura(l[i]) == tipul_facturii:
            adauga_factura_in_lista(sterse, l[i])
            l.remove(l[i])
            i = i - 1
            ok = True
        i = i + 1

    if ok == False:
        print("Nu au fost gasite facturi pentru tipul cautat")
    else:
        undo.append("adauga")
        print("Facturi eliminate cu succes!")

def modifica(l, id_factura, sterse, undo):
    st = ""
    ok = False
    j = i = 0
    while i < len(l):
        if get_id_factura(l[i]) == id_factura:
            ok = True
            j = i
        i = i + 1

    if ok == False:
        st += "Nu au fost gasite facturi cu id-ul cautat"
        time.sleep(3)
        return st

    nume_bloc = input("numele blocului:")

    try:
        scara_bloc = int(input("scara blocului:"))
    except ValueError:
        print("valoare numerica invalida pentru scara blocului!")
        time.sleep(3)
        return

    try:
        apartament = int(input("apartamentul:"))
    except ValueError:
        print("valoare numerica invalida pentru apartament!")
        time.sleep(3)
        return

    tip_factura = input("tipul facturii:")

    try:
        suma = float(input("suma facturii:"))
    except ValueError:
        print("valoare numerica invalida pentru suma!")
        time.sleep(3)
        return

    try:
        ziua = int(input("ziua facturarii:"))
    except ValueError:
        print("valoare numerica invalida pentru zi!")
        time.sleep(3)
        return

    factura = creeaza_factura(id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua)

    try:
        valideaza_factura(factura)
        sterse.append(l[j])
        l.remove(l[j])
        undo.append("modifica")
        adauga_factura_in_lista(l, factura)
    except Exception as ex:
        return ex

    st += "Factura modificata cu succes!"
    return st



def go_back(l, sterse, undo):
    st = ""
    if len(undo) == 0:
        st += "Nu se pot face operatii de undo"
        return st

    if undo[len(undo) - 1] == "sterge":
        l.pop()
        undo.pop()
        st += "Operatie realizata cu succes"
        return st

    if undo[len(undo) - 1] == "adauga":
        l.append(sterse[0])
        sterse.remove(sterse[0])
        undo.pop()
        st += "Operatie realizata cu succes"
        return st

    if undo[len(undo) - 1] == "modifica":
        l.pop()
        l.append(sterse[0])
        sterse.remove(sterse[0])
        undo.pop()
        st += "Operatie realizata cu succes"
        return st