from json import *

def est_base(c):
    return c in "ATGC" and len(c) ==1


def est_adn(s):
    for c in s:
        if not est_base(c):
            return False
    return True


def arn(adn):
    if not est_adn(adn):
        return None
    tab_adn = []
    for c in adn:
        car = c
        if car == "T":
            car = "U"
        tab_adn.append(car)
    return "".join(tab_adn)


def arn_to_codons(arn):
    codon = ""
    tab_codons = []
    for c in arn:
        codon += c
        if len(codon) == 3:
            tab_codons.append(codon)
            codon = ""
    return tab_codons


def load_dico_codons_aa(filename):
    file = open(filename,"r")
    strjson = file.read()
    codons_aa = loads(strjson)
    file.close()
    return codons_aa

import itertools

def codons_stop(dico):
    strcodons = 'AUGC'
    listcodons = itertools.product(strcodons,repeat = 3)
    """
    Autre manière:
    listcodonsStop = []
    for c1 in strcodon:
    cod = c1
    for c2 in strcodon:
        cod += c2
        for c3 in strcodon:
            cod += c3
            if cod not in dico:
                listcodonsStop.append(cod)
    return listcodonsStop
    """
    listcodonsStop = []
    current = next(listcodons)
    finish = False
    while not finish:
        codon = ''.join(current)
        if codon not in dico:
            listcodonsStop.append(codon)
        try :
            current = next(listcodons)
        except StopIteration:
            finish = True
    return listcodonsStop


def codons_to_aa(codons, dico):
    tab = []
    stop = codons_stop(dico)
    for codon in codons:
        if codon in stop:
            return tab
        tab.append(dico[codon])
    return tab

#Partie 2

def nextIndice(tab, ind, elements):
    for i,val in enumerate(tab[ind:]):
        if val in elements:
            return i+ind
    return len(tab)

def decoupe_sequence(seq, start, stop):
    tab = []
    i = 0
    while i < len(seq):
        t = []
        i = nextIndice(seq,i,start)
        fin = nextIndice(seq,i+1,stop)
        for value in seq[i+1:fin] :
            t.append(value)
        if t != []:
            tab.append(t)
        i = fin + 1
    return tab


def codons_to_seq_codantes(codons, dico):
    stop = codons_stop(dico)
    start = "AUG"
    return decoupe_sequence(codons, start, stop)

def seq_codantes_to_seq_aas(seq_codantes, dico):
    tab = []
    for codons in seq_codantes:
        t = codons_to_aa(codons, dico)
        tab.append(t)
        #t = [dico[cod] for cod in codons]
        #tab.append(t)
    return tab

def adn_encode_molecule(adn, dico, molecule):
    arnMol = arn(adn)
    codonsMol = arn_to_codons(arnMol)
    seq_codantesMol = codons_to_seq_codantes(codonsMol, dico)
    moleculeAdn = seq_codantes_to_seq_aas(seq_codantesMol, dico)
    return molecule in moleculeAdn








