
import math
import random
import pygame
from xd import value

from utiles import mostrar_desde_variable

"""ancho y alto,fps"""
width = 1280
heigth = 720
fps = 60
"""iniciar pantalla"""
pygame.init()
screen = pygame.display.set_mode((width, heigth), pygame.RESIZABLE)
pygame.display.set_caption('')
icon = pygame.Surface((32,32))
pygame.display.set_icon(icon)









class player:
    lista_img = None
    """fps"""
    fps = 60
    """fondo"""
    color_background = (0,128,128)
    """formato de imagen"""
    formato = '.png'
    """directorio"""
    directorio = ''
    """solo si es una superficie"""
    scale_surf = 2
    color_back_surf = (0,128,128)
    """atributos"""
    vida_value = 400
    damage = 5
    recuperacion_vida = 5
    alejamiento = 10
    moverse = {'up':False,'down':False,'left':False,'right':False,'punch':False,'kekkai':False,'shunpo':False,'ki_blast':False}
    posicion = [100,360]
    velocidad = 5
    vel_trasicion_img = 0.15
    indice = 0
    bool_game = True
    num_change = 0
    life_color = (200,0,20)
    life_position = (100,50)
    """background"""
    color_fondo = (255,0,0)
    """punch speed multiplier"""
    punch_speed_multiplier = 3
    """index string"""
    index_string = ['up','down','left','right']
    """max frames y y max index"""
    max_frames = 4
    #max_index =
    """superficies y rects"""
    superficie = [pygame.Surface((40, 60))]
    superficies = superficie * 12
    s_rect = superficie[0].get_rect(center=(posicion[0], posicion[1]))
    """enemigo"""
    enem_class = None
    indice_enem = 0
    """minimap"""
    minimap = None
    """world map"""
    world_map = None
    """menu"""
    menu = None
    """charge screen"""
    charge_screen_class = None
    """ki class"""
    ki_class = None
    """npc class"""
    npc_class = None
    """video class"""
    video_class = None
    """adicional"""
    #clash fist
    clash_fist_bool = True
    #ciclo dia noche
    cont_tiempo = 0
    #punch
    cont_punch = 0
    """add to list"""
    punch = None
    kekkai = None
    """guard"""
    Guard_surface = None
    Guard_bubble_alto = 40
    Guard_bubble_ancho = 40
    """type surface"""
    type_surface = 'surface'
    """transform"""
    list_img_2 = None
    list_img_3 = None
    """Game mode"""
    game_mode = 'rpg'
    """convert to interface"""
    """function extras"""
    function_normal = None
    function_in_menu = None
    function_keyboard = None
    def __init__(self, screen, width,height):
        """asignar"""
        self.screen = screen
        #self.lista_img = lista_img
        self.width = width
        self.height = height
        """verificar lista"""
        self.index = 3
        self.punch_add = 0
        self.kekkai_add = 0
        """utilizar"""


        #def on(self):
        while self.bool_game == True:

            pygame.time.Clock().tick(fps)
            if self.function_normal is not None:
                self.function_normal()
            self.numero_redondeado = round(self.num_change)

            if self.type_surface == 'surface':
                if self.lista_img is not None:
                    self.variables = [self.lista_img[0],self.lista_img[1],self.lista_img[2],self.lista_img[3],
                                      self.punch[0],self.punch[1],self.punch[2],self.punch[3],
                                      self.kekkai[0],self.kekkai[1],self.kekkai[2],self.kekkai[3]]
                    self.img_actual = self.variables[self.indice][self.numero_redondeado]
                    """outline"""
                    self.perfect_outline(self.screen, self.img_actual, self.s_rect, 5, 100)
                    """mostrar"""
                    self.screen.blit(self.img_actual, self.s_rect)

            self.reiniciar()

            if self.moverse['up'] == True:
                self.mover_arriba()
            elif self.moverse['down'] == True:
                self.mover_abajo()
            elif self.moverse['left'] == True:
                self.mover_izquierda()
            elif self.moverse['right'] == True:
                self.mover_derecha()
            elif self.moverse['punch'] == True:
                self.Punch()
            elif self.moverse['shunpo'] == True:
                self.Shunpo(self.moverse['shunpo'],100)
            elif self.moverse['kekkai'] == True:
                self.Kekkai()
                if self.Guard_surface is not None:
                    self.Perfect_guard(self.Guard_surface,120)
            else:
                self.num_change = 0

            """mostrar"""

            self.life_bar(self.vida_value,self.life_color,self.life_position)
            if self.enem_class is not None:
                self.enem_class(self.screen,self.s_rect,self.vida_value)
                self.follow()
                self.damage_func(self.s_rect,self.enem_class.e_rect,self.velocidad)

                if self.clash_fist_bool == True:
                    self.clash_fists(self.moverse['punch'],self.recuperacion_vida,self.alejamiento)
                self.life_bar(self.enem_class.vida, self.enem_class.life_color, self.enem_class.life_position)
            if self.minimap is not None:
                self.create_minimap()
            self.ciclo_dia_noche(1280,1080,0.10)



            if self.menu is not None:
                self.menu(self.screen)
                if self.function_in_menu is not None:
                    self.function_in_menu()
                if self.menu.button_clone_1 is not None:
                    self.add_button()
                self.check_button(self.menu.boton_pos,self.menu.boton_scale)

            """redirect"""
            self.redirect(5,1280,720)
            """usar funciones"""
            self.damage_a_enemy()
            self.Defend_player(self.moverse['kekkai'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if self.function_keyboard is not None:
                        self.function_keyboard(event)
                    if event.key == pygame.K_RIGHT:
                        self.moverse['right'] = True
                    if event.key == pygame.K_LEFT:
                        self.moverse['left'] = True
                    if event.key == pygame.K_UP:
                        self.moverse['up'] = True
                    if event.key == pygame.K_DOWN:
                        self.moverse['down'] = True
                    if event.key == pygame.K_SPACE:
                        self.moverse['shunpo'] = True
                    if event.key == pygame.K_k:
                        self.moverse['ki_blast'] = True
                    if event.key == pygame.K_w:  # arriba
                        self.moverse['up'] = True
                    if event.key == pygame.K_s:  # abajo
                        self.moverse['down'] = True
                    if event.key == pygame.K_d:  # derecha
                        self.moverse['right'] = True
                    if event.key == pygame.K_a:  # izquierda
                        self.moverse['left'] = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        # cont_idle += 1
                        self.moverse['right'] = False
                    if event.key == pygame.K_LEFT:
                        # cont_idle += 1
                        self.moverse['left'] = False
                    if event.key == pygame.K_UP:
                        # cont_idle += 1
                        self.moverse['up'] = False
                    if event.key == pygame.K_DOWN:
                        self.moverse['down'] = False
                    if event.key == pygame.K_SPACE:
                        self.moverse['shunpo'] = False
                    if event.key == pygame.K_k:
                        print('xd')
                        self.moverse['ki_blast'] = False
                    if event.key == pygame.K_w:  # arriba
                        self.moverse['up'] = False
                    if event.key == pygame.K_s:  # abajo
                        self.moverse['down'] = False
                    if event.key == pygame.K_d:  # derecha
                        self.moverse['right'] = False
                    if event.key == pygame.K_a:  # izquierda
                        self.moverse['left'] = False


            if pygame.mouse.get_pressed()[0] == True:
                self.moverse['punch'] = True
            else:
                self.moverse['punch'] = False
            if pygame.mouse.get_pressed()[2] == True:
                self.moverse['punch'] = False
                self.moverse['kekkai'] = True
            else:
                self.moverse['kekkai'] = False
            pygame.display.flip()


    def mover_arriba(self):
        self.indice = 0
        self.num_change += self.vel_trasicion_img
        self.s_rect.y -= self.velocidad

    def mover_abajo(self):
        self.indice = 1
        self.num_change += self.vel_trasicion_img
        self.s_rect.y += self.velocidad

    def mover_izquierda(self):
        self.indice = 2
        self.num_change += self.vel_trasicion_img
        self.s_rect.x -= self.velocidad

    def mover_derecha(self):
        self.indice = 3
        self.num_change += self.vel_trasicion_img
        self.s_rect.x += self.velocidad
    def Punch(self):
        # punch

        self.num_change += self.vel_trasicion_img * self.punch_speed_multiplier



        """up"""
        if self.indice == 0 and self.moverse['punch'] == True:
            self.indice = 4

        """down"""
        if self.indice == 1 and self.moverse['punch'] == True:
            self.indice = 5

        """left"""
        if self.indice == 2 and self.moverse['punch'] == True:
            self.indice = 6

        """right"""
        if self.indice == 3 and self.moverse['punch'] == True:
            self.indice = 7

    def Kekkai(self):

        """guardia"""
        if self.indice == 0 and self.moverse['kekkai'] == True:
            self.indice = 8
        if self.indice == 1 and self.moverse['kekkai'] == True:
            self.indice = 9
        if self.indice == 2 and self.moverse['kekkai'] == True:
            self.indice = 10
        if self.indice == 3 and self.moverse['kekkai'] == True:
            self.indice = 11



    def Shunpo(self, bool_shunpo, distancia):  # tecla espacio
        if bool_shunpo == True and self.indice == 0:
            self.s_rect.y -= distancia
        if bool_shunpo == True and self.indice == 1:
            self.s_rect.y += distancia
        if bool_shunpo == True and self.indice == 2:
            self.s_rect.x -= distancia
        if bool_shunpo == True and self.indice == 3:
            self.s_rect.x += distancia
    def clash_fists(self,bool_punch,cantidad_recuperacion,alejamiento):
        if self.s_rect.x > self.enem_class.e_rect.x and bool_punch == True and self.enem_class.golpeando == True:
            self.vida_value += cantidad_recuperacion
            self.screen.fill((255,255,255))
            self.enem_class.e_rect.x -= alejamiento
        elif self.s_rect.x < self.enem_class.e_rect.x and bool_punch == True and self.enem_class.golpeando == True:
            self.vida_value += cantidad_recuperacion
            self.screen.fill((255,255,255))
            self.enem_class.e_rect.x += alejamiento
        if self.s_rect.y > self.enem_class.e_rect.y and bool_punch == True and self.enem_class.golpeando == True:
            self.vida_value += cantidad_recuperacion
            self.screen.fill((255,255,255))
            self.enem_class.e_rect.y -= alejamiento
        elif self.s_rect.y < self.enem_class.e_rect.y and bool_punch == True and self.enem_class.golpeando == True:
            self.vida_value += cantidad_recuperacion
            self.screen.fill((255,255,255))
            self.enem_class.e_rect.y += alejamiento
    def Perfect_guard(self):
        if self.moverse['kekkai'] == True:
            if self.num_change == self.enem_class.num_change_enem:
                print('perfect')


    def reiniciar(self):
        if self.num_change > self.max_frames:
            self.num_change = 0
        if self.indice > 3:
            if self.num_change > 3:
                self.num_change = 0
        if self.indice > 7:
            if self.num_change > 1:
                self.num_change = 1

        """vida"""
        if self.vida_value < 400:
            self.vida_value += 0.2
        """reinicio punch"""
        if self.moverse['punch'] == False and self.indice == 4:
            self.indice = 0
        if self.moverse['punch'] == False and self.indice == 5:
            self.indice = 1
        if self.moverse['punch'] == False and self.indice == 6:
            self.indice = 2
        if self.moverse['punch'] == False and self.indice == 7:
            self.indice = 3
        """reinicio kekkai"""
        if self.indice == 8 and self.moverse['kekkai'] == False:
            self.indice = 0
        if self.indice == 9 and self.moverse['kekkai'] == False:
            self.indice = 1
        if self.indice == 10 and self.moverse['kekkai'] == False:
            self.indice = 2
        if self.indice == 11 and self.moverse['kekkai'] == False:
            self.indice = 3
    def life_bar(self,vida_value,life_color,life_position):
        life = pygame.Surface((vida_value,vida_value//15))
        life.fill(life_color)
        life_back = pygame.Surface((vida_value + 20,vida_value//10))
        life_back.fill((0,0,0))
        self.screen.blit(life_back,life_position)
        self.screen.blit(life,(life_position[0] + 10,life_position[1] + 10))
    def damage_a_enemy(self):
        if self.moverse['punch'] == True:
            if self.enem_class is not None:
                if self.s_rect.colliderect(self.enem_class.e_rect):
                     self.enem_class.vida -= self.damage
    def Defend_player(self,bool_defend):
        if self.enem_class is not None:
            if bool_defend == True:
                self.enem_class.damage = 0
            else:
                self.enem_class.damage = 5
    def create_minimap(self):
        self.minimap.minimap.fill(self.minimap.color_background)
        self.minimap.point_player.fill(self.minimap.color_player)
        if self.enem_class is not None:
            self.minimap.point_enemy.fill(self.minimap.color_enem)
            self.minimap.minimap.blit(self.minimap.point_enemy,(self.enem_class.e_rect.x // self.minimap.escala,self.enem_class.e_rect.y // self.minimap.escala))
        self.minimap.minimap.blit(self.minimap.point_player,(self.s_rect.x // self.minimap.escala,self.s_rect.y // self.minimap.escala))
        self.screen.blit(self.minimap.minimap,(40,550))
    def redirect(self,velocidad,width,height):
        if self.s_rect.x > width:
            self.s_rect.x -= velocidad
        elif self.s_rect.x < 0:
            self.s_rect.x += velocidad
        if self.s_rect.y > height:
            self.s_rect.y -= velocidad
        elif self.s_rect.y < 0:
            self.s_rect.y += velocidad
        """win or lose"""
        if self.vida_value < 5:
            self.vida_value = 400
            if self.enem_class is not None:
                self.enem_class.vida = 400
            self.s_rect.x = 300
            self.s_rect.y = 500
        if self.enem_class is not None:
            if self.enem_class.vida < 40:
                self.enem_class.vida = 400
                self.vida_value = 400
                self.enem_class.e_rect.x = 600
                self.enem_class.e_rect.y = 500
    def ciclo_dia_noche(self,width,height,vel):
        self.cont_tiempo += vel
        self.oscuridad = pygame.Surface((width,height),pygame.SRCALPHA)
        self.oscuridad.fill((0, 0, 0, self.cont_tiempo))
        self.screen.blit(self.oscuridad, (0, 0))
        if self.cont_tiempo > 100:
            self.cont_tiempo = 0




    def is_surface(self,obj):
        return isinstance(obj, pygame.surface.Surface)

    def is_variable(obj):
        """Retorna True si obj es una variable y False si no lo es."""
        return isinstance(obj, (str, int, float, complex, bool, list, tuple, set, dict))
    """verificar si partes de list_img faltan y desaltivar funciones"""

    #def enemy_damage(self):
    """con la clase del enemigo"""
    def damage_func(self, rect_player, rect_enem, vel):
        bools = [True]
        # print(bools[0])

        if rect_player.colliderect(rect_enem):
            self.enem_class.golpeando = True
        else:
            self.enem_class.golpeando = False
        if rect_player.x < rect_enem.x:
            if rect_player.colliderect(rect_enem):
                bools[0] = True
                # print(bools[0])
                self.enem_class.indice_enem = 6
                self.vida_value -= self.enem_class.damage
                rect_player.x -= vel
            else:
                self.enem_class.indice_enem = 2
        if rect_player.x > rect_enem.x:
            if rect_player.colliderect(rect_enem):
                # print(damage)
                self.enem_class.indice_enem = 7
                self.vida_value -= self.enem_class.damage
                rect_player.x += vel
            else:
                self.enem_class.indice_enem = 3
        if rect_player.y < rect_enem.y:
            if rect_player.colliderect(rect_enem):
                # print(damage)
                """indice punch"""
                self.enem_class.indice_enem = 4
                self.vida_value -= self.enem_class.damage
                rect_player.y -= vel
            else:
                self.enem_class.indice_enem = 0
        if rect_player.y > rect_enem.y:
            if rect_player.colliderect(rect_enem):
                # print(damage)
                self.enem_class.indice_enem = 5
                self.vida_value -= self.enem_class.damage
                rect_player.y += vel
            else:
                self.enem_class.indice_enem = 1
    def reinicio_num_change_e(self):
        if self.enem_class.num_change_enem >= 3:
            self.enem_class.num_change_enem = 0
    def follow(self):
        self.reinicio_num_change_e()
        self.enem_class.vel_transition = round(self.enem_class.vel_float)
        if self.avistamiento(self.enem_class.e_rect, self.s_rect, self.enem_class.distancia):
            self.enem_class.num_change_enem += self.enem_class.vel_transition
            if self.enem_class.e_rect.x > self.s_rect.x:
                self.enem_class.indice_enem = 2
                self.enem_class.e_rect.x -= self.enem_class.vel
                #mov_enem_bool_list[2] = True
            elif self.enem_class.e_rect.x < self.s_rect.x:
                self.enem_class.indice_enem = 3
                self.enem_class.e_rect.x += self.enem_class.vel
                #mov_enem_bool_list[3] = True
            if self.enem_class.e_rect.y > self.s_rect.y:
                self.enem_class.indice_enem = 0
                self.enem_class.e_rect.y -= self.enem_class.vel
                #mov_enem_bool_list[0] = True
            elif self.enem_class.e_rect.y < self.s_rect.y:
                self.enem_class.e_rect.y += self.enem_class.vel
                self.enem_class.indice_enem = 1



    def avistamiento(self,a, b, distancia):
        if (math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))) < distancia:
            return True
        else:
            return False
    """menu"""
    def render_text(self,texto,posicion,escala,color):
        fuente_uni = pygame.font.Font(None, escala)
        mensaje_uni = fuente_uni.render(texto, True, color)
        screen.blit(mensaje_uni, posicion)
    def hover(self,button_pos,button_scale):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > button_pos[0] and mouse_pos[0] < button_pos[0] + button_scale and mouse_pos[1] > button_pos[1] and mouse_pos[1] < button_pos[1] + button_scale:
            return True
        else:
            return False
    def check_button(self,button_pos,button_wid):
        if self.hover(button_pos,button_wid):
            self.menu.color_boton = (255,255,255)
            if pygame.mouse.get_pressed()[0] == True:
                self.menu.color_boton = (0, 255, 0)
                self.menu.active = False
        else:
            self.menu.color_boton = (255, 0, 0)
        if pygame.mouse.get_pressed()[1] == True:
            self.menu.active = True

    def add_button(self):
        self.color_copy = self.menu.button_clone_1['color']
        if self.menu.active == True:
            if 'icon' in self.menu.button_clone_1:
                self.icon = pygame.transform.scale(pygame.image.load(self.menu.button_clone_1['icon']),(self.menu.button_clone_1['scale'],self.menu.button_clone_1['scale']))
            self.boton = pygame.Surface((self.menu.button_clone_1['scale'], self.menu.button_clone_1['scale']))
            self.boton.fill(self.menu.button_clone_1['color'])
            self.screen.blit(self.boton, self.menu.button_clone_1['pos'])
            if 'icon' in self.menu.button_clone_1:
                self.screen.blit(self.icon, self.menu.button_clone_1['pos'])
            if 'text' in self.menu.button_clone_1:
                if 'text_scale' not in self.menu.button_clone_1:
                    self.render_text(self.menu.button_clone_1['text'],self.menu.button_clone_1['pos'],32,(255,255,255))
                elif 'text_scale'  in self.menu.button_clone_1:
                    self.render_text(self.menu.button_clone_1['text'],self.menu.button_clone_1['pos'],self.menu.button_clone_1['text_scale'],(255,255,255))
            if self.hover(self.menu.button_clone_1['pos'],self.menu.button_clone_1['scale']):
                self.menu.button_clone_1['color'] = self.menu.button_clone_1['hover_color']
                if self.moverse['punch'] == True:
                    self.menu.button_clone_1['funtion']()

            else:
                self.menu.button_clone_1['color'] = (255,0,0)



    """aura"""

    def perfect_outline(self,display,img, loc,grosor,transparencia):
        mask = pygame.mask.from_surface(img)
        mask_surf = mask.to_surface()
        mask_surf.set_alpha(transparencia)
        #mask_surf.fill((255, 0, 0))
        mask_surf.set_colorkey((0, 0, 0))

        display.blit(mask_surf, (loc[0] - grosor, loc[1]))
        display.blit(mask_surf, (loc[0] + grosor, loc[1]))
        display.blit(mask_surf, (loc[0], loc[1] - grosor))
        display.blit(mask_surf, (loc[0], loc[1] + grosor))


class Enemy:
    vida = 400
    life_color = (255,255,255)
    life_position = (800,50)
    posicion = (600,600)

    distancia = 200
    """extension"""
    extension = '.png'
    """control frame"""
    indice_enem = 0
    num_change_enem = 1
    vel_float = 0.15
    vel_transition = 0.15
    vel = 3

    """surfs"""
    superficie = [pygame.Surface((40, 70))]
    superficies = superficie * 12
    e_rect = superficie[0].get_rect(center=posicion)
    color_back = (0,128,128)
    damage = 5
    """player"""
    golpeando = False
    list_img = None
    punch = None

    def __init__(self,screen,s_rect,life_player):
        self.screen = screen
        self.life_player = life_player
        self.s_rect = s_rect
        if self.list_img is not None and self.punch is not None:
            #self.variables = [globals()[f"{self.list_img[0]}_{self.num_change_enem}"], globals()[f"{self.list_img[1]}_{self.num_change_enem}"],globals()[f"{self.list_img[2]}_{self.num_change_enem}"], globals()[f"{self.list_img[3]}_{self.num_change_enem}"],globals()[f"{self.punch[0]}{self.num_change_enem}"], globals()[f"{self.punch[1]}{self.num_change_enem}"],globals()[f"{self.punch[2]}{self.num_change_enem}"], globals()[f"{self.punch[3]}{self.num_change_enem}"]]
            self.variables = [self.list_img[0],self.list_img[1],self.list_img[2],self.list_img[3],
                              self.punch[0],self.punch[1],self.punch[2],self.punch[3]]
            self.img_actual =  self.variables[self.indice_enem][round(self.num_change_enem)]
            self.screen.blit(self.img_actual,self.e_rect)

class Minimap:
    escala = 5
    color_background = (255,185,15)
    color_player = (255,0,0)
    color_enem = (0,0,255)
    minimap = pygame.Surface((screen.get_width() // 5, screen.get_height() // 5))
    point_player = pygame.Surface((8, 8))
    point_enemy = pygame.Surface((8, 8))
class Menu:
    image_background = None
    color_background = (0,0,0)
    palabra = 'dbz legacy of battle'
    scala_text = 32
    color_text = (255,255,255)
    bool_palabra = True
    X_text = 0
    Y_text = 0
    """boton"""
    color_boton = (255,0,0)
    boton_scale = 50
    boton_pos = (0,0)
    boton_text = 'New'
    #boton_text_pos = (0,0)
    boton_text_pos = (0,0)
    boton_text_scale = 32
    boton_text_color = (255,255,255)
    """activar o desactivar menu"""
    active = True
    """especial"""
    version_txt = '1.0.0'
    version_pos = (0,500)
    version_scale = 32
    version_color = (255,0,0)
    """button clone"""
    button_clone_1 = None
    button_clone_2 = None
    button_clone_3 = None
    button_clone_4 = None
    button_clone_5 = None

    def __init__(self,screen):
        self.screen = screen
        if self.active == True:
            self.screen.fill(self.color_background)
            if self.image_background is not None:
                self.screen.blit(self.image_background,(0,0))
            self.poner_palabra(self.palabra,(self.X_text,self.Y_text),self.scala_text,self.color_text)
            self.poner_palabra(self.version_txt,self.version_pos,self.version_scale,self.version_color)
            self.Boton()
    def poner_palabra(self,texto,posicion,escala,color):
        if self.bool_palabra == True:
            fuente_uni = pygame.font.Font(None, escala)
            mensaje_uni = fuente_uni.render(texto, True, color)
            screen.blit(mensaje_uni, posicion)
    def Boton(self):
        self.boton = pygame.Surface((self.boton_scale,self.boton_scale))
        self.boton.fill(self.color_boton)
        self.screen.blit(self.boton,self.boton_pos)
        self.poner_palabra(self.boton_text,self.boton_text_pos,self.boton_text_scale,self.boton_text_color)



class Video:
    clip = None
    velocity = 3
    max_time = 10000
    scale = 1
    dimemtions = (1280,720)
    num = 1
    speed_multiplier = 0.73
    extensión = '.jpg'
    """activate"""
    activate = True
    """sound"""
    #sound_video = 'clips/audio/bishoujomom_ghosface.mp3'
    sound_video = None
    if sound_video is not None: #and num > 1:
        sonidito = pygame.mixer.Sound(sound_video)
        sonidito.play()
    """end game wins"""
    game_win_clip = None
    """end game lose"""
    game_lose_clip = None
    def __init__(self,screen):
        self.screen = screen
        self.num_round = round(self.num)
        if self.clip is not None:
            self.mostrar_clip(self.clip)
    def sound(self):
        if self.sound_video is not None and self.num > 1:
            sonidito = pygame.mixer.Sound(self.sound_video)
            sonidito.play()


    def mostrar_clip(self,name):
        if self.activate == True:
            self.vidio = pygame.transform.scale(pygame.image.load(f'{name}{self.num_round}{self.extensión}'),(self.dimemtions[0],self.dimemtions[1]))
            self.screen.blit(self.vidio,(0,0))
#milki_1 = pygame.image.load('')



mp = Minimap
mp.color_background = (255,255,255)
mp.color_player = (0,0,0)
mp.color_enem = (0,255,0)
enem = Enemy
enem.vida = 400
enem.list_img = ['personajes/vegeta/up/up_','personajes/vegeta/down/down_','personajes/vegeta/left/left_','personajes/vegeta/right/right_']
enem.punch = ['personajes/vegeta/punch_right/up/up_','personajes/vegeta/punch_right/down/down_','personajes/vegeta/punch_right/left/left_','personajes/vegeta/punch_right/right/right_']
"""menu"""
def xd():
    print('tu madre')

"""menu"""
img_back = pygame.image.load('tema de menu principal/goku_kaioken vs vegeta.jpg')
new_boton = {'scale':200,'pos':(500,500),'color':(255,0,0),'text':'xd','hover_color':(0,0,255),'funtion':xd,'ico':'1080full-gabi-wolscham.jpg','text_scale':32}

menu = Menu
menu.image_background = img_back
menu.boton_pos = (500,300)
menu.boton_text_pos = (500,300)
menu.boton_scale = 200
menu.version_pos = (0,700)
#menu.button_clone_1 = new_boton

"""npc"""
#npc = NPC
diccionario = {'indice':0}



"""character main"""
def charge_img(name,max,extension,scale):
    lista_imgs = []
    for i in range(1,max):
        lista_imgs.append(pygame.transform.rotozoom(pygame.image.load(f'{name}{i}{extension}').convert(),0,scale))
    return lista_imgs
def save_surf_repeated(amount,surf):
    surfs = []
    for i in range(1,amount+1):
        surfs.append(surf)
    return surfs
scala_random = 2

#spritesheet
#goku
goku_spritesheet = pygame.image.load('movimiento/goku_spritesheet.png').convert_alpha()
goku_ssg_spritesheet = pygame.image.load('movimiento/goku_spritesheet_goku_ssg.png').convert_alpha()
goku_ultrainstinc_spritesheet = pygame.image.load('movimiento/goku_spritesheet_goku_ultra_instinc.png').convert_alpha()
#broly
Broly_spritesheet = pygame.image.load('movimiento/goku_spritesheet.png').convert_alpha()
#vegeta
vegeta_spritesheet = pygame.image.load('personajes/vegeta/75737.png').convert_alpha()
#trunks
trunks_spritesheet = pygame.image.load('personajes/trunks/14504 (1).png').convert_alpha()
#picoro
piccolo_spritesheet = pygame.image.load('personajes/piccoro/14502.png').convert_alpha()
#dante
dante_spritesheet = pygame.image.load('personajes/dante sparda/dante.png').convert_alpha()

list_sprite = [goku_spritesheet,goku_ssg_spritesheet,goku_ultrainstinc_spritesheet,vegeta_spritesheet,
               trunks_spritesheet,piccolo_spritesheet,dante_spritesheet]
index_sprite = 0
index_sprite_enem = 0
spritesheet = list_sprite[index_sprite]


def return_spritesheet(img,loc,dimensions,cantidad_frame,vertical_bool,horizontal_bool,list_bool_flip,scale):
    listi = []
    for i in range(1,cantidad_frame+1):
        listi.append(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(img,(loc[0],loc[1]),(dimensions[0],dimensions[1])),0,scale),list_bool_flip[0],list_bool_flip[1]))
        if horizontal_bool == True:
            loc[0] += dimensions[0]
        if vertical_bool == True:
            loc[1] += dimensions[1]
    return listi
scala_sprites = 1.5
cantidad_de_imgs = 6

#probar
up_sprite_list = [return_spritesheet(list_sprite[i],[1,68],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
prob = [return_spritesheet(list_sprite[i],[18,0],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
left_sprite_list = [return_spritesheet(list_sprite[i],[18,34],(17,34),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
right_sprite_list = [return_spritesheet(list_sprite[i],[18,34],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
#probar punch
list_down_sprite_punch_1 = [return_spritesheet(list_sprite[i],[296,0],(21,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_down_sprite_punch_2 = [return_spritesheet(list_sprite[i],[296,0],(21,34),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_up_sprite_punch_1 = [return_spritesheet(list_sprite[i],[278,66],(21,36),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_up_sprite_punch_2 = [return_spritesheet(list_sprite[i],[278,66],(21,36),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_right_sprite_punch_1 = [return_spritesheet(list_sprite[i],[387,34],(25,35),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_right_sprite_punch_2 = [return_spritesheet(list_sprite[i],[490,34],(25,35),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_left_sprite_punch_1 = [return_spritesheet(list_sprite[i],[387,34],(25,35),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_left_sprite_punch_2 =  [return_spritesheet(list_sprite[i],[490,34],(25,35),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
#probar kekkai
list_kekkai_right_sprite = [return_spritesheet(list_sprite[i],[834,33],(17,35),5,False,False,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_kekkai_left_sprite = [return_spritesheet(list_sprite[i],[834,33],(17,35),5,False,False,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_kekkai_down_sprite = [return_spritesheet(list_sprite[i],[743,3],(17,35),5,False,False,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
list_kekkai_up_sprite = [return_spritesheet(list_sprite[i],[710,68],(17,35),5,False,False,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]

"""goku punch"""
down_sprite_punch_1 = return_spritesheet(spritesheet,[296,0],(21,34),5,False,True,(False,False),scala_sprites)
down_sprite_punch_2 = return_spritesheet(spritesheet,[296,0],(21,34),5,False,True,(True,False),scala_sprites)
up_sprite_punch_1 = return_spritesheet(spritesheet,[278,66],(21,36),5,False,True,(False,False),scala_sprites)
up_sprite_punch_2 = return_spritesheet(spritesheet,[278,66],(21,36),5,False,True,(True,False),scala_sprites)
right_sprite_punch_1 = return_spritesheet(spritesheet,[387,34],(25,35),5,False,True,(False,False),scala_sprites)
right_sprite_punch_2 = return_spritesheet(spritesheet,[490,34],(25,35),5,False,True,(False,False),scala_sprites)
left_sprite_punch_1 = return_spritesheet(spritesheet,[387,34],(25,35),5,False,True,(True,False),scala_sprites)
left_sprite_punch_2 =  return_spritesheet(spritesheet,[490,34],(25,35),5,False,True,(True,False),scala_sprites)
"""kekkai"""
kekkai_right_sprite = return_spritesheet(spritesheet,[834,33],(17,35),5,False,False,(False,False),scala_sprites)
kekkai_left_sprite = return_spritesheet(spritesheet,[834,33],(17,35),5,False,False,(True,False),scala_sprites)
kekkai_down_sprite = return_spritesheet(spritesheet,[743,3],(17,35),5,False,False,(False,False),scala_sprites)
kekkai_up_sprite = return_spritesheet(spritesheet,[710,68],(17,35),5,False,False,(False,False),scala_sprites)

n = 0
m = 0

"""customs"""
index_hair = 1
index_head = 0
hair = [pygame.image.load('custom_sprites/hair sprites/hair_spritesheet.png').convert_alpha(),pygame.image.load('custom_sprites/hair sprites/hair_spritesheet_trunks.png').convert_alpha()]
head = [pygame.image.load('custom_sprites/head sprites/head_spritesheet.png').convert_alpha()]
shadows_sprites = pygame.image.load('custom_sprites/shadows sprites/shadows_sprites.png').convert_alpha()
custom_spritesheet_list = [pygame.image.load('custom_sprites/spritesheet/14502.png').convert_alpha(),pygame.image.load('custom_sprites/spritesheet/75737.png').convert_alpha(),pygame.image.load('custom_sprites/spritesheet/goku_spritesheet.png').convert_alpha()]
index_custom = 2
#custom charge
scala_sprites_custom = 2
hair_goku_up = return_spritesheet(hair[index_hair],[1,68],(17,34),5,False,True,(False,False),scala_sprites_custom)
head_goku_up = return_spritesheet(head[index_head],[1,68],(17,34),5,False,True,(False,False),scala_sprites_custom)
shadows_sprites_up = return_spritesheet(shadows_sprites,[1,68],(17,34),5,False,True,(False,False),scala_sprites_custom)
custom_spritesheet_up = return_spritesheet(custom_spritesheet_list[index_custom],[1,68],(17,34),5,False,True,(False,False),scala_sprites_custom)
def create_character(self,list_img):
    global n,m,spritesheet,index_sprite
    #print(round(self.num_change))
    """if round(self.num_change) > 3:
        self.num_change = 0
    if p1.moverse['up'] == False and p1.moverse['down'] == False and p1.moverse['left'] == False and p1.moverse['right'] == False and p1.moverse['punch'] == False and p1.moverse['kekkai'] == False:
        self.num_change = 0
    img = list_img[self.indice][round(self.num_change)]
    img.set_colorkey(self.color_back_surf)"""
    #screen.blit(img,self.s_rect)

    index_sprite += 1
    if index_sprite > 3:
        index_sprite = 3
    n += 0.1
    if n > 3:
        n = 0
    m += 0.15
    if m > 4:
        m = 0
    screen.blit(down_sprite[round(m)],(200,200))
    screen.blit(up_sprite[round(m)], (290, 200))
    screen.blit(left_sprite[round(m)], (380, 200))
    screen.blit(right_sprite[round(m)], (470, 200))
    screen.blit(down_sprite_punch_1[round(n)], (200, 300))
    screen.blit(down_sprite_punch_2[round(n)], (290, 300))
    screen.blit(up_sprite_punch_1[round(n)], (200, 390))
    screen.blit(up_sprite_punch_2[round(n)], (290, 390))
    screen.blit(left_sprite_punch_1[round(n)], (200, 450))
    screen.blit(right_sprite_punch_2[round(n)], (290, 450))
    #custom
    screen.blit(shadows_sprites_up[round(m)], (780, 200))
    screen.blit(custom_spritesheet_up[round(m)], (780, 200))
    screen.blit(hair_goku_up[round(m)],(780,200))
    screen.blit(head_goku_up[round(m)], (780, 200))

def get_locs(amount,x,y,bool_list_vert_or_hor,dimensions):
    locs = [(x,y)]
    for i in range(1,amount+1):
        if bool_list_vert_or_hor[0] == True and bool_list_vert_or_hor[1] == False:
            y += dimensions[1]
        elif bool_list_vert_or_hor[0] == False and bool_list_vert_or_hor[1] == True:
            x += dimensions[0]
        locs.append((x,y))
    return locs

g = get_locs(3,0,0,(True,False),(20,30))
print(g)

#print(save_surf_repeated(9,pygame.image.load('map_obj/muro_1.png').convert()))


def draw_repeated(list_surf,list_pos):
    for surf,pos in zip(list_surf,list_pos):
        screen.blit(surf,pos)
def collide_for_color(self,color,surface_pos,screen_scale,surface_for_detect,length,dimentions):
    #print(p1.s_rect)
    posicion_de_obtencion_left = (surface_pos[0] - length,surface_pos[1])
    posicion_de_obtencion_right = (surface_pos[0] + dimentions[0] + length,surface_pos[1])
    posicion_de_obtencion_up = (surface_pos[0] + dimentions[0]//2,surface_pos[1] + dimentions[1]//2 - length)
    posicion_de_obtencion_down = (surface_pos[0] + dimentions[0]//2,surface_pos[1] + dimentions[1] + length)
    if hover('u', surface_pos, (0, 0), screen_scale):
        if posicion_de_obtencion_left[0] > 0:
                color_detect_left = surface_for_detect.get_at((posicion_de_obtencion_left))
                if color_detect_left == color:
                    Rect_of_color_left = pygame.Rect(posicion_de_obtencion_left, dimentions)
                    print('detect the colour')
                    """colision personaje"""
                    if surface_pos.colliderect(Rect_of_color_left):
                        surface_pos[0] += self.velocidad*2
        if posicion_de_obtencion_right[0] < 1200:
                color_detect_right = surface_for_detect.get_at((posicion_de_obtencion_right))
                if color_detect_right == color:
                    Rect_of_color_right = pygame.Rect(posicion_de_obtencion_right,dimentions)
                    if surface_pos.colliderect(Rect_of_color_right):
                        surface_pos[0] -= self.velocidad*2
        if posicion_de_obtencion_up[1] > 0:
                color_detect_up = surface_for_detect.get_at((posicion_de_obtencion_up))
                if color_detect_up == color:
                    Rect_of_color_up = pygame.Rect(posicion_de_obtencion_up, dimentions)
                    if surface_pos.colliderect(Rect_of_color_up):
                        surface_pos[1] += self.velocidad*2
        if posicion_de_obtencion_down[1] < 720:
                color_detect_down = surface_for_detect.get_at((posicion_de_obtencion_down))
                if color_detect_down == color:
                    Rect_of_color_down = pygame.Rect(posicion_de_obtencion_down, dimentions)
                    if surface_pos.colliderect(Rect_of_color_down):
                        surface_pos[1] -= self.velocidad*2

def invisible_object(pos,dimentions,surface1,colors_allowed):
    # Obtener información de píxeles de la primera superficie
    pixels_to_draw = []
    for x in range(pos[0],pos[0]+dimentions[0]):
        for y in range(pos[1],pos[1]+dimentions[1]):
            if hover('u',p1.s_rect,(0,0),(1280,720)):
                color = surface1.get_at((x, y))
                if color != (0, 0, 0, 255) and color in colors_allowed:  # Si el píxel no es transparente (negro)
                    pixels_to_draw.append(((x, y), color))
    return pixels_to_draw
def draw_the_surf_in_other(pixels_to_draw,surface2):
    # Dibujar los píxeles en la segunda superficie
    if hover('u', p1.s_rect, (0, 0), (1280, 720)):
        for (x, y), color in pixels_to_draw:
            surface2.set_at((x, y), color)


def get_rect_list(list_surfs,center_list):
    rects = []
    for surfs,center in zip(list_surfs,center_list):
        rects.append(surfs.get_rect(center=center))
    return rects
r = pygame.image.load('map_copy_transparent.png')
t = pygame.image.load('objetos_superpuestos/arbol.png')
def get_color_in_img(img):
    width = img.get_width()
    height = img.get_height()
    colores_unicos = []

    for x in range(width):
        for y in range(height):
            color = img.get_at((x, y))

            # Convertir el color a tupla para comparar
            #color_tupla = (color.r, color.g, color.b, color.a)

            # Si el color no estÃ¡ en la lista, agrÃ©galo
            if color not in colores_unicos:
                colores_unicos.append(color)
    return colores_unicos
print(get_color_in_img(t))
color_permitido = get_color_in_img(t)
def indice_punto_mas_cercano(punto_referencia, lista_puntos):
    indice = min(range(len(lista_puntos)), key=lambda i: (lista_puntos[i][0] - punto_referencia[0])**2 + (lista_puntos[i][1] - punto_referencia[1])**2)
    return indice

# Ejemplo de uso:
punto_referencia = (2, 3)
lista_puntos = [(1, 2), (3, 4), (5, 6)]
indice_cercano = indice_punto_mas_cercano(punto_referencia, lista_puntos)
print("Ãndice del punto mÃ¡s cercano:", indice_cercano)
def create_the_npcs(list_imgs,cantidad,area_pos,area_dimention,vel_tran,vel_move,dimention_surf,max_num_lag,life):
    npcs = {'cantidad':cantidad,'list_img': list_imgs,'rect_list':[],'center_rect':[(0,0)],'vel_transition':vel_tran,'vel_move':vel_move,'life_list':life,'indice':[],'number_change':[],'scale':dimention_surf,'num_lag':0,'max_num_lag':max_num_lag}
    indice_obtencion = 0
    tmp = max(npcs['center_rect'])
    indexi = npcs['center_rect'].index(tmp)
    num_pa_verificar = 0
    for i in range(1,cantidad+1):
        num_pa_verificar += 1
        npcs['center_rect'].append((random.randint(area_pos[0],area_pos[0]+area_dimention[0]),random.randint(area_pos[1],area_pos[1]+area_dimention[1])))

    if num_pa_verificar > 0:
        for i in range(1, cantidad + 1):
            npcs['indice'].append(0)
            npcs['number_change'].append(0)
            indice_obtencion += 1
            npcs['rect_list'].append(pygame.Rect(npcs['center_rect'][indice_obtencion],npcs['scale']))
    return npcs
#print(create_the_npcs(mainer,5,(0,0),(500,670),2,5,(32,32)))
the_npc_0 = create_the_npcs([up_sprite_list[index_sprite_enem],prob[index_sprite_enem],left_sprite_list[index_sprite_enem],right_sprite_list[index_sprite_enem]],5,(0,0),(500,670),2,5,(32,32),40,200)
def move_npc_for_enemy(self,npc_dict,distancia_mostrar):
    #avistamiento para ver
    #print(npc_dict['indice'])
    #print(npc_dict['number_change'])

    indice = indice_punto_mas_cercano(p1.s_rect,npc_dict['rect_list'])
    print(npc_dict['number_change'][indice])
    for pos,index,num_img in zip(npc_dict['rect_list'],npc_dict['indice'],npc_dict['number_change']):


        if avistamiento(self,pos,p1.s_rect,distancia_mostrar):
            #print(npc_dict['list_img'][0][index][num_img])
            screen.blit(npc_dict['list_img'][index][round(num_img)],pos)#
        if avistamiento(self, pos, p1.s_rect, distancia_mostrar//3):
            #num_img += 0.15
            #for y in range(len(npc_dict['number_change'])):
            npc_dict['number_change'][indice] += 0.15
            if npc_dict['number_change'][indice] > 3:
                npc_dict['number_change'][indice] -= 3
            #for x in range(len(npc_dict['indice'])):
            """arriba y abajo"""
            x = indice
            if npc_dict['rect_list'][indice][1] > self.s_rect.y:
                npc_dict['rect_list'][indice][1] -= 3
                if npc_dict['indice'][x] > 0:
                    npc_dict['indice'][x] -= 1
                if npc_dict['indice'][x] < 0:
                    npc_dict['indice'][x] += 1

            elif npc_dict['rect_list'][indice][1] < self.s_rect.y:
                npc_dict['rect_list'][indice][1] += 3
                if npc_dict['indice'][x] > 1:
                    npc_dict['indice'][x] -= 1
                if npc_dict['indice'][x] < 1:
                    npc_dict['indice'][x] += 1
            """left right"""
            if npc_dict['rect_list'][indice][0] > self.s_rect.x:
                npc_dict['rect_list'][indice][0] -= 3
                if npc_dict['indice'][x] > 2:
                    npc_dict['indice'][x] -= 1
                if npc_dict['indice'][x] < 2:
                    npc_dict['indice'][x] += 1
            elif npc_dict['rect_list'][indice][0] < self.s_rect.x:
                npc_dict['rect_list'][indice][0] += 3
                if npc_dict['indice'][x] > 3:
                    npc_dict['indice'][x] -= 1
                if npc_dict['indice'][x] < 3:
                    npc_dict['indice'][x] += 1
        if anti_avistamiento(self,pos, p1.s_rect,20):
            if npc_dict['number_change'][indice] > 0:
                npc_dict['number_change'][indice] -= 1
            if npc_dict['number_change'][indice] < 0:
                npc_dict['number_change'][indice] += 1

    # avistamiento para mover
def move_npc_for_npc(self,npc_dict,distancia_mostrar):
    valor = random.randint(0,4)
    caminar = random.choice([True,False])
    npc_dict['num_lag'] += round(npc_dict['vel_transition'])
    indice = indice_punto_mas_cercano(p1.s_rect, npc_dict['rect_list'])
    for pos,index in zip(npc_dict['rect_list'],npc_dict['indice']):
        if avistamiento(self,pos,p1.s_rect,distancia_mostrar):
            screen.blit(npc_dict['list_img'][index][0],pos)
    if npc_dict['num_lag'] > npc_dict['max_num_lag']:
        if valor == 0:
            npc_dict['indice'][indice] = 0
            if caminar == True:
                npc_dict['rect_list'][indice][1] -= npc_dict['vel_move']
        if valor == 1:
            npc_dict['indice'][indice] = 1
            if caminar == True:
                npc_dict['rect_list'][indice][1] += npc_dict['vel_move']
        if valor == 2:
            npc_dict['indice'][indice] = 2
            if caminar == True:
                npc_dict['rect_list'][indice][0] -= npc_dict['vel_move']
        if valor == 3:
            npc_dict['indice'][indice] = 3
            if caminar == True:
                npc_dict['rect_list'][indice][0] += npc_dict['vel_move']
        npc_dict['num_lag'] = 0
pasos = {'orden_de_los_pasos':[1,4,3,2],'tamaño_de_pasos':200,'up':4}
def create_tracks(dict):
    dict['orden_de_los_pasos'] += 1
def npc_follow(dict):
    print('a')
    #if anti_avistamiento()
"""interactuar"""
def create_text(palabras,max_delay,color_text,scale_text):
    dicti = {'palabras':palabras,'delay':0,'max_delay':max_delay,'color':color_text,'scale':scale_text}
    return dicti
texto_normal = create_text(['Ora','ora'],50,(255,0,0),43)
def hablar(dict,pos_list,personaje_pos):
    indice = indice_punto_mas_cercano(personaje_pos, pos_list)
    rand = random.randint(1,50)
    texto = random.choice(dict['palabras'])
    #if dict['delay'] > dict['max_delay']:
    if rand == 5:
        string_blit(texto,(pos_list[indice][0],pos_list[indice][1] - 40),dict['scale'],dict['color'])
#def destruir()
"""xp"""
def obtener_color(dict,nombre_de_json):
    to_py = f'value = {dict}'
    with open(nombre_de_json, "w") as archivo_jsoni:
        archivo_jsoni.write(to_py)
EXP = {'xp':0,'max_xp':3000,'cantidad':10,'color_xp':(255,0,0),'escala_barra':[5,20],'pos':(20,100)}
objetos_de_obtencion = ['']
Misiones_list = {'kills':0,'kills_vel_xp':0,'recorrido':0,'recorrido_vel_xp':0.1}

#poner en el bucle
obtener_color(EXP,'xd.py')
obtener_color(Misiones_list,'metas_xp.py')
def obtener_metas(rect_enem,life_enem):
    if p1.s_rect.colliderect(rect_enem) and life_enem <= 1:
        Misiones_list['kills'] += 1
    if p1.moverse['up'] == True or p1.moverse['down'] == True or p1.moverse['left'] == True or p1.moverse['right'] == True:
        Misiones_list['recorrido'] += p1.velocidad
def use_xp(screen,Exp_dict):
    if pygame.mouse.get_pressed()[0] == True:
        if Exp_dict['xp'] < Exp_dict['max_xp']:
            Exp_dict['escala_barra'][0] += Exp_dict['cantidad']//10
            Exp_dict['xp'] += Exp_dict['cantidad']
    barra_xp = pygame.Surface((Exp_dict['escala_barra']))
    barra_xp.fill(Exp_dict['color_xp'])
    screen.blit(barra_xp,Exp_dict['pos'])
    string_blit(str(Exp_dict['xp']),Exp_dict['pos'],34,(255,255,255))

def za_warudo():
    #p1.vel_trasicion_img = 0
    #p1.velocidad = 0
    enem.vel_transition = 0
    enem.vel = 0
    enem.num_change_enem = 0
    enem.damage = 0
def cancel():
    p1.vel_trasicion_img = 0.15
    p1.velocidad = 5
    enem.vel_transition = 1
    enem.vel = 3
    enem.num_change_enem = 0
    enem.damage = 5
#def reiniciar(list_a_reiniciar,list_orden_reinicio):

za_warudo_skill = {'img':t,'portada':pygame.image.load('portraits/stands/THE-WORLD_2.png'),'portada_pos':(20,120),'damage':200,'increase':5,'time':300,'max_time':300,'time_pos':[20,200],
                   'vel_charge':1,'delay_damage':300,'function':za_warudo,'bool_atack':False}
crazy_diamond = {'img':t,'portada':pygame.Surface((32,32)),'portada_pos':(20,200),'increase':5,'damage':20,'time':5,'vel_charge':0.1,'delay_damage':5,'function':za_warudo}
def use_skills(pantalla,dict):
    """mostrar"""
    pantalla.blit(dict['portada'], dict['portada_pos'])
    string_blit(str(dict['time']),dict['time_pos'],45,(255,0,0))

    if pygame.mouse.get_pressed()[2] == True:
        dict['bool_atack'] = True
    if dict['bool_atack'] == True:
        dict['damage'] += dict['increase']

        if dict['time'] > 0:
            dict['time'] -= dict['vel_charge']
            dict['function']()
        if dict['delay_damage'] > 0:
            dict['delay_damage'] -= dict['vel_charge']

        pantalla.blit(dict['img'], (0, 0))

    if dict['time'] < 1:
        cancel()
        dict['bool_atack'] = False
    if dict['bool_atack'] == False:
        p1.vida_value -= dict['damage']
        if dict['time'] < dict['max_time']:
            dict['time'] += dict['vel_charge']


tamaño = 1.1
def Aura(list,color,cantidad,transparencia):

    masks = [pygame.mask.from_surface(pygame.transform.rotozoom(list[i],0,tamaño)) for i in range(0, cantidad + 1)]
    #mask = pygame.mask.from_surface(to_kaioken[0][0])
    #new_mask = mask.to_surface()
    new_masks = [masks[i].to_surface() for i in range(0, cantidad + 1)]
    masks_reescale = []
    #new_mask.set_colorkey((0,0,0))
    for i in range(0, cantidad + 1):
        new_masks[i].set_colorkey((0,0,0))
    for i in range(0, cantidad + 1):
        for x in range(list[0].get_width()):
            for y in range(list[0].get_height()):
                if new_masks[i].get_at((x,y)) == (255,255,255):
                    new_masks[i].set_at((x,y),color)
                    masks_reescale.append(new_masks[i])
    for i in range(0, cantidad + 1):
        #new_masks[i].set_alpha(transparencia)
        masks_reescale[i].set_alpha(transparencia)
    return masks_reescale
#to_kaioken = [return_spritesheet(list_sprite[i], [1, 68], (17, 34), 5, False, True, (False, False), scala_sprites) for i in range(0, cantidad_de_imgs + 1)]
alpha_aura = 50
color_aura_move = (255,140,0)
color_aura_punch = (255,99,71)
color_aura_kek = (173,16,16)
aura_ej = Aura(up_sprite_list[index_sprite],color_aura_move,4,alpha_aura)
aura_down = Aura(prob[index_sprite],color_aura_move,4,alpha_aura)
aura_left = Aura(left_sprite_list[index_sprite],color_aura_move,4,alpha_aura)
aura_right = Aura(right_sprite_list[index_sprite],color_aura_move,4,alpha_aura)


aura_punch_up_1 = Aura(up_sprite_punch_1,color_aura_punch,4,50)
aura_punch_down_1 = Aura(down_sprite_punch_1,color_aura_punch,4,50)
aura_punch_left_1 = Aura(left_sprite_punch_1,color_aura_punch,4,50)
aura_punch_right_1 = Aura(right_sprite_punch_1,color_aura_punch,4,50)

aura_punch_up_2 = Aura(up_sprite_punch_2,color_aura_punch,4,50)
aura_punch_down_2 = Aura(down_sprite_punch_2,color_aura_punch,4,50)
aura_punch_left_2 = Aura(left_sprite_punch_2,color_aura_punch,4,50)
aura_punch_right_2 = Aura(right_sprite_punch_2,color_aura_punch,4,50)

aura_kekkai_up = Aura(kekkai_up_sprite,color_aura_kek,4,50)
aura_kekkai_down = Aura(kekkai_down_sprite,color_aura_kek,4,50)
aura_kekkai_left = Aura(kekkai_left_sprite,color_aura_kek,4,50)
aura_kekkai_right = Aura(kekkai_right_sprite,color_aura_kek,4,50)

def perfect_outline(self,display,img, loc,grosor):
    mask = pygame.mask.from_surface(img)
    mask_surf = mask.to_surface()
    mask_surf.set_colorkey((0, 0, 0))
    display.blit(mask_surf, (loc[0] - grosor, loc[1]))
    display.blit(mask_surf, (loc[0] + grosor, loc[1]))
    display.blit(mask_surf, (loc[0], loc[1] - grosor))
    display.blit(mask_surf, (loc[0], loc[1] + grosor))

def blit_aura(display,img,loc,grosor):
    display.blit(img, (loc[0] - grosor, loc[1] - grosor))
    """display.blit(img, (loc[0] - grosor, loc[1]))
    display.blit(img, (loc[0] + grosor, loc[1]))
    display.blit(img, (loc[0], loc[1] - grosor))
    display.blit(img, (loc[0], loc[1] + grosor))"""
"""collision mask"""
def Aura_only(img,color,transparencia):
    mask = pygame.mask.from_surface(img)
    new_mask = mask.to_surface()
    new_mask.set_colorkey((0,0,0))
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            if new_mask.get_at((x,y)) == (255,255,255):
                new_mask.set_at((x,y),color)
    new_mask.set_alpha(transparencia)
    return new_mask
def save_surf_and_pos(surface,x,y,bool_collision_mask):
    surf_and_pos = {'img':surface,'x':x,'y':y,'collision_mask':None,
                    'alpha_img':250,
                    'color_mask':(255,0,0),'alpha_mask':200}
    if bool_collision_mask == True:
        surf_and_pos['collision_mask'] = Aura_only(surface,surf_and_pos['color_mask'],surf_and_pos['alpha_mask'])
    #surf_and_pos = [surface,x,y]
    #if bool_collision_mask == True:
        #surf_and_pos.append(Aura(surface,(255,250,250),200))
    return surf_and_pos
"""video"""
vidio = Video
vidio.clip = 'clips/frames/Video1-Frame'
#vidio.activate = True

"""asignar"""
p1 = player
"""surfaces"""
#move = [up_sprite,down_sprite,left_sprite,right_sprite]#"up"
punch = [up_sprite_punch_1,down_sprite_punch_1,left_sprite_punch_1,right_sprite_punch_1]
kekkai = [kekkai_up_sprite,kekkai_down_sprite,kekkai_left_sprite,kekkai_right_sprite]
"""functions"""

def distancia_plana_simple(pos1,pos2):


    d = math.sqrt((pos1[0] - pos2[0])*2 + (pos1[1] - pos2[1])*2)
    return d


def avistamiento(self, a, b, distancia):
    if (math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))) < distancia:
        return True
    else:
        return False
def anti_avistamiento(self,a, b, distancia):
    if (math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))) > distancia:
        return True
    else:
        return False
def transport(self,pos,to):
    if p1.hover(self,pos,20):
        p1.s_rect.x = to

"""change caracter"""
"""botones"""
ubi_boton_atras = (800,500)
scale_boton = (60,60)
boton_atras = pygame.Surface(scale_boton)
color_boton_atras = (0,0,0)
"""listas"""

#mr satan

"""imagen de seleccion"""
cuadro_selector_p1 = pygame.Surface((100,100))
color_cuadro_selector = (0,0,0)
cuadro_selector_p1_pos = (0,0)
goku_selec = pygame.image.load('portraits/goku.png')
broly_selec = pygame.image.load('portraits/broly.png')
vegeta_selec = pygame.image.load('portraits/vegeta.png')

indice_selector_p1 = 0
indice_selector_p2 = 0
all_selec = [broly_selec,goku_selec,vegeta_selec]
all_selec_pos = [(200,200),(300,200),(400,200)]


"""p1 actual y p2"""
p1_actual = goku_selec
p2_actual = vegeta_selec

"""lugares"""
indice_lugares = 0
lugares = [pygame.image.load('lugares/mini/isla_kame_mini.png').convert(),pygame.image.load('lugares/mini/bosque_mini.png').convert(),pygame.image.load('lugares/mini/grand_kai_tournament_mini.png').convert(),pygame.image.load('lugares/mini/mini_fondo.jpg').convert()]
lugares_pos = [(200,600),(350,600),(500,600),(650,600)]
"""def"""
def seleccion_free_battle(self):
    global indice_lugares
    lugar_actual = lugares[indice_lugares]

    #print(pygame.mouse.get_pos())
    screen.fill((255, 0, 0))
    """mostrar roster"""
    string_blit('p1',(1100,250),45,(255,255,255))
    #screen.blit(p1_actual,(1100,300))
    screen.blit(all_selec[indice_selector_p1],(1100,300))
    string_blit('p2',(1200,250),45,(255,255,255))
    screen.blit(all_selec[indice_selector_p2],(1200,300))
    string_blit('START',(600,400),50,(255,255,255))
    for surf,pos in zip(all_selec,all_selec_pos):
        screen.blit(surf,pos)
    for surf,pos in zip(lugares,lugares_pos):
        screen.blit(surf,pos)
    """mostrar lugar"""
    screen.blit(lugar_actual,(800,600))


def antihover(ancho,alto,pos,surface_pos):
    if surface_pos.x < pos[0] or surface_pos.x > pos[0] + ancho or surface_pos.y < pos[1] or surface_pos.y > pos[1] + alto:
        return True
    else:
        return False
def hover(self,surf_pos,pos,scale):
    if surf_pos[0] > pos[0] and surf_pos[0] < pos[0] + scale[0] and surf_pos[1] > pos[1] and surf_pos[1] < pos[1] + scale[1]:
        return True
    else:
        return False



def puente(self,entrada,door_scale,salida,vel_transition,surf_trans):
    if hover(self,self.s_rect,entrada,door_scale):
        dis = distancia_plana_simple(entrada,salida)
        if avistamiento(self,self.s_rect,salida,dis):
            screen.fill(surf_trans)


def string_blit(text,pos,scale,color):
    fuente_uni = pygame.font.Font(None, scale)
    mensaje_uni = fuente_uni.render(text, True, color)
    screen.blit(mensaje_uni, pos)
indice_west_city = 1
img = ['grand_kai_tournament_2.png','lugares/isla_kame.png']
gta = pygame.image.load(img[0]).convert()
gta2 = pygame.image.load(img[1]).convert()
"""imagenes y colision"""

west_city_principal = pygame.image.load('map.png').convert()
map_copy = pygame.image.load('map_copy.png').convert()
map_copy_alpha = pygame.image.load('map_copy_transparent_2.png').convert_alpha()
colorin_allowed = [(224,96,64),(40,40,40),(248,136,24),(96,56,32),(224,160,64),(200,96,0),(184,104,40),(224,184,64),(248,168,88),(248,208,64),
                   (200,96,64),(96,72,64),(168,32,64),(120,0,56),(120,56,0),(128,104,80),(136,80,40),(200,128,80)]
west_city_x = 0
west_city_y = 0

objetos_de_west_city = [pygame.image.load('map_obj/muro_vertical_1.png').convert(),pygame.image.load('map_obj/muro_vertical_1.png').convert(),pygame.image.load('map_obj/muro_vertical_1.png').convert(),
                        pygame.image.load('map_obj/muro_vertical_1.png').convert()]

point_ini = ((8,200))
objetos_de_west_city_pos = [(8,200),(point_ini[0],objetos_de_west_city[1].get_height()+point_ini[1]),(point_ini[0],objetos_de_west_city[1].get_height()*2+point_ini[1]),
                            (point_ini[0],objetos_de_west_city[1].get_height()*3+point_ini[1]),(point_ini[0],objetos_de_west_city[1].get_height()*4+point_ini[1])]
recto = get_rect_list(objetos_de_west_city,objetos_de_west_city_pos)

"""rect npc"""

"""definir algo"""
p1.punch_speed_multiplier = 5
p1.s_rect.x = 400
p1.s_rect.y = 300
enem.e_rect.x = 800
enem.e_rect.y = 300


map_activates = 'training'
contador_de_salida = 0
#map
mapita = [pygame.image.load('lugares/isla_kame.png').convert(),pygame.image.load('lugares/bosque.png').convert(),pygame.image.load('lugares/grand_kai_tournament_2.png').convert(),pygame.image.load('lugares/fondo.jpg').convert()]
"""portadas"""
portraits = [pygame.image.load('portraits/goku.png').convert(),pygame.image.load('portraits/goku_ssg.png').convert(),
               pygame.image.load('portraits/goku_ui.png').convert(),pygame.image.load('portraits/vegeta.png').convert(),
               pygame.image.load('portraits/trunks.png').convert(),pygame.image.load('portraits/piccoro.png').convert(),
             pygame.image.load('portraits/dante.png').convert()]


portrait_modos = [pygame.image.load('mode_titles/training.png').convert_alpha(),pygame.image.load('mode_titles/History.png').convert_alpha(),pygame.image.load('mode_titles/Tournament.png').convert_alpha(),
                  pygame.image.load('mode_titles/Free-battle.png').convert_alpha()]
ind_mode = 0
modos_string = ['training','history','tournament','free_battle']
"""video"""

def blit_video(screen,dict):
    print(dict['indice'])
    if dict['bool_pause'] == False:
        if dict['indice'] < dict['max_frames']:
            dict['indice'] += dict['vel']
    if dict['indice'] > dict['max_frames']:
        #dict['bool_pause'] = True
        dict['indice'] = 0
    screen.blit(dict['video_frames'][round(dict['indice'])],dict['pos'])
video_ghostface = {'video_frames':charge_img('videos/frames/bishoujo_ghostface/Video1-Frame',20,'.jpg',1.5),'max_frames':5000,
                   'sound':pygame.mixer.music.load('videos/sonido/bishoujo_ghostface.ogg'),'vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_bleach = {'video_frames':charge_img('videos/frames/ichigo vs kenpachi/Video1-Frame',100,'.jpg',0.5),'max_frames':99,
                   'sound':pygame.mixer.music.load('videos/sonido/bishoujo_ghostface.ogg'),'vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_goku_sad = {'video_frames':charge_img('videos/frames/goku sad/Video1-Frame',100,'.jpg',5),'max_frames':90,
                   'sound':pygame.mixer.music.load('videos/sonido/bishoujo_ghostface.ogg'),'vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_saitama_meme = {'video_frames':charge_img('videos/frames/saitama achicado/Video1-Frame',140,'.jpg',0.5),'max_frames':130,
                   'sound':pygame.mixer.music.load('videos/sonido/bishoujo_ghostface.ogg'),'vel':1.5,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_dante_dr_fauss = {'video_frames':charge_img('videos/frames/dante dr_fauss/Video1-Frame',58,'.jpg',0.5),'max_frames':56,
                   'sound':pygame.mixer.music.load('videos/sonido/bishoujo_ghostface.ogg'),'vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
videos = [video_ghostface,video_bleach,video_goku_sad,
          video_saitama_meme,video_dante_dr_fauss]
index_video = 4
vid = videos[index_video]

"""botones"""
#funciones
vel_ind = 0.3
def sumar_indice_lugares():
    global indice_lugares
    if indice_lugares < 3:
        indice_lugares += vel_ind
def restar_indice_lugares():
    global indice_lugares
    if indice_lugares > -1:
        indice_lugares -= vel_ind
def suma_index_sprite():
    global index_sprite
    if index_sprite < 6:
        index_sprite += vel_ind
def resta_index_sprites():
    global index_sprite
    if index_sprite > -1:
        index_sprite -= vel_ind
def resta_index_sprites_enem():
    global index_sprite_enem
    if index_sprite_enem > -1:
        index_sprite_enem -= vel_ind
def suma_index_sprite_enem():
    global index_sprite_enem
    if index_sprite_enem < 6:
        index_sprite_enem += vel_ind

def sum_index_mode():
    global ind_mode
    if ind_mode < 3:
        ind_mode += vel_ind
def res_index_mode():
    global ind_mode
    if ind_mode > -1:
        ind_mode -= vel_ind

def pause_sound_and_video():
    vid['bool_pause'] = True
def despause_sound_and_video():
    vid['bool_pause'] = False
#create
def create_button(screen,dict,bool_active):
    button = pygame.Surface(dict['escala'])
    button.fill(dict['color'])
    screen.blit(button,dict['pos'])
    string_blit(dict['string'],dict['pos'],dict['string_scale'],dict['string_color'])
    if hover('a',pygame.mouse.get_pos(),dict['pos'],dict['escala']):
        if bool_active == True:
            dict['funcion']()
button_sum_lugares = {'escala': (32, 32),'pos':(1100,500), 'color': (240, 240, 240),
                      'string':'+','string_scale':40,'string_color':(255,255,255),
                      'funcion':sumar_indice_lugares}
button_res_lugares = {'escala': (32, 32),'pos':(1000,500), 'color': (240, 240, 240),
                      'string':'-', 'string_scale':40,'string_color':(255,255,255),
                      'funcion':restar_indice_lugares}

button_sum_index_sprite = {'escala': (32, 32),'pos':(100,0), 'color': (255, 0, 0),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':suma_index_sprite}
button_res_index_sprite = {'escala': (32, 32),'pos':(0,0), 'color': (255, 0, 0),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':resta_index_sprites}

button_res_index_sprite_enem = {'escala': (32, 32),'pos':(1140,0), 'color': (255, 0, 0),
                                'string':'-','string_scale':40,'string_color':(255,255,255),
                                'funcion':resta_index_sprites_enem}
button_sum_index_sprite_enem = {'escala': (32, 32),'pos':(1240,0), 'color': (255, 0, 0),
                                'string':'+','string_scale':40,'string_color':(255,255,255),
                                'funcion':suma_index_sprite_enem}

button_sum_index_mode = {'escala': (32, 32),'pos':(720,300), 'color': (255, 0, 0),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':sum_index_mode}
button_res_index_mode = {'escala': (32, 32),'pos':(450,300), 'color': (255, 0, 0),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':res_index_mode}
button_pause = {'escala': (32, 32),'pos':(0,300), 'color': (255, 0, 0),
                           'string':'P','string_scale':40,'string_color':(255,255,255),
                           'funcion':pause_sound_and_video}
button_despause = {'escala': (32, 32),'pos':(0,340), 'color': (255, 0, 0),
                           'string':'D','string_scale':40,'string_color':(255,255,255),
                           'funcion':despause_sound_and_video}
"""fonts"""
def encontrar_posiciones(palabra, lista):
    posiciones = [i for i, elemento in enumerate(lista) if elemento == palabra]
    return posiciones if posiciones else f"La palabra '{palabra}' no se encuentra en la lista."




abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
font_custom = [pygame.image.load('fonts/A-B-C-D-E-F-G-H-I-J-K-L-.png').convert_alpha()]
font_1 = return_spritesheet(font_custom[0],[7,0],(59,60),25,False,True,(False,False),1)
palabra_a = 'v'
palabra_list = ['d','a','n','t','e']
posicion_de_las_letras = get_locs(5,0,0,(False,True),(32,32))
print(posicion_de_las_letras)
posiciones_a = encontrar_posiciones(palabra_a, abc)
posiciones_b = [encontrar_posiciones(palabra_list[i],abc)for i in range(0,4+1)]
def create_text_by_font_img(screen,posiciones,font_imgs,pos_txt,scale_text):
    for ind_pos in posiciones:
        screen.blit(font_imgs[ind_pos],pos_txt)
        #for pos in pos_txt:




def move_map(self):

    global contador_de_salida,indice_west_city,west_city,indice_surfaces,numero_de_cambio,west_city_x,west_city_y,index_sprite,move
    map_activates = modos_string[round(ind_mode)]
    cont_round = round(contador_de_salida)
    """p1"""
    num_aleatorio = random.randint(1,2)
    self.lista_img = [up_sprite_list[round(index_sprite)],prob[round(index_sprite)],left_sprite_list[round(index_sprite)],right_sprite_list[round(index_sprite)]]
    self.punch = [globals()[f'list_up_sprite_punch_{num_aleatorio}'][round(index_sprite)],globals()[f'list_down_sprite_punch_{num_aleatorio}'][round(index_sprite)],globals()[f'list_left_sprite_punch_{num_aleatorio}'][round(index_sprite)],globals()[f'list_right_sprite_punch_{num_aleatorio}'][round(index_sprite)]]
    self.kekkai = [list_kekkai_up_sprite[round(index_sprite)],list_kekkai_down_sprite[round(index_sprite)],list_kekkai_left_sprite[round(index_sprite)],list_kekkai_right_sprite[round(index_sprite)]]
    """enem"""
    enem.list_img = [up_sprite_list[round(index_sprite_enem)],prob[round(index_sprite_enem)],left_sprite_list[round(index_sprite_enem)],right_sprite_list[round(index_sprite_enem)]]
    enem.punch = [globals()[f'up_sprite_punch_{num_aleatorio}'],globals()[f'down_sprite_punch_{num_aleatorio}'],globals()[f'left_sprite_punch_{num_aleatorio}'],globals()[f'right_sprite_punch_{num_aleatorio}']]
    """maps"""
    if map_activates == 'free_battle':
        lugar_actual = mapita[round(indice_lugares)]
        screen.blit(lugar_actual, (0, -200))
        create_button(screen, button_res_lugares, pygame.mouse.get_pressed()[0])
        create_button(screen, button_sum_lugares, pygame.mouse.get_pressed()[0])
        lugari_actual = lugares[round(indice_lugares)]
        """mostrar lugar"""
        screen.blit(lugari_actual, (1020, 600))

    elif map_activates == 'tournament':

        screen.blit(gta,(0,-200))

        """salir del escenario"""
        if antihover(450, 360, (400, 140), p1.s_rect):
            contador_de_salida += 0.3
            string_blit(str(cont_round), (0, 0), 40, (255, 0,0))
        elif antihover(450, 360, (400, 140), enem.e_rect):
            contador_de_salida += 0.3
            string_blit(str(cont_round), (0, 0), 40, (255, 0,0))
        else:
            contador_de_salida = 0
        if contador_de_salida > 10:
            p1.s_rect.x = 400
            p1.s_rect.y = 400
            enem.e_rect.x = 800
            enem.e_rect.y = 400
            contador_de_salida = 0
    elif map_activates == 'history':
        west_city_principal_subsurf = pygame.Surface.subsurface(west_city_principal, (west_city_x, west_city_y),(1280, 720)).convert()
        west_copy_subsurf = pygame.Surface.subsurface(map_copy, (west_city_x, west_city_y),(1280, 720)).convert()
        screen.blit(west_city_principal_subsurf,(0,0))
        """button"""
        create_button(screen, button_sum_index_sprite, pygame.mouse.get_pressed()[0])
        create_button(screen, button_res_index_sprite, pygame.mouse.get_pressed()[0])

        create_button(screen,button_res_index_sprite_enem,pygame.mouse.get_pressed()[0])
        create_button(screen,button_sum_index_sprite_enem,pygame.mouse.get_pressed()[0])


        screen.blit(portraits[round(index_sprite)],(35,0))
        screen.blit(portraits[round(index_sprite_enem)], (1175, 0))

        #create_character(self,mainer)
        use_skills(screen,za_warudo_skill)
        for rect_list in the_npc_0['rect_list']:
            rex = [p1.s_rect,enem.e_rect,rect_list]
            for rects in rex:
                collide_for_color(self,(248,0,0),rects,(1200,600),west_copy_subsurf,1,(32,32))
        #draw_the_surf_in_other(invisible_object(p1.s_rect,(32,32),west_copy_subsurf,color_permitido),map_copy_alpha)
        #move_npc_for_enemy(self,the_npc_0,300)
        move_npc_for_npc(self,the_npc_0,300)
        #create_character(self,mainer)
        #screen.blit(prob[index_sprite][index_sprite],(0,0))
        #move_in_map(self,500,recto,objetos_de_west_city)
        if p1.moverse['up'] == True:
            enem.e_rect.y += p1.velocidad
            if west_city_y > 0:
                west_city_y -= p1.velocidad
        if p1.moverse['down'] == True:
            enem.e_rect.y -= p1.velocidad
            #if west_city_y > 450 and west_city_y < 1630:
                #west_city_y += p1.velocidad*3
            if west_city_y < 1630:
                west_city_y += p1.velocidad
        if p1.moverse['left'] == True:
            if west_city_x > 0:
                west_city_x -= p1.velocidad
        if p1.moverse['right'] == True:
            if west_city_x < 670:
                west_city_x += p1.velocidad
    elif map_activates == 'training':
        p1.vida_value = 300
        enem.vida = 300
        screen.blit(p1_actual,(0,100))
        screen.blit(p2_actual,(1200,100))

    if map_activates != 'training':
        p1.vel_trasicion_img = 0.1

nigga = 0
max_nigga = 4
def change_map(self):
    global map_activates,the_character,indice_lugares,the_enemy,index_skills,index_video,nigga
    map_activates = modos_string[round(ind_mode)]
    rgb = (random.randint(0,250),random.randint(0,250),random.randint(0,250),random.randint(0,250))
    """map copy alpha"""
    if menu.active == False:
        """exp"""
        use_xp(screen,EXP)
        """auras"""
        num_rand = random.randint(1,2)
        auras = [aura_ej, aura_down, aura_left, aura_right,
                 globals()[f'aura_punch_up_{num_rand}'], globals()[f'aura_punch_down_{num_rand}'], globals()[f'aura_punch_left_{num_rand}'], globals()[f'aura_punch_right_{num_rand}'],
                 aura_kekkai_up, aura_kekkai_down, aura_kekkai_left, aura_kekkai_right]
        blit_aura(screen, auras[self.indice][round(self.num_change)], p1.s_rect, tamaño)
        hablar(texto_normal,[enem.e_rect],p1.s_rect)
    if pygame.mouse.get_pressed()[1] == True:
        map_activates = 'training'

    if menu.active == True:
        string_blit(str(map_activates),(900,50),50,rgb)
        screen.blit(portrait_modos[round(ind_mode)],(400,200))
        create_button(screen,button_res_index_mode,pygame.mouse.get_pressed()[0])
        create_button(screen, button_sum_index_mode, pygame.mouse.get_pressed()[0])

        randi = random.randint(0,4)
        if nigga < max_nigga:
            nigga += 0.2
        if nigga > max_nigga:
            nigga = 0
        num_change = round(nigga)
        create_text_by_font_img(screen, posiciones_b[num_change], font_1, posicion_de_las_letras[num_change], 40)

        #video
        #index_video += vel_frame
        #screen.blit(video_1[round(index_video)],(0,0))
        blit_video(screen,vid)
        create_button(screen,button_pause,pygame.mouse.get_pressed()[0])
        create_button(screen, button_despause, pygame.mouse.get_pressed()[0])
p1.function_normal = move_map
p1.function_in_menu = change_map

# p1.type_surface = 'variable'
p1.minimap = mp
p1.enem_class = enem
p1.menu = Menu
"""p1.lista_img = move
p1.punch = punch
p1.kekkai = kekkai"""
#p1.npc_class = npc
#p1.ki_class = Ki
#p1.Guard_surface = pygame.transform.rotozoom(pygame.image.load('bubble.png'),0,0.1)
#p1.Guard_surface.set_colorkey((255,255,255))
#p1.world_map = world
#p1.video_class = vidio
#p1.charge_screen_class = charging_screen
p1(screen,1280,720)
#p1(screen,moverse)
#p1 = player()

