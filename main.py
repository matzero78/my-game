import sys
from time import sleep
import moviepy.editor
import pygame
from bala import Bullet
from enemigo import Enemigo
from enemigo import Obstaculo
from estadisticas import Estadisticas
from personaje import Personaje

#joystick
pygame.joystick.init()
class juego:
    def __init__(self):
        pygame.init()
        self.ancho = 1280
        self.alto = 720
        self.screen = pygame.display.set_mode((self.ancho,self.alto))#poner dentro pa fullscreen (, pygame.FULLSCREEN), pygame.RESIZABLE
        self.fondo = pygame.image.load('assets/background/rojo.jpg').convert()
        self.screen_width = self.screen.get_rect().width
        self.screen_heigth = self.screen.get_rect().height
        pygame.display.set_caption('proyecto 1')
        self.clock = pygame.time.Clock()
        self.icon = pygame.image.load('assets\icono\icono.png')
        self.icon.set_colorkey((248,208,64))
        pygame.display.set_icon(self.icon)
        #self.color = (255,0,0)
        self.color = (4, 0, 0)
        self.contador = 0 #contador
        self.idle = False #idle
        self.velocidad = 1
        self.anchobala = 3
        self.altobala = 15
        self.colorbala =(26,127,239)
        self.personajes_restantes = 3
        self.Obstaculo = Obstaculo(self)
        self.estadisticas = Estadisticas(self)
        self.personaje = Personaje(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()
        self.balas_totales = 15
        #obstaculos
        self.obstaculos = pygame.sprite.Group()

        self.enemigos = pygame.sprite.Group()
        self.velocidad_Enemigo = 1.0
        self.grupo_enemigo = 10
        self.grupo_direccion = 1 # o -1
        pygame.mixer.music.load('assets\musica\main.wav')
        #pygame.mixer.music.play(6)
        pygame.mixer.music.set_volume(0.2)
        self._create_fleet()
        #aderir
        self.obstaculo = pygame.image.load('assets/sprites/Sprite-0001.png')
        self.obs_rect = self.obstaculo.get_rect()
        #booleanito
        self.booleano_de_intro = True
        self.booleano_d_boton = False
        #intro
        self.conta_frame = 0
        self.segs_end = 4
        #self.obstaculos.add(self.obs_rect)
        self.obstaculos.add(self.Obstaculo)
        #experi
        #self.Obstaculo.
        self.Jugar = True
    def correrjuego(self):
        while self.Jugar:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        self.Jugar = False
                    if event.key == pygame.K_RIGHT:
                        self.personaje.mover_derecha = True
                        self.booleano_de_intro = False
                        self.contador = 5
                    if event.key == pygame.K_LEFT:
                        self.personaje.mover_izquierda = True
                        self.booleano_de_intro = False
                        self.contador = 5
                    if event.key == pygame.K_UP:
                        self.personaje.mover_arriba = True
                        self.booleano_de_intro = False
                        self.contador = 5
                    if event.key == pygame.K_DOWN:
                        self.personaje.mover_abajo = True
                        self.booleano_de_intro = False
                        self.contador = 5
                    if event.key == pygame.K_SPACE:
                        self.bullet.fueguito = True
                        self.firebullet()
                        self.contador = 5
                    if event.key == pygame.K_m:
                        self.saltaris = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.personaje.mover_derecha = False
                        self.contador += 1
                    if event.key == pygame.K_LEFT:
                        self.personaje.mover_izquierda = False
                        self.contador += 1
                    if event.key == pygame.K_UP:
                        self.personaje.mover_arriba = False
                        self.contador += 1
                    if event.key == pygame.K_DOWN:
                        self.personaje.mover_abajo = False
                        self.contador += 1
                    if event.key == pygame.K_SPACE:
                        self.bullet.fueguito = False

            self.screen.fill(self.color)
            global camara_x,camara_y
            camara_x = +pygame.mouse.get_pos()[0]
            camara_y = +pygame.mouse.get_pos()[1]
            #self.screen.blit(self.fondo, (camara_x, camara_y))
            colorcito = pygame.image.load('assets/1200px-Color_negro.webp')
            #self.screen.blit(colorcito, (500, 500))
            self.clock.tick(30)
            self.personaje.mover()
            self.personaje.checa_idle()
            self.personaje.checa_paso()
            self.personaje.reinicia_contador()
            self.Obstaculo.poner_fondo_de_pasto()
            self.personaje.poner_pisos()
            self.personaje.hogar()
            self.Obstaculo.poner_obstaculo()

            # colision obs
            #self.personaje.colision_obst()

            #self.personaje.mov_joy()
            self.personaje.corre()
            self.personaje.Barra_vida()
            #self.personaje.aumentar_tamano()
            #self.personaje.camara_centrar()
            self.bullets.update()
            #self.update_enemigo()
            self.obstaculos.update()
            self.colision_horizontal(600,700,400,600,700,500)
            self.colision_vertical(400,500,600,400,500,700)
            #self.colision_obst()
            #self.intro_secundaria()
            #self.Boton()
            self.bullet.golpear()
            #self.personaje.Luffy()



            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                    print(len(self.bullets))

            for bullet in self.bullets.sprites():
                bullet.drawbullet()
            #self.enemigos.draw(self.screen)
            pygame.display.flip()
    def firebullet(self):
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.balas_totales = self.balas_totales - 1

    def _create_fleet(self):
        enemigo = Enemigo(self)
        enemigo_width, enemigo_height = enemigo.rect.size
        availableSpace = self.ancho - (2 * enemigo_width)
        numerodeenemigos = availableSpace // (2 * enemigo_width)
        personaje_height = self.personaje.rect.height
        availableSpacey = self.alto - (3 * enemigo_height) - personaje_height
        numerofilas = availableSpacey // (2 * personaje_height)

        for fila in range(numerofilas):
            for numeroEnemigo in range(numerodeenemigos):
                self.createenemy(numeroEnemigo, fila)


    def createenemy(self, numeroEnemigo, fila):
        enemigo = Enemigo(self)
        enemigo_width, enemigo_height = enemigo.rect.size
        enemigo.x = enemigo_width + 2 * enemigo_width * numeroEnemigo
        enemigo.rect.x = enemigo.x
        enemigo.rect.x = enemigo.rect.height + 2*enemigo.rect.height + fila
        self.enemigos.add(enemigo)
    def update_enemigo(self):
        self.checa_bordesGrupo()
        #self.enemigos.update()
        if not self.enemigos:
            self.bullets.empty()
            self._create_fleet()
        if pygame.sprite.spritecollideany(self.personaje, self.enemigos):
            self.personaje_colisionado()
        #if pygame.sprite.spritecollideany(self.personaje, self.Obstaculo):
            #self.personaje_colisionado()
    def pasar_a_false(self):
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False

    def colision_horizontal (self, puntoA1_x, puntoB1_x, puntoY1, puntoA2_x, puntoB2_x, puntoY2):
        # colisión cabeza
        #puntoA1_x = 600
        #puntoB1_x = 700
        #puntoY1 = 400
        if puntoA1_x < self.personaje.rect.x < puntoB1_x and self.personaje.rect.y < puntoY1 + 5 and self.personaje.rect.y > puntoY1:
            self.personaje.rect.y -= 10
        # colision de culo
        #puntoA2_x = 600
        #puntoB2_x = 700
        #puntoY2 = 500
        if puntoA2_x < self.personaje.rect.x < puntoB2_x and self.personaje.rect.y < puntoY2 + 5 and self.personaje.rect.y > puntoY2 :
            self.personaje.rect.y += 10
    #def colision_obst(self):
        #colision de plataforma
        #if self.personaje.rect.x < self.obs_plataforma_x and self.personaje.rect.y < self.obs_y:


        #if self.personaje.rect.x > self.obs_plataforma_x:

        #if self.personaje.rect.y > self.obs_plataforma_y:

        #if self.personaje.rect.y < self.obs_plataforma_y:
    def colision_vertical(self,puntoA1_Y, puntoB1_Y, puntoX1, puntoA2_Y, puntoB2_Y, puntoX2):
        #400,500,600
        #colision cabeza
        if puntoA1_Y < self.personaje.rect.y < puntoB1_Y and self.personaje.rect.x < puntoX1 + 5 and self.personaje.rect.x > puntoX1:
            self.personaje.rect.x -= 10
        #400, 500, 700
        #colision de culo
        if puntoA2_Y < self.personaje.rect.y < puntoB2_Y and self.personaje.rect.x < puntoX1 + 5 and self.personaje.rect.x > puntoX2:
            self.personaje.rect.x += 10



    def Boton(self):
        self.color_negro = (0,0,0)
        self.contador_de_la_pantalla_d_boton = 0
        if self.booleano_d_boton == True and self.contador_de_la_pantalla_d_boton == 0:
            self.screen.fill(self.color_negro)
        #if self.booleano_d_boton == False:
            #self.contador_de_la_pantalla_d_boton = 1
        self.fuente = pygame.font.Font (None,30)
        self.boton_continuar = pygame.Rect(600, 300, 100, 100)
        self.mensaje = self.fuente.render('continuar',True,(255,255,255))
        pygame.draw.rect(self.screen, (100, 100, 100), self.boton_continuar, 0)
        #self.screen.blit()
        self.screen.blit(self.mensaje, (self.boton_continuar.x +(self.boton_continuar.width - self.mensaje.get_width())/2, self.boton_continuar.y+(self.boton_continuar.height - self.mensaje.get_height())/2))


    def personaje_colisionado(self):
        self.personajes_restantes -= 1

        self.enemigos.empty()
        self.bullets.empty()

        self._create_fleet()
        self.personaje.centrar_personaje()

        sleep(0.5)


    def checa_bordesGrupo(self):
        for enemigo in self.enemigos.sprites():
            if enemigo.checar_bordes():
                self.cambia_direccion()
                break

    def cambia_direccion(self):
        for enemigo in self.enemigos.sprites():
            enemigo.rect.y += self.velocidad_Enemigo
        self.grupo_direccion *= -1


    def intro_secundaria(self):
        self.gojito = pygame.image.load('assets/intro/gojito.gif')
        self.texto_d_presentacion = pygame.image.load('assets/textmark/press-any-key-to-continue.png')
        self.texto_d_presentacion.set_colorkey((255,255,255))
        self.frame = pygame.image.load('assets/intro/1_res.jpg')
        self.frame2 = pygame.image.load('assets/intro/2.jpg')
        self.frame3 = pygame.image.load('assets/intro/3.jpg')
        self.frame4 = pygame.image.load('assets/intro/4.jpg')
        self.frame5 = pygame.image.load('assets/intro/5.jpg')
        self.frame6 = pygame.image.load('assets/intro/6.jpg')
        self.frame7 = pygame.image.load('assets/intro/7.jpg')
        self.frame8 = pygame.image.load('assets/intro/8.jpg')
        self.frame9 = pygame.image.load('assets/intro/9.jpg')
        self.frame10 = pygame.image.load('assets/intro/10.jpg')
        if self.conta_frame == 0 and self.booleano_de_intro == True:
            #print(self.conta_frame)
            #self.conta_frame += 1
            self.screen.blit(self.gojito,(0,0))
            self.screen.blit(self.texto_d_presentacion, (300,500))
        if self.booleano_de_intro == False:
            self.booleano_d_boton = True
            self.Boton()
        if self.personaje.contador_de_intro == 0:
            #print(self.personaje.contador_de_intro)
            self.personaje.contador_de_intro += 1
        if self.personaje.contador_de_intro == 10:
            self.gojito = self.frame
    def intro(self):
        #if self.segs_end == 0:
            #self.segs_end += 1
        if self.segs_end < 3:
            video = moviepy.editor.VideoFileClip("assets/intro/gojito.mp4")
            #video = moviepy.editor.VideoFileClip("assets/zelda botw.mp4")
            #video = moviepy.editor.VideoFileClip("assets/video-luffy-gear-2.mp4")
            video.preview()








if __name__ == "__main__":
    game = juego()
    #game.intro()
    #game.Boton()
    #game.intro_secundaria()
    game.correrjuego()






