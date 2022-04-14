import pygame

class Cake(pygame.sprite.Sprite):
    # <prof> le mieux est encore de placer les constantes dans la classe
    SIZE = 50
    CELL_SIZE = 80
    VELOCITY = 5
    
    """
    COLORS =[
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (50, 50, 50),
        (200, 200, 0),
        (0, 200, 200)
    ]
    """
    OBJET_MAX = 6
    DESTRUCT_FRAMES = 10
    POPUP_FRAMES = 10

    def __init__(self, x, y, cake_type):
        super().__init__()
        
        assert 0 <= cake_type < Cake.OBJET_MAX
        self.image_de_base = pygame.image.load('Illustration{}.png'.format(cake_type+1))
        self.image = pygame.transform.scale(self.image_de_base, (50,50))
        #self.image = pygame.Surface([Cake.SIZE, Cake.SIZE])
        #self.color = Cake.COLORS[cake_type-1]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.blit(self.image_de_base,self.rect)
        #pygame.draw.rect(self.image,(0,0,0),self.rect)
        self.type = cake_type

        self.destruct_count_down = 0
        self.popup_count_down = 0
        self.x_cible = x
        self.y_cible = y

    def unselect(self):
        # <prof> remet en situation normale après sélection
        self.image = pygame.transform.scale(self.image_de_base, (Cake.SIZE,Cake.SIZE))
        self.image.blit(self.image_de_base,self.rect)     

    def select(self):
        # <prof> fonction consistant à mettre le cake en surbrillance
        # quand on le sélectionne
        self.image = pygame.transform.scale(self.image_de_base, (Cake.SIZE+10,Cake.SIZE+10))
        self.image.blit(self.image_de_base,self.rect)
        
    
    def highlight(self):
        # <prof> mise en surbrillance par exemple juste avant de disparaitre
        self.image = pygame.Surface([Cake.SIZE//2 , Cake.SIZE//2])
        self.image.fill(self.color)

    def assign_cible(self, cake):
        '''
        Assigne une cible qui est la position de cake
        '''
        self.x_cible = cake.rect.x
        self.y_cible = cake.rect.y
    
    def assign_cible_xy(self, x ,y):
        '''
        Assigne une cible qui est la position de cake
        '''
        self.x_cible = x
        self.y_cible = y

    def program_destruct(self):
        '''
        programmation d'une animation de destruction
        On peut amorcer un compte à rebours qui consistera à enlever 1
        le temps de la destruction.
        '''
        # modifier l'aspect du sprite (à faire)
        self.destruct_count_down = self.DESTRUCT_FRAMES

    def program_popup(self):
        '''
        programmation d'une animation d'apparition
        On peut amorcer un compte à rebours qui consistera à enlever 1
        le temps de l'apparition.
        '''
        self.popup_count_down = self.POPUP_FRAMES
        # modifier l'apparence du sprite (à faire)

    def are_neighbours(self, otherCake):
        # deux cakes seront voisins si leur distance est = CELL_SIZE
        d = abs(self.rect.x - otherCake.rect.x) + abs(self.rect.y - otherCake.rect.y)
        return d == Cake.CELL_SIZE

    def update(self):
        '''
        Mets à jour en fonction de ce qui est programmé :
        - si la position courante ne correspond pas à x_cible, y_cible
          alors il faut déplacer un peu dans la bonne direction
        - si destruct_count_down est > 0 alors il faut le décrémenter de 1
          et éventuellement (si vous aimez la difficulté, modifier l'image)
        - si popup_count_down est > 0 alors il faut le décrémenter et
          changer l'image
        
        Dans tous les cas :
        - si cake n'a rien de programmé, renvoyer 0
        - si cake a encore quelque chose de programmé et d'inachevé,
          renvoyé 1
        - si cake vien d'achever un descruct_count_down, renvoyer 2
          cet cas particulier permet à tab_cakes de savoir qu'il doit tuer
          le cake et mettre à jour le tableau
        '''
        if self.rect.x > self.x_cible:
          self.rect.x -= Cake.VELOCITY
          return 1
        if self.rect.x < self.x_cible:
          self.rect.x += Cake.VELOCITY
          return 1
        if self.rect.y > self.y_cible:
          self.rect.y -= Cake.VELOCITY
          return 1
        if self.rect.y < self.y_cible:
          self.rect.y += Cake.VELOCITY
          return 1
      
        if self.popup_count_down > 0:
          self.popup_count_down -= 1
          size = Cake.SIZE - self.popup_count_down*2
          self.image = pygame.transform.scale(self.image_de_base, (Cake.SIZE,Cake.SIZE))
          self.image.blit(self.image_de_base,self.rect)
          return 1
        
        if self.destruct_count_down > 0:
          self.destruct_count_down -= 1
          size = Cake.SIZE - self.destruct_count_down*2
          self.image = pygame.transform.scale(self.image_de_base, (Cake.SIZE,Cake.SIZE))
          self.image_de_base = pygame.image.load('Illustration{}.png'.format(self.type+1))
          if self.destruct_count_down > 0:
            return 1
          else:
            return 2
        return 0
        ''' pseudo-code à traduire
        si x > cible_x -> diminuer x de VELOCITE, renvoyer 1
        si x < cible_x -> augmenter x de VELOCITE, renvoyer 1
        idem pour y
        
        si popup_count_down > 0:
            réduire de 1 popup_count_down
            ... changer apparence
            size = dépend de Cake.SIZE et de de count_down
                   il faut que ce soit égale à SIZE quand count_down
                   arrive à 0
            self.image = pygame.Surface([size, size])
            self.color = Cake.COLORS[self.type-1]
            renvoie 1
        
       si destruct_count_down > 0:
            réduire de 1 popup_count_down
            ... changer apparence
            size = dépend de Cake.SIZE et de de count_down
                   il faut que ce soit égale à SIZE quand count_down
                   arrive à 0
            self.image = pygame.Surface([size, size])
            self.color = Cake.COLORS[self.type-1]
            si destrutct_count_down > 0:
               renvoie 1
            sinon:
               renvoie 2      
        '''