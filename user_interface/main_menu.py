from user_interface.ui_adauga_factura import *
from logic.crud import *
from time import sleep

def ui_meniu():
    print("Administrare facturi:")
    print("1. Adăugare(add_factura)")
    print("2. Afisare facturi(show_facturi)")
    print("3. Ștergere")
    print("4. Căutări")
    print("5. Rapoarte")
    print("6. Filtreaza facturi")
    print("7. Modifica factura")
    print("8. Undo")

def ui_afiseaza_meniu_stergeri():
    print("1. Șterge toate cheltuielile de la un apartament")
    print("2. Șterge cheltuielile de la apartamente consecutive")
    print("3. Șterge cheltuielile de un anumit tip de la toate apartamentele")
    print("4. Inapoi")

def ui_afiseaza_meniu_cautari():
    print("1. Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată")
    print("2. Tipărește cheltuielile de un anumit tip de la toate apartamentele")
    print("3. Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua)")
    print("4. Inapoi")

def ui_afiseaza_meniu_rapoarte():
    print("1. Tipărește suma totală pentru un tip de cheltuială")
    print("2. Tipărește toate apartamentele sortate după un tip de cheltuială")
    print("3. Tipărește totalul de cheltuieli pentru un apartament dat")
    print("4. Inapoi")

def ui_afiseaza_meniu_filtre():
    print("1. Elimină toate cheltuielile de un anumit tip")
    print("2. Elimină toate cheltuielile mai mici decât o sumă dată")
    print("3. Inapoi")

def run():
    l = []
    sterse = []
    undo = []
    while True:
        ui_meniu()
        cmd = input(">>>")
        if cmd == "exit":
            return
        elif cmd == "":
            continue
        elif cmd == "add_factura" or cmd == "1":
            try:
                ui_adauga_factura(l, undo)
            except Exception as ex:
                print(ex)
        elif cmd == "show_facturi" or cmd == "2":
            ui_afiseaza_facturi(l)
        elif cmd == "delete" or cmd == "3":
            meniu_stergere(l, sterse, undo)
            continue
        elif cmd == "search" or cmd == "4":
            meniu_cautari(l)
            continue
        elif cmd == "reports" or cmd == "5":
            meniu_rapoarte(l)
            continue
        elif cmd == "filter" or cmd == "6":
            meniu_filtre(l)
            continue
        elif cmd == "undo" or cmd == "7":
            try:
                id_factura = int(input("Id-ul facturii pe care vrei sa o modifici:"))
            except ValueError:
                print("valoare numerica invalida pentru id!")
                time.sleep(3)
                return
            if id_factura < 1:
                print("valoare numerica invalida pentru id!")
                time.sleep(3)
                return
            print(modifica(l, id_factura, sterse, undo))
            sleep(3)
        elif cmd == "8":
            print(go_back(l, sterse, undo))
            """print(sterse)
            print("\n\n\n")
            print(undo)"""
            sleep(3)
        else:
            print("comanda invalida")
            sleep(3)

def meniu_cautari(l):
    while True:
        ui_afiseaza_meniu_cautari()
        cmd = input(">>>")
        if cmd == "1":
            afiseaza_cautari_1(l)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "2":
            afiseaza_cautari_2(l)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "3":
            try:
                zi_data = int(input("Introduce ziua data:"))
            except ValueError:
                print("valoare numerica invalida pentru zi!")
                time.sleep(3)
                return
            try:
                suma_data = float(input("Introduce suma data:"))
            except ValueError:
                print("valoare numerica invalida pentru suma!")
                time.sleep(3)
                return
            print(afiseaza_cautari_3(l, zi_data, suma_data))
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            sleep(3)
            return


def meniu_rapoarte(l):
    while True:
        ui_afiseaza_meniu_rapoarte()
        cmd = input(">>>")
        if cmd == "1":
            afiseaza_rapoarte_1(l)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "2":
            afiseaza_cautari_2(l)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "3":
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
            print(afiseaza_rapoarte_3(l, nume_bloc, scara_bloc, apartament))
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            sleep(3)
            return


def meniu_filtre(l):
    while True:
        ui_afiseaza_meniu_filtre()
        cmd = input(">>>")
        if cmd == "1":
            afiseaza_filtre_1(l)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "2":
            try:
                suma_data = float(input("Introduce suma data:"))
            except ValueError:
                print("valoare numerica invalida pentru suma!")
                time.sleep(3)
                return
            print(afiseaza_filtre_2(l, suma_data))
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "3":
            return
        else:
            print("comanda incorecta!")
            sleep(3)
            return

def meniu_stergere(l, sterse, undo):
    while True:
        ui_afiseaza_meniu_stergeri()
        cmd = input(">>>")
        if cmd == "1":
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
            print(stergere_1(l, nume_bloc, scara_bloc, apartament, sterse, undo))
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "2":
            nume_bloc = input("numele blocului:")

            try:
                scara_bloc = int(input("scara blocului:"))
            except ValueError:
                print("valoare numerica invalida pentru scara blocului!")
                time.sleep(3)
                return

            try:
                apartament1 = int(input("primul apartament:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                time.sleep(3)
                return

            try:
                apartament2 = int(input("al doilea apartament:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                time.sleep(3)
                return
            print(stergere_2(l, nume_bloc, scara_bloc, apartament1, apartament2, sterse, undo))
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "3":
            stergere_3(l, sterse, undo)
            print("Press ENTER to continue")
            a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            sleep(3)
            return