# Projet Biologie - Manipulation ADN/ARN

## Description

Projet de bioinformatique en Python pour manipuler des séquences d'ADN : vérification de bases, transcription ADN vers ARN, découpage en codons et traduction en acides aminés.

## Contenu

- **biology.py** - Module principal contenant les fonctions de manipulation ADN/ARN :
  - `est_base()` / `est_adn()` - Validation de séquences
  - `arn()` - Transcription ADN -> ARN
  - `arn_to_codons()` - Découpage ARN en codons
  - `load_dico_codons_aa()` - Chargement du dictionnaire codons/acides aminés
- **test_biology.py** - Tests unitaires
- **using_biology.ipynb** - Notebook d'utilisation du module
- **data/codons_aa.json** - Table de correspondance codons / acides aminés

## Technologies

- Python
- Jupyter Notebook
