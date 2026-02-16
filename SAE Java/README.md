# SAE Java - Calculatrice Orientée Objet

## Description

Calculatrice en Java utilisant le pattern **arbre d'expressions** (Composite). Chaque expression arithmétique est représentée sous forme d'arbre où les feuilles sont des nombres et les noeuds internes sont des opérations.

## Structure

```
SAE Java/
├── src/                    # Code source
│   ├── Expression.java     # Interface commune
│   ├── Nombre.java         # Feuille : nombre entier
│   ├── Operation.java      # Classe abstraite pour les opérations
│   ├── Addition.java       # Opération addition
│   ├── Soustraction.java   # Opération soustraction
│   ├── Multiplication.java # Opération multiplication
│   ├── Division.java       # Opération division (gestion division par 0)
│   ├── Calculatrice.java   # Programme principal (expressions composées)
│   └── CalculatriceSimple.java # Programme principal (opérations simples)
├── class/                  # Fichiers compilés
├── Execution.pdf           # Capture d'écran de l'exécution
└── UML.pdf                 # Diagramme UML des classes
```

## Compilation et exécution

```bash
cd src
javac -d ../class *.java
cd ../class
java Calculatrice
java CalculatriceSimple
```

## Technologies

- Java (POO, héritage, polymorphisme)
