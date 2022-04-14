# TO DO
from biology import *

def test_est_base():
    assert est_base('A')
    assert est_base('T')
    assert est_base('G')
    assert est_base('C')
    assert not est_base('@')
    assert not est_base('Z')
    assert not est_base('z')
    assert not est_base('AU')
    print('Test de la fonction est_base ok')

def test_est_adn():
    assert est_adn('ATGTCAAA')
    assert not est_adn('ATBOAATG')
    print('Test de la fonction est_adn ok')

def test_arn():
    assert arn('ATGTCAAA') == 'AUGUCAAA'
    assert arn('NonArn') == None
    assert arn('AGCAGACCA') == 'AGCAGACCA'
    print('Test de la fonction arn ok')

def test_arn_to_codons():
    assert arn_to_codons('CGUUAGGGG') == ["CGU", "UAG", "GGG"]
    assert arn_to_codons('CGUAAU') == ["CGU", "AAU"]
    assert arn_to_codons('CGUAAUGC') == ["CGU", "AAU"]
    print('Test de la fonction arn_to_codons ok')

def test_load_dico_codons_aa():
    dico = load_dico_codons_aa('data/codons_aa.json')
    assert type(dico) == dict
    assert dico["UUU"] == "Phenylalanine"
    assert dico["CCC"] == "Proline"
    assert not dico["UUU"] == "Proline"
    print('Test de la fonction load_dico_codons_aa ok')

def test_codons_stop():
    dico = load_dico_codons_aa('data/codons_aa.json')
    stop = codons_stop(dico)
    assert len(stop) == 3
    assert 'UAA' in stop
    assert 'UAG' in stop
    assert 'UGA' in stop
    print('Test de la fonction codons_stop ok')

def test_codons_to_aa():
    dico = load_dico_codons_aa('data/codons_aa.json')
    assert codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"],dico) == ["Arginine", "Asparagine"]
    assert codons_to_aa(["CGU", "AAU", "UUU", "GGG", "CGU"],dico) == ["Arginine", "Asparagine",'Phenylalanine','Glycine','Arginine']
    assert codons_to_aa(["UAG", "AAU", "UAA", "GGG", "CGU"],dico) == []
    print('Test de la fonction codons_to_aa ok')

def test_nextIndice():
    tab = ["bonjour", "hello", "buongiorno", "ciao", "bye"]
    elements = ["hello", "bye"]
    assert nextIndice(tab,0,elements) == 1
    assert nextIndice(tab,1,elements) == 1
    assert nextIndice(tab,2,elements) == 4
    elements = ["yo", "ya"]
    assert nextIndice(tab,0,elements) == 5
    elements = ["bye", "hello"]
    assert nextIndice(tab,0,elements) == 1
    elements = ["buongiorno"]
    assert nextIndice(tab,0,elements) == 2
    elements = ["ciao"]
    assert nextIndice(tab,0,elements) == 3
    print('Test de la fonction nextIndice ok')

def test_decoupe_sequence():
    seq = ["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"]
    start = ["début", "begin"]
    stop = ["fin", "end"]
    assert decoupe_sequence(seq, start, stop) == [ ["val2", "val3"], ["val5"] ]
    seq = ["début","end","val1", "val2","begin","fin","val3", "val4", "val5", "fin", "val6"]
    assert decoupe_sequence(seq, start, stop) == []
    seq = ["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"]
    start = ["commencement", "start"]
    stop = ["terminado", "finito"]
    assert decoupe_sequence(seq, start, stop) == []
    print('Test de la fonction decoupe_sequence ok')

def test_codons_to_seq_codantes():
    dico = load_dico_codons_aa('data/codons_aa.json')
    stop = codons_stop(dico)
    d = ["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"]
    assert codons_to_seq_codantes(d,dico) == [['CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    d = ["AUG", "UUU", "CGU", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "UAG", "CGU", "GGG"]
    assert codons_to_seq_codantes(d,dico) == [["UUU", "CGU", "CGU", "AUG", "AAU"],['GGG', 'CCC']]
    print('Test de la fonction codons_to_seq_codantes ok')

def test_seq_codantes_to_seq_aas():
    dico = load_dico_codons_aa('data/codons_aa.json')
    seq = [['CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    assert seq_codantes_to_seq_aas(seq,dico) == [['Arginine', 'Methionine', 'Asparagine'], ['Glycine', 'Proline', 'Arginine']]
    seq = [['CGU', 'CCC', 'AAU'], ['GGG', 'AAU', 'CGU']]
    assert seq_codantes_to_seq_aas(seq,dico) == [['Arginine', 'Proline', 'Asparagine'], ['Glycine', 'Asparagine', 'Arginine']]
    print('Test de la fonction seq_codantes_to_seq_aas ok')

def test_adn_encode_molecule():
    dico = load_dico_codons_aa('data/codons_aa.json')
    adn = "CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG"
    molecule = ["Glycine", "Proline", "Arginine"]
    assert adn_encode_molecule(adn,dico,molecule)
    molecule = ['Arginine', 'Methionine', 'Asparagine']
    assert adn_encode_molecule(adn,dico,molecule)
    adn = "CGTTTTATGCGTATGAATTAAATGGGGCCCTAGGGG"
    molecule = ["Glycine", "Proline"]
    assert adn_encode_molecule(adn,dico,molecule)
    adn = "CGTTTTATGCGTATGAATTAAATGGGGTAGCCCCGTGGG"
    molecule = ["Glycine"]
    assert adn_encode_molecule(adn,dico,molecule)
    print('Test de la fonction adn_encode_molecule ok')










