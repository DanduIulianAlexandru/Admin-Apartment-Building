from domain.factura import *
from domain.validation import *
from business.service import *
from tests.crud_tests import *

def test_valideaza_nume_bloc():
    #functie care verifica valideaza_nume_bloc
    assert valideaza_nume_bloc("A3") == True
    assert valideaza_nume_bloc("") == False
    assert valideaza_nume_bloc("CC") == False
    assert valideaza_nume_bloc("3242f") == False
    assert valideaza_nume_bloc("A") == False
    assert valideaza_nume_bloc("33") == False
    assert valideaza_nume_bloc("D4") == True
    assert valideaza_nume_bloc("c3") == False
    assert valideaza_nume_bloc("D0") == False

def test_valideaza_apartament():
    #functie care verifica folosind assert-uri corectitudinea funtctiei valideaza_apartament
    assert valideaza_apartament(23, 3) == True
    assert valideaza_apartament(4, 1) == True
    assert valideaza_apartament(10, 2) == False
    assert valideaza_apartament(31, 1) == False
    assert valideaza_apartament(-13, 3) == False
    assert valideaza_apartament(25, 2) == False
    assert valideaza_apartament(20, 2) == True
    assert valideaza_apartament(55, 6) == True
    assert valideaza_apartament(0, 1) == False

def test_valideaza_tip_factura():
    #functie care verifica folosind assert-uri corectitudinea functiei valideaza_tip_factura
    assert valideaza_tip_factura("gaz") == True
    assert valideaza_tip_factura("bere") == False
    assert valideaza_tip_factura("") == False
    assert valideaza_tip_factura("33") == False
    assert valideaza_tip_factura("altele") == True

def test_valideaza_factura():
    factura = creeaza_factura(32, "B4", 3, 25, "apa", 213.12, 3)
    valideaza_factura(factura)

    invalid_id_factura = creeaza_factura(-3, "B4", 3, 25, "apa", 213.12, 3)
    try:
        valideaza_factura(invalid_id_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "id factura invalid!\n")

    invalid_nume_bloc_factura = creeaza_factura(23,"33", 3, 25, "canal", 32.4, 6)
    try:
        valideaza_factura(invalid_nume_bloc_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "nume bloc invalid!\n")

    invalid_scara_bloc_factura = creeaza_factura(4,"B6", 0, -5, "apa", 23.42, 4)
    try:
        valideaza_factura(invalid_scara_bloc_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "scara bloc invalida!\n")

    invalid_apartament_factura = creeaza_factura(4, "B4", 4, 5, "apa", 324.23, 5)
    try:
        valideaza_factura(invalid_apartament_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "apartament invalid!\n")

    invalid_tip_factura = creeaza_factura(4, "C7", 3, 24, "bere", 23.4, 6)
    try:
        valideaza_factura(invalid_tip_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "tip factura invalida!\n")

    invalid_suma_factura = creeaza_factura(234, "D2", 2, 14, "gaz", -53.4, 23)
    try:
        valideaza_factura(invalid_suma_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "suma invalida!\n")

    invalid_ziua_factura = creeaza_factura(12, "B6", 2, 14, "apa", 23.5, 55)
    try:
        valideaza_factura(invalid_ziua_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "ziua invalida!\n")

    invalid_all_factura = creeaza_factura(0, "SD", -4, 31, "dunno", -23, -3)
    try:
        valideaza_factura(invalid_all_factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "id factura invalid!\nnume bloc invalid!\nscara bloc invalida!\napartament invalid!\ntip factura invalida!\nsuma invalida!\nziua invalida!\n")

def test_creeaza_factura():
    id_factura = 341
    nume_bloc = "A3"
    scara_bloc = 2
    apartament = 15
    tip_factura = "gaz"
    suma = 941.56
    ziua = 16
    factura = creeaza_factura(id_factura, nume_bloc, scara_bloc, apartament, tip_factura, suma, ziua)
    assert(get_id_factura(factura) == id_factura)
    assert(get_nume_bloc(factura) == nume_bloc)
    assert(get_scara_bloc(factura) == scara_bloc)
    assert(get_apartament(factura) == apartament)
    assert(get_tip_factura(factura) == tip_factura)
    assert(fabs(get_suma(factura) - suma) < EPSILON)
    assert(get_ziua(factura) == ziua)

def test_adauga_factura_in_lista():
    l = []
    assert(len(l) == 0)
    factura = creeaza_factura(1, "A3", 1, 15, "gaz", 954, 23)
    adauga_factura_in_lista(l, factura)
    assert(len(l) == 1)
    assert(get_id_factura(factura) == get_id_factura(l[0]))
    assert(get_nume_bloc(factura) == get_nume_bloc(l[0]))
    assert(get_apartament(factura) == get_apartament(l[0]))
    assert(get_scara_bloc(factura) == get_scara_bloc(l[0]))
    assert(get_tip_factura(factura) == get_tip_factura(l[0]))
    assert(fabs(get_suma(factura) - get_suma(l[0])) < EPSILON)

    try:
        adauga_factura_in_lista(l, factura)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "factura cu id existent!\n")

def test_srv_adauga_in_lista():
    l = []
    srv_adauga_in_lista(l, 12, "A3", 3, 24, "canal", 332.4, 15)
    assert(len(l) == 1)
    try:
        srv_adauga_in_lista(l, 12, "A3", 3, 24, "canal", 332.4, 15)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "factura cu id existent!\n")

    try:
        srv_adauga_in_lista(l, 3, "fgh", 2, 15, "apa", 32.3, 5)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "nume bloc invalid!\n")

def run_teste():
    test_creeaza_factura()
    test_valideaza_nume_bloc()
    test_valideaza_apartament()
    test_valideaza_tip_factura()
    test_valideaza_factura()
    test_adauga_factura_in_lista()
    test_srv_adauga_in_lista()
    test_afiseaza_filtre_2()
    test_stergere_1()
    test_stergere_2()
    test_afiseaza_cautari_3()
    test_afiseaza_rapoarte_3()
    test_go_back()