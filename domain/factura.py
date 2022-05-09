EPSILON = 0.0001

def creeaza_factura(id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua):
    """functie care creeaza o factura pentru un apartament
    factura va avea:
    * un id_factura numar natural unic
    * numele blocului de unde e apartamentul un string format dintr-o litera mare si un numar natural
    * scara_bloc un numar natural din intervalul  [1, 10]
    * apartamentul care va fi un numar intreg pozitiv din intervalul [scara * 10 - 10, scara * 10]
    * tip_factura care va fi un string din lista :  [apa, canal, incalzire, gaz, altele]
    * suma care va fi un numar real pozitiv
    * ziua care va fi un numar natural din intervalul [1, 30]

    * - input

    output: o factura"""

    return {
        "id_factura": id_factura,
        "nume_bloc": nume_bloc,
        "scara_bloc": scara_bloc,
        "apartament": apartament,
        "tip_factura": tip_factura,
        "suma": suma,
        "ziua": ziua
    }


"""def creeaza_factura(id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua):
    return [id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua]"""


def get_id_factura(factura):
    # input: o factura
    # output: id-ul intreg al pozei
    return factura["id_factura"]


def get_nume_bloc(factura):
    # input: o factura
    # output: stringul cu numele blocului
    return factura["nume_bloc"]


def get_scara_bloc(factura):
    # input: o factura
    # output: numarul natural care reprezinta scara blocului
    return factura["scara_bloc"]


def get_apartament(factura):
    # input: o factura
    # output: numarul apartamentului facturat
    return factura["apartament"]


def get_tip_factura(factura):
    # input: o factura
    # output: string-ul cu tipul facturii
    return factura["tip_factura"]


def get_suma(factura):
    # input: o factura
    # output: numarul real ce reprezinta suma de plata a facturii
    return factura["suma"]


def get_ziua(factura):
    # input: o factura
    # output: numarul natural ce reprezinta ziua in care a fost facuta factura
    return factura["ziua"]


def to_str_factura(factura):
    print("Id: ", factura["id_factura"])
    print("Adresa: Bloc " + factura["nume_bloc"] + ", scara ", factura["scara_bloc"], ", apartament ",
          factura["apartament"])
    print("Tip factura: " + factura["tip_factura"])
    print("Suma de plata: ", factura["suma"])
    print("Ziua facturarii: ", factura["ziua"])


"""def to_str_factura(factura):
    print("Id: ", factura[0])
    print("Adresa: Bloc " + factura[1] + ", scara " ,factura[2], ", apartament ", factura[3])
    print("Tip factura: " + factura[4])
    print("Suma de plata: ", factura[5])
    print("Ziua facturarii: ", factura[6])"""


def return_str_factura(factura):
    st = "Id: " + str(factura["id_factura"]) + "\n" + "Adresa: Bloc " + factura["nume_bloc"] + ", scara " + str(
        factura["scara_bloc"]) + ", apartament " + "\n" + str(factura["apartament"]) + "\n" + "Tip factura: " + factura[
             "tip_factura"] + "\n" + "Suma de plata: " + str(factura["suma"]) + "\n" + "Ziua facturarii: " + str(
        factura["ziua"]) + "\n"
    return st


"""def return_str_factura(factura):
    st = "Id: " + str(factura[0]) + "\n" + "Adresa: Bloc " + factura[1] + ", scara " + str(factura[2]) + ", apartament " + "\n" + str(factura[3]) + "\n" + "Tip factura: " + factura[4] + "\n" + "Suma de plata: " + str(factura[5]) + "\n" + "Ziua facturarii: " + str(factura[6]) + "\n"
    return st"""

def facturi_egale(factura1, factura2):
    #functie care verifica egalitatea id-urilor a doua facturi
    return get_id_factura(factura1) == get_id_factura(factura2)