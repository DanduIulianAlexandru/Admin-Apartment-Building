from user_interface.ui_adauga_factura import *
from logic.crud import *
from time import sleep
from business.service import *
from domain.factura import *

def run():
    l = []
    sterse = []
    undo = []
    while True:
        #ui_meniu()
        batch_commands = input(">>>")
        batch_list = batch_commands.split()
        k = 0
        print(batch_list)
        while k < len(batch_list):
            cmd = batch_list[k]
            if cmd == "exit":
                return
            elif cmd == "":
                continue
            elif cmd == "add_factura" or cmd == "1":
                ui_adauga_factura_batch(l, undo, batch_list, k)
                k = k + 7
            elif cmd == "show_facturi" or cmd == "2":
                ui_afiseaza_facturi(l)
            elif cmd == "delete" or cmd == "3":
                meniu_stergere(l, sterse, undo)
                continue
            elif cmd == "search" or cmd == "4":
                meniu_cautari_batch(l, batch_list, k)
                k = k + 1
                #continue
            elif cmd == "reports" or cmd == "5":
                meniu_rapoarte_batch(l, batch_list, k)
                continue
            elif cmd == "filter" or cmd == "6":
                meniu_filtre_batch(l, batch_list, k)
                continue
            elif cmd == "undo" or cmd == "7":
                try:
                    id_factura = int(input("Id-ul facturii pe care vrei sa o modifici:"))
                except ValueError:
                    print("valoare numerica invalida pentru id!")
                    #time.sleep(3)
                    return
                if id_factura < 1:
                    print("valoare numerica invalida pentru id!")
                    #time.sleep(3)
                    return
                print(modifica_batch(l, id_factura, sterse, undo, batch_list, k))
                #time.sleep(3)
            elif cmd == "undo" or cmd == "8":
                print(go_back_batch(l, sterse, undo, batch_list, k))
                #time.sleep(3)
            else:
                print("comanda invalida")
                #time.sleep(3)
            k = k + 1

def ui_adauga_factura_batch(l, undo, batch_list, k):
    batch_factura = creeaza_factura(batch_list[k + 1], batch_list[k + 2], batch_list[k + 3], batch_list[k + 4], batch_list[k + 5], batch_list[k + 6], batch_list[k + 7])
    adauga_factura_in_lista(l, batch_factura)
    undo.append("sterge")

def meniu_cautari_batch(l, batch_list, k):
    while True:
        #ui_afiseaza_meniu_cautari()
        k = k + 1
        cmd = batch_list[k]
        if cmd == "1":
            afiseaza_cautari_1_batch(l, batch_list, k)
            k = k + 2
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "2":
            afiseaza_cautari_2(l)
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "3":
            try:
                zi_data = int(input("Introduce ziua data:"))
            except ValueError:
                print("valoare numerica invalida pentru zi!")
                #time.sleep(3)
                return
            try:
                suma_data = float(input("Introduce suma data:"))
            except ValueError:
                print("valoare numerica invalida pentru suma!")
                #time.sleep(3)
                return
            print(afiseaza_cautari_3(l, zi_data, suma_data))
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            #time.sleep(3)
            return

def afiseaza_cautari_1_batch(l, batch_list, k):
    k = k + 1
    for factura in l:
        if get_suma(factura) > batch_list[k]:
            print("Adresa: Bloc " + get_nume_bloc(factura) + ", scara " + str(get_scara_bloc(factura)) + ", apartament " + str(get_apartament(factura)))


def meniu_rapoarte_batch(l, batch_list, k):
    while True:
        #ui_afiseaza_meniu_rapoarte()
        cmd = input(">>>")
        if cmd == "1":
            afiseaza_rapoarte_1(l)
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "2":
            afiseaza_cautari_2(l)
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "3":
            nume_bloc = input("numele blocului:")
            try:
                scara_bloc = int(input("scara blocului:"))
            except ValueError:
                print("valoare numerica invalida pentru scara blocului!")
                ##time.sleep(3)
                return

            try:
                apartament = int(input("apartamentul:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                #time.sleep(3)
                return
            print(afiseaza_rapoarte_3(l, nume_bloc, scara_bloc, apartament))
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            #time.sleep(3)
            return


def meniu_filtre_batch(l, batch_list, k):
    while True:
        #ui_afiseaza_meniu_filtre()
        cmd = input(">>>")
        if cmd == "1":
            afiseaza_filtre_1(l)
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "2":
            try:
                suma_data = float(input("Introduce suma data:"))
            except ValueError:
                print("valoare numerica invalida pentru suma!")
                #time.sleep(3)
                return
            print(afiseaza_filtre_2(l, suma_data))
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "3":
            return
        else:
            print("comanda incorecta!")
            #time.sleep(3)
            return

def meniu_stergere_batch(l, sterse, undo):
    while True:
        #ui_afiseaza_meniu_stergeri()
        cmd = input(">>>")
        if cmd == "1":
            nume_bloc = input("numele blocului:")

            try:
                scara_bloc = int(input("scara blocului:"))
            except ValueError:
                print("valoare numerica invalida pentru scara blocului!")
                #time.sleep(3)
                return

            try:
                apartament = int(input("apartamentul:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                #time.sleep(3)
                return
            print(stergere_1(l, nume_bloc, scara_bloc, apartament, sterse, undo))
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "2":
            nume_bloc = input("numele blocului:")

            try:
                scara_bloc = int(input("scara blocului:"))
            except ValueError:
                print("valoare numerica invalida pentru scara blocului!")
                #time.sleep(3)
                return

            try:
                apartament1 = int(input("primul apartament:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                #time.sleep(3)
                return

            try:
                apartament2 = int(input("al doilea apartament:"))
            except ValueError:
                print("valoare numerica invalida pentru apartament!")
                #time.sleep(3)
                return
            print(stergere_2(l, nume_bloc, scara_bloc, apartament1, apartament2, sterse, undo))
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "3":
            stergere_3(l, sterse, undo)
            #print("Press ENTER to continue")
            #a = input(">>>")
            return
        elif cmd == "4":
            return
        else:
            print("comanda incorecta!")
            #time.sleep(3)
            return