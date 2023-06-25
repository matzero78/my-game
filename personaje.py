import pygame
import random
from pygame.sprite import Sprite
import sys
from bala import Bullet
from pygame import joystick
# Configurar el joystick
pygame.joystick.init()
#Joystick = pygame.joystick.Joystick(0)
#Joystick.init()

# Detectar movimiento del joystick
#horizontal_axis = Joystick.get_axis(0)
#vertical_axis = Joystick.get_axis(1)

class Personaje(Sprite):
    def __init__(self, game_game):
        super().__init__()
        self.screen = game_game.screen
        self.screen_rect = game_game.screen.get_rect()
        self.image = pygame.image.load("assets\sprites\quieto\idle_abajo1.png")
        self.width = self.image.get_width()
        self.heigth = self.image.get_height()
        self.resize_image = pygame.transform.scale(self.image, (self.width * 2, self.heigth * 2))
        self.resize_image.set_colorkey((0, 128, 128))
        # imagenes
        self.image_up = pygame.image.load(
            "assets/sprites/caminar/arriba/caminar1.png")  # .set_colorkey((0,128,128))  # .convert()
        self.image_down = pygame.image.load(
            "assets/sprites/caminar/abajo/caminar1.png")  # .set_colorkey((0,128,128))  # .convert()
        self.image_left = pygame.image.load(
            "assets/sprites/caminar/izquierda/caminar1.png")  # .set_colorkey((0,128,128))  # .convert()
        self.image_right = pygame.image.load(
            "assets/sprites/caminar/derecha/caminar1.png")  # .set_colorkey((0,128,128))  # .convert()
        self.current_sprite = self.image_down
        # imagenes2
        self.image_up2 = pygame.image.load("assets/sprites/caminar/arriba/caminar2.png")
        self.image_down2 = pygame.image.load("assets/sprites/caminar/abajo/caminar2.png")
        self.image_left2 = pygame.image.load("assets/sprites/caminar/izquierda/caminar2.png")
        self.image_right2 = pygame.image.load("assets/sprites/caminar/derecha/caminar2.png")
        #imagenes3
        self.image_up3 = pygame.image.load('assets/sprites/caminar/arriba/caminar3.png')
        self.image_down3 = pygame.image.load("assets/sprites/caminar/abajo/caminar3.png")
        self.image_left3 = pygame.image.load("assets/sprites/caminar/izquierda/caminar3.png")
        self.image_right3 = pygame.image.load("assets/sprites/caminar/derecha/caminar3.png")
        # imagenes4
        self.image_up4 = pygame.image.load('assets/sprites/caminar/arriba/caminar4.png')
        self.image_down4 = pygame.image.load("assets/sprites/caminar/abajo/caminar4.png")
        self.image_left4 = pygame.image.load("assets/sprites/caminar/izquierda/caminar4.png")
        self.image_right4 = pygame.image.load("assets/sprites/caminar/derecha/caminar4.png")
        # gif del idle
        self.gif = pygame.image.load('assets/sprites/quieto/idle_abajo1-sheet.gif')
        # idles
        self.idle_arriba = pygame.image.load('assets/sprites/quieto/idle_arriba.png')
        self.idle_abajo = pygame.image.load('assets/sprites/quieto/idle_abajo1.png')
        self.idle_derecha = pygame.image.load('assets/sprites/quieto/idle_derecha1.png')
        self.idle_izquierda = pygame.image.load('assets/sprites/quieto/idle_izquierda1.png')
        #idle abajo resize
        self.width_idle_abajo = self.idle_abajo.get_width()
        self.heigth_idle_abajo = self.idle_abajo.get_height()
        self.idle_abajo_rez = pygame.transform.scale(self.idle_abajo, (self.width_idle_abajo * 2, self.heigth_idle_abajo * 2))
        self.idle_abajo_rez.set_colorkey((0, 128, 128))
        # set_colorkey
        self.image_up.set_colorkey((0, 128, 128))
        self.image_down.set_colorkey((0, 128, 128))
        self.image_left.set_colorkey((0, 128, 128))
        self.image_right.set_colorkey((0, 128, 128))

        self.idle_arriba.set_colorkey((0, 128, 128))
        self.idle_abajo.set_colorkey((0, 128, 128))
        self.idle_derecha.set_colorkey((0, 128, 128))
        self.idle_izquierda.set_colorkey((0, 128, 128))
        # set_colorkey2
        self.image_up2.set_colorkey((0, 128, 128))
        self.image_down2.set_colorkey((0, 128, 128))
        self.image_left2.set_colorkey((0, 128, 128))
        self.image_right2.set_colorkey((0, 128, 128))
        # set_colorkey3
        self.image_up3.set_colorkey((0, 128, 128))
        self.image_down3.set_colorkey((0, 128, 128))
        self.image_left3.set_colorkey((0, 128, 128))
        self.image_right3.set_colorkey((0, 128, 128))
        # set_colorkey4
        self.image_up4.set_colorkey((0, 128, 128))
        self.image_down4.set_colorkey((0, 128, 128))
        self.image_left4.set_colorkey((0, 128, 128))
        self.image_right4.set_colorkey((0, 128, 128))
        #width and heigth de resize image UP
        self.width_up1 = self.image_up.get_width()
        self.heigth_up1 = self.image_up.get_height()
        self.image_up_rez = pygame.transform.scale(self.image_up, (self.width_up1 * 2, self.heigth_up1 * 2))
        self.width_up2 = self.image_up2.get_width()
        self.heigth_up2 = self.image_up2.get_height()
        self.image_up2_rez = pygame.transform.scale(self.image_up2, (self.width_up2 * 2, self.heigth_up2 * 2))
        self.width_up3 = self.image_up3.get_width()
        self.heigth_up3 = self.image_up3.get_height()
        self.image_up3_rez = pygame.transform.scale(self.image_up3, (self.width_up3 * 2, self.heigth_up3 * 2))
        self.width_up4 = self.image_up4.get_width()
        self.heigth_up4 = self.image_up4.get_height()
        self.image_up4_rez = pygame.transform.scale(self.image_up4, (self.width_up4 * 2, self.heigth_up4 * 2))
        # width and heigth de resize image DOWN
        self.width_down1 = self.image_down.get_width()
        self.heigth_down1 = self.image_down.get_height()
        self.image_down_rez = pygame.transform.scale(self.image_down, (self.width_down1 * 2, self.heigth_down1 * 2))
        self.width_down2 = self.image_down2.get_width()
        self.heigth_down2 = self.image_down2.get_height()
        self.image_down2_rez = pygame.transform.scale(self.image_down2, (self.width_down2 * 2, self.heigth_down2 * 2))
        self.width_down3 = self.image_down3.get_width()
        self.heigth_down3 = self.image_down3.get_height()
        self.image_down3_rez = pygame.transform.scale(self.image_down3, (self.width_down3 * 2, self.heigth_down3 * 2))
        self.width_down4 = self.image_down4.get_width()
        self.heigth_down4 = self.image_down4.get_height()
        self.image_down4_rez = pygame.transform.scale(self.image_down4, (self.width_down4 * 2, self.heigth_down4 * 2))
        # width and heigth de resize image right
        self.width_righ1 = self.image_right.get_width()
        self.heigth_righ1 = self.image_right.get_height()
        self.image_right_rez = pygame.transform.scale(self.image_right, (self.width_righ1 * 2, self.heigth_righ1 * 2))
        self.width_righ2 = self.image_right2.get_width()
        self.heigth_righ2 = self.image_right2.get_height()
        self.image_right2_rez = pygame.transform.scale(self.image_right2, (self.width_righ2 * 2, self.heigth_righ2 * 2))
        self.width_righ3 = self.image_right3.get_width()
        self.heigth_righ3 = self.image_right3.get_height()
        self.image_right3_rez = pygame.transform.scale(self.image_right3, (self.width_righ3 * 2, self.heigth_righ3 * 2))
        self.width_righ4 = self.image_right4.get_width()
        self.heigth_righ4 = self.image_right4.get_height()
        self.image_right4_rez = pygame.transform.scale(self.image_right4, (self.width_righ4 * 2, self.heigth_righ4 * 2))
        # width and heigth de resize image left
        self.width_left1 = self.image_left.get_width()
        self.heigth_left1 = self.image_left.get_height()
        self.image_left_rez = pygame.transform.scale(self.image_left, (self.width_left1 * 2, self.heigth_left1 * 2))
        self.width_left2 = self.image_left2.get_width()
        self.heigth_left2 = self.image_left2.get_height()
        self.image_left2_rez = pygame.transform.scale(self.image_left2, (self.width_left2 * 2, self.heigth_left2 * 2))
        self.width_left3 = self.image_left3.get_width()
        self.heigth_left3 = self.image_left3.get_height()
        self.image_left3_rez = pygame.transform.scale(self.image_left3, (self.width_left3 * 2, self.heigth_left3 * 2))
        self.width_left4 = self.image_left4.get_width()
        self.heigth_left4 = self.image_left4.get_height()
        self.image_left4_rez = pygame.transform.scale(self.image_left4, (self.width_left4 * 2, self.heigth_left4 * 2))
        # obstaculos
        self.obstaculo = pygame.image.load('assets/sprites/Sprite-0001.png')
        # axis
        #self.horizontal_axis = joystick.get_axis(0)
        #self.vertical_axis = joystick.get_axis(1)
        # self.rect = self.image.get_rect()
        self.rect = self.resize_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False
        self.saltaris = False
        self.idle = False
        self.contador = 0
        #contador de pasos
        self.conta_pasos_arriba = 0
        self.conta_pasos_abajo = 0
        self.conta_pasos_izquierda = 0
        self.conta_pasos_derecha = 0
        # obtener posicion del obstáculo
        #self.obs_width = self.obstaculo.get_width()
        #self.obs_heigth = self.obstaculo.get_height()
        self.obs_width = 100
        self.obs_heigth = 100
        #coord para personajes
        self.per_cord_x = 500 + 100
        self.per_cord_y = 400 + 200
        #coord de barra de vida
        self.coord_vida_x = 500
        self.coord_vida_y = 800
        # Rect
        self.xante = self.rect.left
        self.yante =  self.rect.top
        self.per_Rect = pygame.Rect(self.per_cord_x, self.per_cord_y, self.width, self.heigth)
        #self.obst = pygame.Rect(self.cord_x, self.cord_y, self.obs_width, self.obs_heigth)
        self.mapas = [
            "XXXXXXXXXXXX",
            "X          X",
            'X XXX  XXX X',
            'X XXXXXX X X',
            'X X X X X XX',]
        #intro secundaria
        self.contador_de_intro = 0
    # >
    def mover(self):
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
            self.resize_image = self.image_right_rez
            self.coord_vida_x += 1
            self.per_cord_x += 1
            self.rect.x += 5
        if self.mover_izquierda and self.rect.left > self.screen_rect.left:
            self.resize_image = self.image_left_rez
            self.coord_vida_x -= 1
            self.per_cord_x -= 1
            self.rect.x -= 5
        if self.mover_arriba and self.rect.top > self.screen_rect.top:
            self.resize_image = self.image_up_rez
            self.coord_vida_y -= 1
            self.per_cord_y -= 1
            self.rect.y -= 5
        if self.mover_abajo and self.rect.bottom < self.screen_rect.bottom:
            self.resize_image = self.image_down_rez
            self.coord_vida_y += 1
            self.per_cord_y += 1
            self.rect.y += 5
    def saltar(self):
        self.imagen_saltar = pygame.image.load('assets/sprites/caminar/salto/abajo.png')
        if self.saltaris == True:
            self.idle_arriba = self.imagen_saltar
            self.rect.y += 5
        if self.saltaris == False:
            self.imagen_saltar = self.resize_image

    def checa_idle(self):
        if self.mover_abajo == False:
            self.contador += 1
        if self.contador == 100:
            self.idle = True
        if self.idle == True:
            self.resize_image = self.idle_abajo_rez
    def checa_paso(self):
        #arriba
        if self.mover_arriba:
            print(self.conta_pasos_arriba)
            self.idle_arriba = self.image_up_rez
            self.conta_pasos_arriba += 30
        #if self.conta_pasos_arriba == 5:
            #self.conta_pasos_arriba += 30
        if self.conta_pasos_arriba == 30:
            self.image_up_rez = self.image_up2_rez
        if self.conta_pasos_arriba == 60:
            self.image_up2_rez = self.image_up3_rez
        if self.conta_pasos_arriba == 90:
            self.image_up3_rez = self.image_up4_rez
        if self.conta_pasos_arriba == 120:
            self.image_up4_rez = self.idle_arriba
        if self.conta_pasos_arriba == 120:
            self.conta_pasos_arriba = 0
        #abajo
        if self.mover_abajo:
            self.conta_pasos_abajo += 30
        #if self.conta_pasos_abajo == 5:
            #self.conta_pasos_abajo += 30
        if self.conta_pasos_abajo == 30:
            self.image_down_rez = self.image_down2_rez
        if self.conta_pasos_abajo == 60:
            self.image_down2_rez = self.image_down3_rez
        if self.conta_pasos_abajo == 90:
            self.image_down3_rez = self.image_down4_rez
        if self.conta_pasos_abajo == 120:
            self.image_down4_rez = self.image_down_rez
        if self.conta_pasos_abajo == 120:
            self.conta_pasos_abajo = 0
        #izquierda
        if self.mover_izquierda:
            self.conta_pasos_izquierda += 30
        if self.conta_pasos_izquierda == 30:
            self.image_left_rez = self.image_left2_rez
        if self.conta_pasos_izquierda == 60:
            self.image_left2_rez = self.image_left3_rez
        if self.conta_pasos_izquierda == 90:
            self.image_left3_rez = self.image_left4_rez
        if self.conta_pasos_izquierda == 120:
            self.image_left4_rez = self.image_left_rez
        if self.conta_pasos_izquierda == 120:
            self.conta_pasos_izquierda = 0
        # izquierda
        if self.mover_derecha:
            self.conta_pasos_derecha += 30
        if self.conta_pasos_derecha == 30:
            self.image_right_rez = self.image_right2_rez
        if self.conta_pasos_derecha == 60:
            self.image_right2_rez = self.image_right3_rez
        if self.conta_pasos_derecha == 90:
            self.image_right3_rez = self.image_right4_rez
        if self.conta_pasos_derecha == 120:
            self.image_right4_rez = self.image_right_rez
        if self.conta_pasos_derecha == 120:
            self.conta_pasos_derecha = 0
    def reinicia_contador(self):
        if self.mover_arriba:
            self.contador = 0
            self.idle = False
        if self.mover_abajo:
            self.contador = 0
            self.idle = False
        if self.mover_derecha:
            self.contador = 0
            self.idle = False
        if self.mover_izquierda:
            self.contador = 0
            self.idle = False


    def mov_joy(self):
        # self.image = current_image
        if self.horizontal_axis < -0.1:
            self.image_left = self.image_left2
            self.rect.x -= 1
        elif self.horizontal_axis > 0.1:
            self.resize_image = self.image_right
            self.rect.x += 1
        elif self.vertical_axis < -0.1:
            self.resize_image = self.image_up
            self.rect.y -= 1
        elif self.vertical_axis > 0.1:
            self.resize_image = self.image_down
            self.rect.y += 1
    def corre(self):
        self.screen.blit(self.resize_image, self.rect)
        print(self.rect.x)
        print(self.rect.y)
    def centrar_personaje(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def Barra_vida(self):
        self.barra_vida = 200
        self.valor_d_life1 = 1
        self.valor_d_life2 = 1
        self.imagen_barra_alt = pygame.image.load('assets/life.png')
        self.imagen_barra = pygame.image.load('assets/images/loading_image.jpg')
        self.imagen_barra.set_colorkey((255,255,255))
        #self.width_barra_vida = self.imagen_barra.get_width()
        #self.heigth_barra_vida = self.imagen_barra.get_height()
        self.width_barra_vida = 100
        self.heigth_barra_vida = 40
        self.imagen_barra_resize = pygame.transform.scale(self.imagen_barra, (self.width_barra_vida * 1, self.heigth_barra_vida * 1))
        if self.valor_d_life1 == 1:
            self.screen.blit(self.imagen_barra_alt, (100,50))
        #self.screen.blit(self.imagen_barra_resize,(self.coord_vida_x,self.coord_vida_y))
        #if self.barra_vida == 190

    def poner_culo(self, Culo, X, Y):
        self.screen.blit(Culo, (X,Y))
    def poner_pisos(self):

        self.piso = pygame.image.load('assets/background/cell arena.png')
        self.piso.set_colorkey((0,255,29))
        self.screen.blit(self.piso, (350,300))
    def hogar(self):
        self.hogares = pygame.image.load('assets/background/casita.png')
        self.screen.blit(self.hogares, (490,330))
    def Luffy(self):

        #arriba
        self.luffy_up = pygame.image.load('assets/sprites/caminar/luffy opcion 2/arriba/luffy 2 opcion-arriba_1.png')
        self.luffy_up2 = pygame.image.load('assets/sprites/caminar/luffy opcion 2/arriba/luffy 2 opcion-arriba_2.png')
        self.luffy_up3 = pygame.image.load('assets/sprites/caminar/luffy opcion 2/arriba/luffy 2 opcion-arriba_3.png')
        #abajo
        self.image_up = self.luffy_up
        self.image_up2 = self.luffy_up2
        self.image_up3 = self.luffy_up3


    #def saitama(self):




    #def enemigo_cell(self):
