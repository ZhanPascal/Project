'''
module: analyseur.py
description: reçoit l'état d'un tableau de cakes et analyse la présence
  d'un ou plusieurs groupes de cakes alignés
'''

class Analyseur:
    def __init__(self, tab):
        # on fait confiance au tableau créé qui est fourni par tab_cakes
        self.__tab = tab
        self.__largeur = len(tab)
        self.__longueur = len(tab[0])

    def getCell(self, line, col):
        if line < 0 or line >= self.__largeur:
            return None
        if col < 0 or col >= self.__longueur:
            return None
        return self.__tab[line][col]

    def clearCell(self, line, col):
        if line < 0 or line >= self.__largeur:
            return
        if col < 0 or col >= self.__longueur:
            return
        self.__tab[line][col] = None

    def look_for_groups(self):
        '''
        lance l'analyse du tableau selon la méthode définie par Dave
        '''
        groupes = []

        for x in range(self.__largeur):
            for y in range(self.__longueur):
                if self.getCell(x, y) == self.getCell(x + 1, y) == self.getCell(x + 2, y) != None:
                    bonbon = self.getCell(x,y)
                    deplacement = 0
                    supp = []
                    while self.getCell(x + deplacement, y) == bonbon:
                        supp.append((x + deplacement, y))
                        self.clearCell(x,y)
                        deplacement += 1
                    groupes.append(supp)
                if self.getCell(x, y) == self.getCell(x, y + 1) == self.getCell(x, y + 2) != None:
                    bonbon = self.getCell(x,y)
                    deplacement = 0
                    supp = []
                    while self.getCell(x, y + deplacement) == bonbon:
                        supp.append((x, y + deplacement))
                        self.clearCell(x,y)
                        deplacement += 1
                    groupes.append(supp)

        return groupes


    def look_for_falls(self):
        '''
        cherche les cases vides et fait descendre les items au
        dessus des cases vides.
        Renvoie la liste des coordonnées des cases où se trouve
        un cake qui doit descendre ainsi que le nombre de cases
        de la descente.
        Par exemple :
        [(2,1,4), (4,1,3)]
        Ce tableau sera utilisé par la boucle principale pour commander
        la mise à jour de tab_cakes.
        L'idée est de permettre la communication entre Tableau et TabCakes
        sans qu'on est besoin de créer explicitement des dépendances entre
        les deux. De plus les classes fonctionnent indépendamment les
        unes des autres le mieux c'est (sinon on forme des sac de noeuds...)
        C'est le programme principal qui, voyant les deux structures en
        parallèle, peut se charger de faire communiquer les deux.
        '''
        #<Pascal> Pour Dave: J'ai modifié un peu cette fonction, si t as des questions tu peux me les poser
        caseVide = []
        for column in range(self.__longueur):
          nb_descente = 0
          for line in range(self.__largeur) :
            if nb_descente != 0:
              if self.__tab[-line-1][column] != None:
                caseVide.append((self.__largeur - line-1, column ,nb_descente))
            if self.__tab[-line-1][column] == None:
              nb_descente += 1
        return caseVide




    def look_for_refill(self):
        '''
        Après avoir détecté les groupes, ce qui supprime des cakes,
        après avoir fait tomber les cakes,
        vous avez le choix : est-ce que l'on attend qu'il ne se passe
        plus rien avant de remettre des cakes ? est-ce qu'on en remet
        dès que des trous se forment ? à vous de voir, mais à un moment
        il faudra reremplir.
        Même système, cette fonction, en même temps qu'elle réactualise
        le tableau, renvoie une liste qui informe le programme principal
        des changements effectués ce qui permettra au programme principal
        de demander à tab_cakes de répercuter graphiquement ces changements.
        '''
        #La chute est déjà faite
        # renvoie une liste avec les index des cases à remplir
        #<Pascal> La fonction renvoie les index des cases à remplir dans un tableau
        caseAremplir = []
        for line in range(self.__largeur):
          for column in range(self.__longueur) :
            if self.__tab[line][column] == None:
              caseAremplir.append((line,column))
        return caseAremplir

