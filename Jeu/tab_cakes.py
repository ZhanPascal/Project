'''
module: tab_cakes
descripton: définit l'objet TabCakes reponsable de la grille de cakes, de sa mise à jour et de son évolution.
'''

import pygame
from cake import Cake
from random import randrange
from analyseur import Analyseur

class TabCakes:
    def __init__(self, x0, y0, largeur, hauteur, maxClicked = 30):
        self.__x0 = x0 # x du coin haut gauche
        self.__y0 = y0 # y du coin haut gauche
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__group = pygame.sprite.Group()
        self.__init_cakes()
        self.__mode = 0
        self.__cake_clicked1 = None
        self.__cake_clicked2 = None
        self.score = 0
        self.clicked = maxClicked
        self.__maxClicked = maxClicked
        '''
        tabCakes a plusieurs modes:
        0 : attente d'un click. Dans ce mode un cake peut être sélectionné
        1 : permutation en cours : deux cakes venant d'être cliqués se déplacent. On doit mémoriser l'endroit de la permutation pour éventuellement l'annuler.
        2: analyse
            si le tableau a des groupes -> 3
            si le tableau a des trous avec des cakes pouvant tomber -> 4
            si le tableau a des trous mais rien pouvant tomber -> 5
            si aucune action n'a été faite -> 6
            si des actions ont été faites mais que tout est fini -> 0
        3: destruction de groupes (animation) -> 2 quand fini
        4: déplacement de cakes (animation) -> 2 quand fini
        5: remplissement (animation) -> 2 quand fini
        6: annulation de la permutation, mouvement inverse -> 0 quand fini
        '''
        self.__last_permutation = None
        '''
        __last_permutation contiendra les coordonnées des 2 cases permutées par click
        '''
        self.__something_done = False
        '''
        marqueur pour savoir si une permutation à provoquer quelque chose
        '''

    def __init_cakes(self):
        '''
        création initiale des cakes
        '''
        # création d'un tableau vide
        self.__cakes = [[None for col in range(self.__largeur)] for line in range(self.__hauteur)]
        # remplissage du tableau
        for line in range(self.__hauteur):
            for col in range(self.__largeur):
                r = randrange(Cake.OBJET_MAX)
                self.addCake(line, col, r)

    def getLineColFromCake(self, cake):
        x = cake.rect.x
        y = cake.rect.y
        line = (y - self.__y0)//Cake.CELL_SIZE
        col = (x - self.__x0)//Cake.CELL_SIZE
        return line,col

    def addCake(self, line, col, categorie):
        '''
        Création d'un cake de catégorie donnée en line et colonne
        '''
        assert 0 <= line < self.__hauteur
        assert 0 <= col < self.__largeur
        assert self.__cakes[line][col] == None
        new_cake = Cake(self.__x0 + col*Cake.CELL_SIZE, self.__y0 + line*Cake.CELL_SIZE, categorie)
        self.__cakes[line][col] = new_cake
        self.__group.add(new_cake)

    def getGroup(self):
        return self.__group

    def onclick(self, cake):
        '''
        Réagit au click sur un cake.
        Cas possibles :
        - tabCakes n'est pas en train d'attendre un click, il gère un
          mouvement en cours. Le click est ignoré.
        - aucun cake n'était cliqué -> on sélectionne donc ce cake cliqué
        - un cake était déjà sélectionné mais celui-ci n'est pas son voisin
          on sélectionne alors ce nouveau cake
        - un cake était déjà sélectioné et c'était un voisin -> Enregistrement de ce second click et activation du mode 1
        '''
        if self.__mode != 0:
          return
        if self.__mode == 0:
          if not self.__cake_clicked1:
            self.__cake_clicked1 = cake
            # <prof> il faut agir sur le cake pour changer son aspect
            cake.select()
            return # c'est fini
          if cake.are_neighbours(self.__cake_clicked1):
            self.__cake_clicked2 = cake
            self.clicked -= 1
            cake.select()
            self.go_mode_1()

    def go_mode_0(self):
        '''
        ramène au mode 0
        '''
        self.__cake_clicked1 = None
        self.__cake_clicked2 = None
        self.__mode = 0

    def go_mode_1(self):
        '''
        selon la permutation demandée,
        assigne aux cakes concernés une demande de mouvement
        '''
        # <prof> non non.
        # self.cake_clicked1 et self.cake_clicked2 indiquent seulement
        # quels sont les cakes à permuter.
        # Mais pour le permuter il faut :
        # 1. modifier le tableau self.__cakes
        # 2. assigner cible aux deux cakes (cake.assign_cible)
        # 3. change self.__mode à 1
        # 4. tu peux effectivement mettre __something_done à False maintenant
        line1, col1 = self.getLineColFromCake(self.__cake_clicked1)
        line2, col2 = self.getLineColFromCake(self.__cake_clicked2)
        self.__cakes[line1][col1],self.__cakes[line2][col2] = self.__cakes[line2][col2], self.__cakes[line1][col1]
        self.__last_permutation = ((line1,col1),(line2,col2))
        self.__cake_clicked2.assign_cible(self.__cake_clicked1)
        self.__cake_clicked1.assign_cible(self.__cake_clicked2)
        self.__mode = 1
        self.__something_done = False # pour l'instant rien de fait



    def analyse(self):
        '''
        À faire :
        - Créer un tableau au mêmes dimensions que self.__cakes
          mais qui au lieu de contenir des sprites de gâteaux,
          contient seulement l'id de catégorie de chaque gâteau

        - Faire une analyse des groupes
          -> s'il y a des groupes, les utiliser pour passer en mode 3
        - sinon faire une analyse de chutes (cakes qui doivent tomber)
          -> s'il y a des chutes, passer en mode 4 en précisant quels
          cakes doivent chuter
        - sinon faire une analyse des trous à remplir
          -> s'il y en a, passer en mode 5
        - s'il n'y a rien et que quelque chose a été fait,
          repasser en mode 0
        - et sinon enfin, lancer le mode 6

        '''
        tab  = Analyseur(self.get_analyse_tab())
        groupes = tab.look_for_groups()
        if groupes != [] :
          self.go_mode_3(groupes)
          return
        fall = tab.look_for_falls()
        if fall !=[]:
          self.go_mode_4(fall)
          return
        refill = tab.look_for_refill()
        if refill != [] :
          self.go_mode_5(refill)
          return
        if not self.__something_done:
          self.go_mode_6()
          return
        self.go_mode_0()

    def get_analyse_tab(self):
        tab = []
        for line in self.__cakes:
            tab_line = []
            for cake in line:
                if cake != None:
                    tab_line.append(cake.type)
                else:
                    tab_line.append(None)
            tab.append(tab_line)
        return tab



    def go_mode_3(self, groupes):
        '''
        fait passer en mode 3 et programme la destruction des cakes désignés
        '''
        self.__mode = 3
        self.__something_done = True
        # puisque on fait quelque chose,
        # on peut désélectionner les 2 cakes selected
        # les déséolectionner, et mettre __cake_clicked1 et _cake_clicked2 à None

        self.unselect()
        for list in groupes:
          for line,col in list:
            self.__cakes[line][col].program_destruct()
          #self.__cakes[line][col] = None
        #self.update()

    def unselect(self):
        if self.__cake_clicked1 != None:
            self.__cake_clicked1.unselect()
            self.__cake_clicked1 = None
        if self.__cake_clicked2 != None:
            self.__cake_clicked2.unselect()
            self.__cake_clicked2 = None

    def go_mode_4(self, cakes):
        '''

        fait passer en mode 4 et programme le mouvement vers le bas des cakes désignés
        '''
        self.__something_done = True
        self.__mode = 4

        for line,col, nb_descente in cakes:
          assert self.__cakes[line +nb_descente][col] == None
          self.__cakes[line +nb_descente][col] = self.__cakes[line][col]
          x_destination = self.__cakes[line][col].rect.x
          y_destination = self.__cakes[line][col].rect.y + nb_descente * Cake.CELL_SIZE
          self.__cakes[line+ nb_descente][col].assign_cible_xy(x_destination,y_destination)
          self.__cakes[line][col] = None

    def go_mode_5(self, cells):
        '''
        <Pascal> Je vous ai écrits un pseudo code, c une piste vous pouvez améliorer si vous trouvez
        une méthode qui est mieux
        cells : une liste avec les index des cases à remplir sous forme de tuple (ligne,colonne)
        Vous pourrez utiliser la méthode program_popup dans la classe cake
        Vous pourrez également utiliser la méthode addCake en définnissant la catégorie avant

        fait passer en mode 5 et programme la création des cakes dans les cellules désignées
        '''
        self.__something_done = True
        self.__mode = 5

        for line, col in cells:
          categorie = randrange(Cake.OBJET_MAX)
          self.addCake(line,col,categorie)
          self.__cakes[line][col].program_popup()


    def go_mode_6(self):
       #J'ai fait ce mode et j'ai ajouté une modification de mode pour chaque fonction de mode (Pascal)
        '''
        programme le mouvement inverse à la dernière permutation
        '''
        self.__mode = 6
        self.unselect()
        line1,col1 = self.__last_permutation[0]
        line2,col2 = self.__last_permutation[1]
        self.__cakes[line1][col1],self.__cakes[line2][col2] = self.__cakes[line2][col2], self.__cakes[line1][col1]
        self.__cakes[line2][col2].assign_cible(self.__cakes[line1][col1])
        self.__cakes[line1][col1].assign_cible(self.__cakes[line2][col2])


    def update(self):
        '''
        parcours tous les cakes en leur demandant de changer selon s'ils
        ont un programme en cours (animation, mouvement)
        Si aucun cake n'a un programme en cours (tout terminé)
        on actualise le mode courant :
        - En fin de 1, 3, 4, 5, on déclenche analyse()
        - En fin de 6, on repasse en mode 0
        Quand un cake renvoie 2, il faut kill le cake et mettre None dans
          la case correspondante pour signifier que la case est désormais
          vide
        '''
        ''' pseudo code à traduire
        marqueur : chosesAFaire à False
        pour chaque cake dans self.__cakes faire
            update du cake et noter la valeur renvoyer
            si c'était 1, cela veut juste dire qu'il y avait encore
            des choses à faire -> margueur chosesAFaire passe à True

            si c'était 2, le cake concerné est mort -> cake.kill()
            (penser à mettre à jour le tableau pour mettre None dans
            la case correspondante)

        si chosesAFaire est False -> on peut réfléchir à passer au mode suivant
        '''
        un_cake_a_bougé = False
        for cake in self.__group:
          check = cake.update()
          if check == 1:
            un_cake_a_bougé = True
          elif check == 2:
            ligne, colonne = self.getLineColFromCake(cake)
            self.__cakes[ligne][colonne] = None
            self.score += 100
            cake.kill()
        if un_cake_a_bougé == False:
          if self.__mode >= 1 and self.__mode <= 5:
            self.analyse()
          if self.__mode == 6:
            self.go_mode_0()

    def get_score(self):
      return self.score

    def score_init(self):
        self.score = 0

    def get_clicked(self):
        return self.clicked

    def nb_clicked_init(self):
        self.clicked = self.__maxClicked

