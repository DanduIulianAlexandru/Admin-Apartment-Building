from logic.crud import *
from user_interface.main_menu import *
from time import sleep

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