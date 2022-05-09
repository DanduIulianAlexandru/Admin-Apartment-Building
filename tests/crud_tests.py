from domain.factura import *
from business.service import *
from logic.crud import *

def test_afiseaza_cautari_3():
    l = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert (afiseaza_cautari_3(l, 25, 25) == return_str_factura(factura1))
    assert (afiseaza_cautari_3(l, 15, 0) == return_str_factura(factura2))

def test_afiseaza_rapoarte_3():
    l = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert (afiseaza_rapoarte_3(l, "A2", 3, 23) == str(get_tip_factura(factura1)) + " -> " + str(get_suma(factura1)) + "\n")
    assert (afiseaza_rapoarte_3(l, "A4", 2, 15) == "gaz -> " + str(get_suma(factura2)) + "\n")

def test_afiseaza_filtre_2():
    l = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert(afiseaza_filtre_2(l, 25) == return_str_factura(factura1))

def test_stergere_1():
    l = []
    sterse = []
    undo = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert (stergere_1(l, "A2", 3, 23, sterse, undo) == "Facturi eliminate cu succes!")

def test_stergere_2():
    l = []
    sterse = []
    undo = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert (stergere_2(l, "A2", 3, 22, 24, sterse, undo) == "Facturi eliminate cu succes!")

def test_go_back():
    l = []
    sterse = []
    undo = []
    factura1 = creeaza_factura(1, "A2", 3, 23, "gaz", 50, 23)
    factura2 = creeaza_factura(2, "A4", 2, 15, "gaz", 5, 10)
    adauga_factura_in_lista(l, factura1)
    adauga_factura_in_lista(l, factura2)
    assert (go_back(l, sterse, undo) == "Nu se pot face operatii de undo")