# SAE Implémentation - Codage et Décodage

## Description

Projet d'implémentation de techniques de codage et décodage de l'information, couvrant deux méthodes :

1. **Code à bit de parité simple** - Vérification de l'intégrité d'une transmission (trame de 11 bits)
2. **Chiffrement de César** - Chiffrement/déchiffrement de textes par rotation alphabétique, incluant ROT13 et une attaque par force brute

## Contenu

- **Sujet_2021.ipynb** - Notebook Jupyter contenant le sujet et les solutions
- **lorem.txt** - Fichier texte de test
- **fichier_chiffré.txt** - Résultat du chiffrement de César
- **fichier_déchiffré.txt** - Résultat du déchiffrement

## Fonctionnalités implémentées

- Conversion décimal/binaire
- Construction et vérification de trames à bit de parité
- Chiffrement/déchiffrement de César (caractère, chaîne, fichier)
- ROT13
- Attaque brute force du chiffrement de César (`hackCesar`)

## Technologies

- Python (Jupyter Notebook)
