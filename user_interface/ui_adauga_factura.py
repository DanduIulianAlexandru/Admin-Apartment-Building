from business.service import *
from time import sleep

def ui_adauga_factura(l, undo):
    try:
        id_factura = int(input("id factura:"))
    except ValueError:
        print("valoare numerica invalida pentru id-ul facturii!")
        time.sleep(3)
        return

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
    srv_adauga_in_lista(l, id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua)
    undo.append("sterge")

def ui_afiseaza_facturi(l):
    for i in range(len(l)):
        print("Factura cu numarul ", i + 1)
        to_str_factura(l[i])

    if len(l) == 0:
        print("Nu exita facturi in lista")
        sleep(1)
        return

    sleep(3)