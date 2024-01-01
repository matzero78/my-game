

import random
import pygame

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





class charging_screen:
    """tiempo"""
    cont_tiempo = 0
    max_time = 100
    velocity_charge = 1
    """ancho y alto"""
    barra_width = 1
    barra_high = 10
    """bar charge"""
    bar_pos = (0,0)
    barra_de_carga = pygame.Surface((barra_width, barra_high))
    barra_de_carga_back = pygame.Surface((barra_width * 100, barra_high))
    """color"""
    screen_color_background = (255,0,0)
    charge_bar_color = (255,255,255)
    charge_bar_color_back = (0, 0, 0)
    def __init__(self,screen):

        self.screen = screen

        self.screen_bar()
    def screen_bar(self):
        print(self.cont_tiempo)
        self.cont_tiempo += self.velocity_charge
        if self.cont_tiempo < self.max_time:
            self.barra_width += self.velocity_charge
            self.screen.fill(self.screen_color_background)
            self.barra_de_carga.fill(self.charge_bar_color)
            self.barra_de_carga_back.fill(self.charge_bar_color_back)
            self.screen.blit(self.barra_de_carga_back,self.bar_pos)
            self.screen.blit(self.barra_de_carga,self.bar_pos)




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


            #if self.is_surface(lista_img[0]):
            #if self.is_surface(pygame.image.load(f"{lista_img[0]}{self.numero_redondeado}{self.formato}")):
            if self.type_surface == 'surface':
                #self.screen.fill(self.color_background)
                if self.world_map is not None:
                    #self.world_map(self.screen, self.s_rect, self.velocidad * 2)
                    if self.world_map.floor is not None:
                        self.blit_floor()
                        #self.screen.blit(pygame.transform.rotozoom(pygame.image.load('edificio_1.png'),0,2),(0,0))
                if self.lista_img is not None:
                    self.variables = [self.lista_img[0],self.lista_img[1],self.lista_img[2],self.lista_img[3],
                                      self.punch[0],self.punch[1],self.punch[2],self.punch[3],
                                      self.kekkai[0],self.kekkai[1],self.kekkai[2],self.kekkai[3]]


                    print(self.punch_add)
                    self.img_actual = self.variables[self.indice][self.numero_redondeado]
                    print(self.img_actual)
                    print(self.kekkai[0])
                    """outline"""
                    #self.perfect_outline(self.screen,self.img_actual,self.s_rect,1)
                    """mostrar"""
                    self.screen.blit(self.img_actual, self.s_rect)
            elif self.type_surface == 'variable':
                self.variables = [globals()[f"{self.lista_img[0]}{self.numero_redondeado}"], globals()[f"{self.lista_img[1]}{self.numero_redondeado}"],
                                globals()[f"{self.lista_img[2]}{self.numero_redondeado}"], globals()[f"{self.lista_img[3]}{self.numero_redondeado}"]]
                                #"""globals()[f"{self.punch[0]}{self.numero_redondeado}"],
                                #globals()[f"{self.punch[1]}{self.numero_redondeado}"],
                                #globals()[f"{self.punch[2]}{self.numero_redondeado}"],
                                #globals()[f"{self.punch[3]}{self.numero_redondeado}"],
                                #globals()[f"{self.kekkai[0]}"], globals()[f"{self.kekkai[1]}"], globals()[f"{self.kekkai[2]}"], globals()[f"{self.kekkai[3]}"]]"""
                self.img_actual = self.variables[0]
                self.surf = self.superficies[self.indice]
                self.surf.fill(self.color_back_surf)
                mostrar_desde_variable(self.screen, self.surf, self.img_actual, (self.s_rect), self.color_back_surf)

            self.reiniciar()

            #self.img_actual = self.variables[self.indice]



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
            #self.vida_value -= 5
            """mostrar"""
            if self.world_map is not None:
                self.world_map(self.screen,self.s_rect,self.velocidad*2,self.width,self.height)
                if self.world_map.pos_x is not None and self.world_map.pos_y is not None:
                    if self.world_map.collide == False:
                        if self.moverse['left'] == True:
                            if self.enem_class is not None:
                                self.enem_class.e_rect.x += self.velocidad
                            for x in range(len(self.world_map.pos_x)):
                                self.world_map.pos_x[x] += self.velocidad
                        if self.moverse['right'] == True:
                            if self.enem_class is not None:
                                self.enem_class.e_rect.x -= self.velocidad
                            for x in range(len(self.world_map.pos_x)):
                                self.world_map.pos_x[x] -= self.velocidad
                        if self.moverse['up'] == True:
                            if self.enem_class is not None:
                                self.enem_class.e_rect.y += self.velocidad
                            for y in range(len(self.world_map.pos_y)):
                                self.world_map.pos_y[y] += self.velocidad
                        if self.moverse['down'] == True:
                            if self.enem_class is not None:
                                self.enem_class.e_rect.y -= self.velocidad
                            for y in range(len(self.world_map.pos_y)):
                                self.world_map.pos_y[y] -= self.velocidad
            self.life_bar(self.vida_value,self.life_color,self.life_position)
            if self.enem_class is not None:
                self.enem_class(self.screen,self.s_rect,self.vida_value)
                self.follow()
                self.damage_func(self.s_rect,self.enem_class.e_rect,self.velocidad)
                if self.ki_class is not None:
                    self.Explode('e')
                if self.clash_fist_bool == True:
                    self.clash_fists(self.moverse['punch'],self.recuperacion_vida,self.alejamiento)
                self.life_bar(self.enem_class.vida, self.enem_class.life_color, self.enem_class.life_position)
            if self.minimap is not None:
                self.create_minimap()
            self.ciclo_dia_noche(1280,1080,0.10)
            if self.ki_class is not None:
                self.ki_class(self.screen)
                self.ki(self.moverse['ki_blast'])
                self.return_ki_blast_by_punch(self.moverse['ki_blast'])
                self.Explode('p')
                self.return_ki_blast_by_idle(self.moverse['ki_blast'],0,30)
            if self.npc_class is not None:
                self.npc_class(self.screen)
                self.increase_cont()
            if self.charge_screen_class is not None:
                self.charge_screen_class(self.screen)
            if self.menu is not None:
                self.menu(self.screen)
                if self.function_in_menu is not None:
                    self.function_in_menu()
                if self.menu.button_clone_1 is not None:
                    self.add_button()
                self.check_button(self.menu.boton_pos,self.menu.boton_scale)
            if self.video_class is not None:
                self.video_class(self.screen)
                self.increase_frame_video()
            """redirect"""
            self.redirect(5,1280,720)
            """usar funciones"""
            self.damage_a_enemy()
            self.Defend_player(self.moverse['kekkai'])
            #self.screen.blit(self.img_current,)
            #self.screen.blit(self.img_actual,(self.posicion[0],self.posicion[1]))
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
        """orientar hacia enem"""
        """if self.enem_class.indice_enem == 1:
            self.indice = 0
        elif self.enem_class.indice_enem == 0:
            self.indice = 1
        elif self.enem_class.indice_enem == 2:
            self.indice = 3
        elif self.enem_class.indice_enem == 3:
            self.indice = 2"""
        #if self.avistamiento():
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
    def Perfect_guard(self,s,guard_alpha):
        s.set_alpha(guard_alpha)  # alpha level  # this fills the entire surface
        #pygame.draw.circle(s, guard_color, (0, 0), radio)
        self.screen.blit(s,(self.s_rect.x,self.s_rect.y))
        #if self.vida_value < self.vida_value // 10:




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
            if self.s_rect.colliderect(self.enem_class.e_rect):
                 self.enem_class.vida -= self.damage
    def Defend_player(self,bool_defend):
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

    """verificar tipos de superficie"""

    def is_json(self,obj):
        try:
            json.loads(obj)
            return True
        except json.JSONDecodeError:
            return False


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
        if self.enem_class.num_change_enem >= 4:
            self.enem_class.num_change_enem = 1
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
        #self.menu.poner_palabra(self.menu.button_clone_1['text'],self.menu.button_clone_1['pos'],32,(255,0,0))
        #funtion()
    #def reordenar_lista_img(self):
        #if self.index_string
    #def encontrar_caracter(self):
    """ki"""
    def ki(self,bool_ki):
        if bool_ki == True and self.indice == 3:
            self.ki_class.ki_blast_pos.x += self.ki_class.ki_blast_velocity
        if bool_ki == True and self.indice == 2:
            self.ki_class.ki_blast_pos.x -= self.ki_class.ki_blast_velocity
        if bool_ki == True and self.indice == 0:
            self.ki_class.ki_blast_pos.y -= self.ki_class.ki_blast_velocity
        if bool_ki == True and self.indice == 1:
            self.ki_class.ki_blast_pos.y += self.ki_class.ki_blast_velocity

    def return_ki_blast_by_punch(self,bool_punch):
        if bool_punch == True and self.s_rect.x < self.ki_class.ki_blast_pos.x and self.indice == 3:
            if self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode = 0
                self.ki_class.ki_blast_pos.x += self.ki_class.ki_blast_velocity
        if bool_punch == True and self.s_rect.x > self.ki_class.ki_blast_pos.x and self.indice == 2:
            if self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode = 0
                self.ki_class.ki_blast_pos.x -= self.ki_class.ki_blast_velocity
        if bool_punch == True and self.s_rect.y > self.ki_class.ki_blast_pos.y and self.indice == 0:
            if self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode = 0
                self.ki_class.ki_blast_pos.y -= self.ki_class.ki_blast_velocity
        if bool_punch == True and self.s_rect.y < self.ki_class.ki_blast_pos.y and self.indice == 1:
            if self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode = 0
                self.ki_class.ki_blast_pos.y += self.ki_class.ki_blast_velocity
    def Explode(self,objetivo):
        if objetivo == 'p':
            if self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode += self.ki_class.crono_vel
            if self.ki_class.crono_explode > 1 and self.s_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode = 0
                self.vida_value -= self.ki_class.damage
        elif objetivo == 'e':
            if self.enem_class.e_rect.colliderect(self.ki_class.ki_blast_pos):
                self.ki_class.crono_explode += self.ki_class.crono_vel
            if self.ki_class.crono_explode > 0.1 and self.enem_class.e_rect.colliderect(self.ki_class.ki_blast_pos):
                self.enem_class.vida -= self.ki_class.damage
                self.ki_class.crono_explode = 0


    def return_ki_blast_by_idle(self,bool_ki_blast,distancia_de_ancho,distancia_de_alto):
        if bool_ki_blast == False:
            if self.avistamiento(self.ki_class.ki_blast_pos,self.s_rect,self.ki_class.distance):
                """if self.indice =="""
                if self.ki_class.ki_blast_pos.x  > self.s_rect.x + distancia_de_ancho:
                    self.ki_class.ki_blast_pos.x -= self.ki_class.back_vel
                elif self.ki_class.ki_blast_pos.x  < self.s_rect.x - distancia_de_ancho:
                    self.ki_class.ki_blast_pos.x += self.ki_class.back_vel
                if self.ki_class.ki_blast_pos.y  > self.s_rect.y - distancia_de_alto:
                    self.ki_class.ki_blast_pos.y -= self.ki_class.back_vel
                elif self.ki_class.ki_blast_pos.y  < self.s_rect.y + distancia_de_alto:
                    self.ki_class.ki_blast_pos.y += self.ki_class.back_vel
    """viaje"""
    def teleport(self):
        print('xd')
    """npc"""
    def increase_cont(self):
        self.npc_class.contador += 1
        if self.npc_class.contador > self.npc_class.point_change + 5:
            self.npc_class.contador = 0
    """aura"""

    def perfect_outline(self,display,img, loc,grosor):
        mask = pygame.mask.from_surface(img)
        mask_surf = mask.to_surface()
        mask_surf.set_colorkey((0, 0, 0))
        display.blit(mask_surf, (loc[0] - grosor, loc[1]))
        display.blit(mask_surf, (loc[0] + grosor, loc[1]))
        display.blit(mask_surf, (loc[0], loc[1] - grosor))
        display.blit(mask_surf, (loc[0], loc[1] + grosor))
    """video"""
    def increase_frame_video(self):
        if self.video_class.num < self.video_class.max_time and self.video_class.activate == True:
            self.video_class.num += self.video_class.velocity * self.video_class.speed_multiplier
            #self.video_class.activate = True
        else:
            self.video_class.activate = False
    """world map"""
    def blit_floor(self):
        self.screen.blit(self.world_map.floor,(self.world_map.floor_x,self.world_map.floor_y))


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
    vel_float = 1
    vel_transition = 1
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
            self.variables = [f"{self.list_img[0]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.list_img[1]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.list_img[2]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.list_img[3]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.punch[0]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.punch[1]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.punch[2]}{round(self.num_change_enem)}{self.extension}",
                              f"{self.punch[3]}{round(self.num_change_enem)}{self.extension}"]
            self.img_actual = pygame.transform.rotozoom(pygame.image.load(self.variables[self.indice_enem]),0,2)
            self.surf = self.superficies[self.indice_enem]
            self.img_actual.set_colorkey(self.color_back)
            #self.surf.fill(self.color_back)
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

#npc.sprites_list = ['a','a','a','a']
#surfaces

ubi = (random.randint(0,1000),random.randint(0,600))
posiciones = [(random.randint(0,1000),random.randint(0,600)),(random.randint(0,1000),random.randint(0,600)),(random.randint(0,1000),random.randint(0,600))]
"""move npc"""
up_npc = [pygame.image.load('personajes/vegeta/up/up_1.png'),pygame.image.load('personajes/vegeta/up/up_2.png'),pygame.image.load('personajes/vegeta/up/up_3.png'),pygame.image.load('personajes/vegeta/up/up_4.png'),pygame.image.load('personajes/vegeta/up/up_5.png')]
domn_npc = [pygame.image.load('personajes/vegeta/down/down_1.png'),pygame.image.load('personajes/vegeta/down/down_2.png'),pygame.image.load('personajes/vegeta/down/down_3.png'),pygame.image.load('personajes/vegeta/down/down_4.png'),pygame.image.load('personajes/vegeta/down/down_5.png')]
left_npc = [pygame.image.load('personajes/vegeta/left/left_1.png'),pygame.image.load('personajes/vegeta/left/left_2.png'),pygame.image.load('personajes/vegeta/left/left_3.png'),pygame.image.load('personajes/vegeta/left/left_4.png'),pygame.image.load('personajes/vegeta/left/left_5.png'),]
right_npc = [pygame.image.load('personajes/vegeta/right/right_1.png'),pygame.image.load('personajes/vegeta/right/right_2.png'),pygame.image.load('personajes/vegeta/right/right_3.png'),pygame.image.load('personajes/vegeta/right/right_4.png'),pygame.image.load('personajes/vegeta/right/right_5.png'),]

surfaces = [up_npc,domn_npc,left_npc,right_npc]

indice_surfaces = 0
numero_de_cambio = 1
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
tukk = charge_img('movimiento/up/up',6,'.png',scala_random)
tukk_d = charge_img('movimiento/down/down',6,'.png',scala_random)
tukk_l = charge_img('movimiento/left/left',6,'.png',scala_random)
tukk_r = charge_img('movimiento/right/right',6,'.png',scala_random)

tmm = charge_img('movimiento/punch_up/punchup',5,'.png',scala_random)
tmn_d = charge_img('movimiento/punch_down/punchdown',5,'.png',scala_random)
tmn_l = charge_img('movimiento/punch_left/punchleft',5,'.png',scala_random)
tmm_r = charge_img('movimiento/punch_right/punchright',5,'.png',scala_random)

"""kek_up = charge_img('movimiento/kekkai/up',5,'.png',scala_random)
kek_down = charge_img('movimiento/kekkai/down',5,'.png',scala_random)
kek_left = charge_img('movimiento/kekkai/left',5,'.png',scala_random)
kek_right = charge_img('movimiento/kekkai/right',5,'.png',scala_random)"""
#print(tukk)
#main

mainer = [tukk,tukk_d,tukk_l,tukk_r,
          tmm,tmn_d,tmn_l,tmm_r]
          #kek_up,kek_down,kek_left,kek_right]
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
list_sprite = [goku_spritesheet,goku_ssg_spritesheet,goku_ultrainstinc_spritesheet,vegeta_spritesheet,trunks_spritesheet,piccolo_spritesheet]
index_sprite = 0
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
cantidad_de_imgs = 5
"""goku move"""
down_sprite = return_spritesheet(spritesheet,[18,0],(17,34),5,False,True,(False,False),scala_sprites)
right_sprite = return_spritesheet(spritesheet,[18,34],(17,34),5,False,True,(False,False),scala_sprites)
left_sprite = return_spritesheet(spritesheet,[18,34],(17,34),5,False,True,(True,False),scala_sprites)
up_sprite = return_spritesheet(spritesheet,[1,68],(17,34),5,False,True,(False,False),scala_sprites)
#probar
up_sprite_list = [return_spritesheet(list_sprite[i],[1,68],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
prob = [return_spritesheet(list_sprite[i],[18,0],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
left_sprite_list = [return_spritesheet(list_sprite[i],[18,34],(17,34),5,False,True,(True,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
right_sprite_list = [return_spritesheet(list_sprite[i],[18,34],(17,34),5,False,True,(False,False),scala_sprites) for i in range(0,cantidad_de_imgs+1)]
#probar punch

"""goku punch"""
down_sprite_punch = return_spritesheet(spritesheet,[296,0],(21,34),5,False,True,(False,False),scala_sprites)
down_sprite_punch_2 = return_spritesheet(spritesheet,[296,0],(21,34),5,False,True,(True,False),scala_sprites)
up_sprite_punch = return_spritesheet(spritesheet,[278,66],(21,36),5,False,True,(False,False),scala_sprites)
up_sprite_punch_2 = return_spritesheet(spritesheet,[278,66],(21,36),5,False,True,(True,False),scala_sprites)
right_sprite_punch = return_spritesheet(spritesheet,[387,34],(25,35),5,False,True,(False,False),scala_sprites)
right_sprite_punch_2 = return_spritesheet(spritesheet,[490,34],(25,35),5,False,True,(False,False),scala_sprites)
left_sprite_punch = return_spritesheet(spritesheet,[387,34],(25,35),5,False,True,(True,False),scala_sprites)
n = 0
m = 0
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

    """index_sprite += 1
    if index_sprite > 5:
        index_sprite = 0"""
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
    screen.blit(down_sprite_punch[round(n)], (200, 300))
    screen.blit(down_sprite_punch_2[round(n)], (290, 300))
    screen.blit(up_sprite_punch[round(n)], (200, 390))
    screen.blit(up_sprite_punch_2[round(n)], (290, 390))
    screen.blit(left_sprite_punch[round(n)], (200, 450))
    screen.blit(right_sprite_punch_2[round(n)], (290, 450))
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
kekkai_right_sprite = return_spritesheet(spritesheet,[834,33],(17,35),5,False,False,(False,False),scala_sprites)
kekkai_left_sprite = return_spritesheet(spritesheet,[834,33],(17,35),5,False,False,(True,False),scala_sprites)
kekkai_down_sprite = return_spritesheet(spritesheet,[743,3],(17,35),5,False,False,(False,False),scala_sprites)
kekkai_up_sprite = return_spritesheet(spritesheet,[710,6],(17,35),5,False,False,(False,False),scala_sprites)

def draw_repeated(list_surf,list_pos):
    for surf,pos in zip(list_surf,list_pos):
        screen.blit(surf,pos)
def collide_for_color(self,color,surface_for_detect,length,dimentions):
    posicion_de_obtencion_left = (p1.s_rect.x - length,p1.s_rect.y)
    posicion_de_obtencion_right = (p1.s_rect.x + dimentions[0] + length,p1.s_rect.y)
    posicion_de_obtencion_up = (p1.s_rect.x + dimentions[0]//2,p1.s_rect.y + dimentions[1]//2 - length)
    posicion_de_obtencion_down = (p1.s_rect.x + dimentions[0]//2,p1.s_rect.y + dimentions[1] // 2 + length < 0)
    if p1.s_rect.x - length > 0:
        color_detect_left = surface_for_detect.get_at((posicion_de_obtencion_left))
        if color_detect_left == color:
            Rect_of_color_left = pygame.Rect(posicion_de_obtencion_left, dimentions)
            print('detect the colour')
            """colision personaje"""
            if p1.s_rect.colliderect(Rect_of_color_left):
                p1.s_rect.x += self.velocidad*2
    if p1.s_rect.x + dimentions[0] + length < 1200:
        color_detect_right = surface_for_detect.get_at((posicion_de_obtencion_right))
        if color_detect_right == color:
            Rect_of_color_right = pygame.Rect(posicion_de_obtencion_right,dimentions)
            if p1.s_rect.colliderect(Rect_of_color_right):
                p1.s_rect.x -= self.velocidad*2
    if p1.s_rect.y + dimentions[1]//2 - length > 0:
        color_detect_up = surface_for_detect.get_at((posicion_de_obtencion_up))
        if color_detect_up == color:
            Rect_of_color_up = pygame.Rect(posicion_de_obtencion_up, dimentions)
            if p1.s_rect.colliderect(Rect_of_color_up):
                p1.s_rect.y -= self.velocidad*2
    if p1.s_rect.y + dimentions[1] // 2 + length < 720:
        color_detect_down = surface_for_detect.get_at((posicion_de_obtencion_down))
        if color_detect_down == color:
            Rect_of_color_down = pygame.Rect(posicion_de_obtencion_down, dimentions)
            if p1.s_rect.colliderect(Rect_of_color_down):
                p1.s_rect.y += self.velocidad*2

def invisible_object(pos,dimentions,surface1,colors_allowed):
    # Obtener información de píxeles de la primera superficie
    pixels_to_draw = []
    for x in range(pos[0],pos[0]+dimentions[0]):
        for y in range(pos[1],pos[1]+dimentions[1]):
            color = surface1.get_at((x, y))
            if color != (0, 0, 0, 255) and color in colors_allowed:  # Si el píxel no es transparente (negro)
                pixels_to_draw.append(((x, y), color))
    return pixels_to_draw
def draw_the_surf_in_other(pixels_to_draw,surface2):
    # Dibujar los píxeles en la segunda superficie
    for (x, y), color in pixels_to_draw:
        surface2.set_at((x, y), color)


def get_rect_list(list_surfs,center_list):
    rects = []
    for surfs,center in zip(list_surfs,center_list):
        rects.append(surfs.get_rect(center=center))
    return rects
def create_the_npcs(list_imgs,cantidad,area_pos,area_dimention,vel_tran,vel_move,dimention_surf):
    npcs = {'cantidad':cantidad,'list_img': list_imgs,'rect_list':[],'center_rect':[(0,0)],'vel_transition':vel_tran,'vel_move':vel_move,'indice':[],'number_change':[]}
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
            npcs['rect_list'].append(pygame.Rect(npcs['center_rect'][indice_obtencion],dimention_surf))
    return npcs
#print(create_the_npcs(mainer,5,(0,0),(500,670),2,5,(32,32)))
the_npc_0 = create_the_npcs(mainer,5,(0,0),(500,670),2,5,(32,32))
def move_npc_for_enemy(self,npc_dict,distancia_mostrar):
    #avistamiento para ver
    for pos,index,num_img in zip(npc_dict['rect_list'],npc_dict['indice'],npc_dict['number_change']):
        if avistamiento(self,pos,p1.s_rect,distancia_mostrar):
            #print(npc_dict['list_img'][0][index][num_img])
            screen.blit(npc_dict['list_img'][index][num_img],pos)
    # avistamiento para mover
def move_npc_for_npc(self,npc_dict):
    valor = random.randint(0,4)
    """if avistamiento(self)
        if valor == 0:
            npc_dict['indice'] = 0"""


"""video"""
vidio = Video
vidio.clip = 'clips/frames/Video1-Frame'
#vidio.activate = True

"""asignar"""
p1 = player
"""surfaces"""
move = [up_sprite,down_sprite,left_sprite,right_sprite]#"up"
punch = [up_sprite_punch,down_sprite_punch,left_sprite_punch,right_sprite_punch]
kekkai = [kekkai_up_sprite,kekkai_down_sprite,kekkai_left_sprite,kekkai_right_sprite]
"""functions"""
def transcision(self,pos,scale_cubes,color_cubes):
    pygame.Surface((scale_cubes,scale_cubes),pygame.SRCALPHA)
    """fisicas de choque en las paredes"""

    """si esta cerca ir mostrando mas"""
    #if (math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))) < distancia:
    """si esta lejos ir desvaneciendo"""
    #if (math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))) > distancia:

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

all_selec = [broly_selec,goku_selec,vegeta_selec]

all_selec_pos = [(200,200),(300,200),(400,200)]
""""bool seleccion"""
seleccion_player = False
seleccion_enem = False
"""the character """
the_character = 'goku'
the_enemy = 'vegeta'
"""p1 actual y p2"""
p1_actual = goku_selec
p2_actual = vegeta_selec
"""fonts"""
font = pygame.font.Font('freesansbold.ttf',52)
"""lugares"""
indice_lugares = 0
lugares = [pygame.image.load('lugares/mini/isla_kame_mini.png').convert(),pygame.image.load('lugares/mini/bosque_mini.png').convert(),pygame.image.load('lugares/mini/grand_kai_tournament_mini.png').convert(),pygame.image.load('lugares/mini/mini_fondo.jpg').convert()]
lugares_pos = [(200,600),(350,600),(500,600),(650,600)]
"""skills"""
skills_imgs = [pygame.transform.scale(pygame.image.load('skills/portada/kame_hame_ha.jpg').convert(),(200,100)),pygame.image.load('skills/portada/ki_blast.png').convert(),pygame.image.load('skills/portada/genkidama_3.png').convert()]
index_skills = 0
skills_names = ['kame_hame_ha','ki_blast','genki_dama','ssj','kaioken']

#kamehameha
kamehameha_angle = 0
kamehameha_point = ()
kamehameha = [pygame.image.load('skills/kamehameha/kame_hame_ha_1.jpg').convert(),pygame.image.load('skills/kamehameha/kame_hame_ha_2.jpg').convert(),pygame.image.load('skills/kamehameha/kame_hame_ha_3.jpg').convert(),pygame.image.load('skills/kamehameha/kame_hame_ha_4.jpg').convert(),pygame.image.load('skills/kamehameha/kame_hame_ha_5.jpg').convert(),pygame.image.load('skills/kamehameha/kame_hame_ha_6.jpg').convert()]
kamehameha_index = 0

#kiblast
kiblast_angle = 0
kiblast = [pygame.image.load('skills/ki_blast/ki_blast_1.png').convert(),pygame.image.load('skills/ki_blast/ki_blast_2.png').convert(),pygame.image.load('skills/ki_blast/ki_blast_3.png').convert()]
kiblast_index = 0
#genki dama
genki_dama = [pygame.image.load('skills/genkidama/genkidama_1.png').convert(),pygame.image.load('skills/genkidama/genkidama_2.png').convert(),pygame.image.load('skills/genkidama/genkidama_3.png').convert(),pygame.image.load('skills/genkidama/genkidama_4.png').convert(),pygame.image.load('skills/genkidama/genkidama_5.png').convert(),pygame.image.load('skills/genkidama/genkidama_6.png').convert(),pygame.image.load('skills/genkidama/genkidama_7.png').convert(),pygame.image.load('skills/genkidama/genkidama_8.png').convert()]
genki_dama_index = 0
#ssj
ssj_goku_move = []
#kaioken
kaioken_color = ()
#rects
rects = [kamehameha[0].get_rect(),kiblast[0].get_rect(),genki_dama[0].get_rect()]
#colorkey
colorkeys = [(0,0,0),(178,0,255),(0,64,128)]
#contador de movimiento casi inperceptuble
contador_de_movimiento_casi_inperceptible = 0
"""def"""
def seleccion_free_battle(self):
    global indice_lugares
    lugar_actual = lugares[indice_lugares]

    #print(pygame.mouse.get_pos())
    screen.fill((255, 0, 0))
    """mostrar roster"""
    string_blit('p1',(1100,250),45,(255,255,255))
    screen.blit(p1_actual,(1100,300))
    string_blit('p2',(1200,250),45,(255,255,255))
    screen.blit(p2_actual,(1200,300))
    string_blit('START',(600,400),50,(255,255,255))
    for surf,pos in zip(all_selec,all_selec_pos):
        screen.blit(surf,pos)
    for surf,pos in zip(lugares,lugares_pos):
        screen.blit(surf,pos)
    """mostrar lugar"""
    screen.blit(lugar_actual,(800,600))
def cambiar_portada(self):
    global the_character,the_enemy,p1_actual,p2_actual
    """p1"""
    if the_character == 'goku':
        p1_actual = goku_selec
    elif the_character == 'broly':
        p1_actual = broly_selec
    elif the_character == 'vegeta':
        p1_actual = vegeta_selec
    """p2"""
    if the_enemy == 'goku':
        p2_actual = goku_selec
    elif the_enemy == 'broly':
        p2_actual = broly_selec
    elif the_enemy == 'vegeta':
        p2_actual = vegeta_selec



"""other """
#goku
#move
goku_move = ['movimiento/up/up',"movimiento/down/down","movimiento/left/left","movimiento/right/right"]
#punches
kick_left = ['movimiento/kick_up/kick_up_','movimiento/kick_down/kick_down_','movimiento/kick_left/kick_left_','movimiento/kick_right/kick_right_']
kick_right = []
punch_rights = ["movimiento/punch_up/punchup","movimiento/punch_down/punchdown","movimiento/punch_left/punchleft","movimiento/punch_right/punchright"]
punchs_lefts = ['movimiento/punch_up_left/punch_left_up_','movimiento/punch_down_left/punch_left_down_','movimiento/punch_left_left/punch_left_left_','movimiento/punch_right_left/punch_left_right_']
kicks_and_punchs = [punchs_lefts,punch_rights,kick_left]
#kekkai
goku_guard = ['movimiento/kekkai/up','movimiento/kekkai/down','movimiento/kekkai/left','movimiento/kekkai/right']
#launch
goku_launch = ['skills/launch/launch goku/up/up_','skills/launch/launch goku/down/down_','skills/launch/launch goku/left/left_','skills/launch/launch goku/right/right_']
#broly
broly_move = ['personajes/broly/moves/up/up_','personajes/broly/moves/down/down_','personajes/broly/moves/left/left_','personajes/broly/moves/right/right_']
broly_punch = ['personajes/broly/punchs/normal_punchs/up/up_','personajes/broly/punchs/normal_punchs/down/down_','personajes/broly/punchs/normal_punchs/left/left_','personajes/broly/punchs/normal_punchs/right/right_']
broly_guard = ['personajes/broly/guard/up/broly_up_','personajes/broly/guard/down/broly_down_','personajes/broly/guard/left/broly_left_','personajes/broly/guard/right/broly_right_']
#vegeta
vegeta_move = ['personajes/vegeta/up/up_','personajes/vegeta/down/down_','personajes/vegeta/left/left_','personajes/vegeta/right/right_']
vegeta_punch_right = ['personajes/vegeta/punch_right/up/up_','personajes/vegeta/punch_right/down/down_','personajes/vegeta/punch_right/left/left_','personajes/vegeta/punch_right/right/right_']
vegeta_guard = ['personajes/vegeta/guard/up/up_','personajes/vegeta/guard/down/down_','personajes/vegeta/guard/left/left_','personajes/vegeta/guard/right/right_']
def other_punchs_or_kicks(self):

    global punch,move
    punch_random = random.choice(kicks_and_punchs)
    if punch[0] == kick_left[0] and p1.moverse['punch'] == True:
        #p1.s_rect.x = 1000
        p1.damage = 34
        p1.alejamiento = 50
    else:
        p1.damage = 5
        p1.alejamiento = 10
    #print(move)
    if the_character == 'goku':
        p1.punch_speed_multiplier = 3
        p1.color_back_surf = (0, 128,128)
        move[0],move[1],move[2],move[3] = goku_move[0],goku_move[1],goku_move[2],goku_move[3]
        #punch = random.choice(kicks_and_punchs)
        punch[0],punch[1],punch[2],punch[3] = punch_random[0],punch_random[1],punch_random[2],punch_random[3]
        kekkai[0], kekkai[1], kekkai[2], kekkai[3] = goku_guard[0], goku_guard[1], goku_guard[2], goku_guard[3]
    elif the_character == 'broly':
        p1.punch_speed_multiplier = 2
        move[0],move[1],move[2],move[3] = broly_move[0],broly_move[1],broly_move[2],broly_move[3]
        p1.color_back_surf = (0,130,255)
        punch[0],punch[1],punch[2],punch[3] = broly_punch[0],broly_punch[1],broly_punch[2],broly_punch[3]
        kekkai[0],kekkai[1],kekkai[2],kekkai[3] = broly_guard[0],broly_guard[1],broly_guard[2],broly_guard[3]
    elif the_character == 'vegeta':
        p1.punch_speed_multiplier = 3
        p1.color_back_surf = (0, 128, 128)
        move[0], move[1], move[2], move[3] = vegeta_move[0], vegeta_move[1], vegeta_move[2], vegeta_move[3]
        punch[0], punch[1], punch[2], punch[3] = vegeta_punch_right[0], vegeta_punch_right[1], vegeta_punch_right[2], vegeta_punch_right[3]
        kekkai[0], kekkai[1], kekkai[2], kekkai[3] = vegeta_guard[0], vegeta_guard[1], vegeta_guard[2], vegeta_guard[3]
    """the enemy"""
    if the_enemy == 'goku':
        enem.color_back = (0,128,128)
        enem.vel_transition = 0.1
        enem.list_img[0],enem.list_img[1],enem.list_img[2],enem.list_img[3] =  goku_move[0],goku_move[1],goku_move[2],goku_move[3]
        enem.punch[0],enem.punch[1],enem.punch[2],enem.punch[3] = punch_random[0],punch_random[1],punch_random[2],punch_random[3]
    elif the_enemy == 'broly':
        enem.color_back = (0,130,255)
        enem.list_img[0], enem.list_img[1], enem.list_img[2], enem.list_img[3] =  broly_move[0],broly_move[1],broly_move[2],broly_move[3]
        enem.punch[0], enem.punch[1], enem.punch[2], enem.punch[3] =  broly_punch[0],broly_punch[1],broly_punch[2],broly_punch[3]
    elif the_enemy == 'vegeta':
        enem.color_back = (0, 128, 128)
        enem.list_img[0], enem.list_img[1], enem.list_img[2], enem.list_img[3] = vegeta_move[0], vegeta_move[1], vegeta_move[2], vegeta_move[3]
        enem.punch[0], enem.punch[1], enem.punch[2], enem.punch[3] = vegeta_punch_right[0], vegeta_punch_right[1], vegeta_punch_right[2], vegeta_punch_right[3]
"""ki blast"""
barra_de_ki = 200
barra_de_ki_surf = pygame.Surface((barra_de_ki,20))
gastar = 20
ki_blast_surf = pygame.Surface((10,10),pygame.SRCALPHA)
ki_blast_color = (255,185,15,100)
ki_blast_pos = [0,0]
ki_blast_velocity = 5
vel_multi = 1
time_of_ki_blast = 0
ki_blast_bool = False
desviar_hacia_player = False
desviar_hacia_enem = False
def ki_blast(self):
    global ki_blast_bool,barra_de_ki,vel_multi
    golpear_ki_blast = random.choice([True, False])
    ki_blast_surf.fill(ki_blast_color)
    barra_de_ki_surf.fill((255,0,0))
    screen.blit(barra_de_ki_surf,(100,100))
    #if barra_de_ki < 200:
        #barra_de_ki += 0.1
    if hover(self, ki_blast_pos, (enem.e_rect.x, enem.e_rect.y), (100, 100)) or ki_blast_pos[0] == enem.e_rect.x and ki_blast_pos[1] == enem.e_rect.y:
        enem.vida -= 15
        ki_blast_bool = False
    if anti_avistamiento(self,p1.s_rect,enem.e_rect,200):
        screen.blit(ki_blast_surf, (ki_blast_pos[0], ki_blast_pos[1]))
        p1.vel_trasicion_img = 0.0000001


        if p1.moverse['punch'] == True:
            barra_de_ki -= 20
            ki_blast_bool = True
        if ki_blast_bool == True:
            vel_multi += 0.3
            if (math.sqrt(((enem.e_rect.x - ki_blast_pos[0]) ** 2) + ((enem.e_rect.y - ki_blast_pos[1]) ** 2))) < 1000:
                if ki_blast_pos[0] > enem.e_rect.x:
                    ki_blast_pos[0] -= ki_blast_velocity * vel_multi
                elif ki_blast_pos[0] < enem.e_rect.x:
                    ki_blast_pos[0] += ki_blast_velocity*vel_multi
                if ki_blast_pos[1] > enem.e_rect.y:
                    ki_blast_pos[1] -= ki_blast_velocity*vel_multi
                elif ki_blast_pos[1] < enem.e_rect.y:
                    ki_blast_pos[1] += ki_blast_velocity*vel_multi
        if desviar_hacia_player == True:
            if (math.sqrt(((p1.s_rect.x - ki_blast_pos[0]) ** 2) + ((p1.s_rect.y - ki_blast_pos[1]) ** 2))) < 1000:
                if ki_blast_pos[0] > p1.s_rect.x:
                    ki_blast_pos[0] -= ki_blast_velocity
                elif ki_blast_pos[0] < p1.s_rect.x:
                    ki_blast_pos[0] += ki_blast_velocity
                if ki_blast_pos[1] > p1.s_rect.y:
                    ki_blast_pos[1] -= ki_blast_velocity
                elif ki_blast_pos[1] < p1.s_rect.y:
                    ki_blast_pos[1] += ki_blast_velocity
        """desactivar"""
        if ki_blast_bool == False and desviar_hacia_player == False:
            vel_multi = 1
            ki_blast_pos[0] = p1.s_rect.x
            ki_blast_pos[1] = p1.s_rect.y + 5
    else:
        p1.vel_trasicion_img = 0.1


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
map_copy_alpha = pygame.image.load('map_copy_transparent.png').convert()
colorin_allowed = [(224,96,64)]
west_city_x = 0
west_city_y = 0

objetos_de_west_city = [pygame.image.load('map_obj/muro_vertical_1.png').convert(),pygame.image.load('map_obj/muro_vertical_1.png').convert(),pygame.image.load('map_obj/muro_vertical_1.png').convert(),
                        pygame.image.load('map_obj/muro_vertical_1.png').convert()]

point_ini = ((8,200))
objetos_de_west_city_pos = [(8,200),(point_ini[0],objetos_de_west_city[1].get_height()+point_ini[1]),(point_ini[0],objetos_de_west_city[1].get_height()*2+point_ini[1]),
                            (point_ini[0],objetos_de_west_city[1].get_height()*3+point_ini[1]),(point_ini[0],objetos_de_west_city[1].get_height()*4+point_ini[1])]
recto = get_rect_list(objetos_de_west_city,objetos_de_west_city_pos)


"""definir algo"""
p1.punch_speed_multiplier = 5
p1.s_rect.x = 400
p1.s_rect.y = 300
enem.e_rect.x = 800
enem.e_rect.y = 300
#map_activates = 'tournament'
map_activates = 'training'
contador_de_salida = 0
#map
mapita = [pygame.image.load('lugares/isla_kame.png').convert(),pygame.image.load('lugares/bosque.png').convert(),pygame.image.load('lugares/grand_kai_tournament_2.png').convert(),pygame.image.load('lugares/fondo.jpg').convert()]
def move_map(self):
    #print(pygame.mouse.get_pos())
    #orientacion(self)
    #other_punchs_or_kicks(self)

    global contador_de_salida,indice_west_city,west_city,indice_surfaces,numero_de_cambio,west_city_x,west_city_y,index_sprite,move
    cont_round = round(contador_de_salida)
    self.lista_img = [up_sprite_list[index_sprite],prob[index_sprite],left_sprite_list[index_sprite],right_sprite_list[index_sprite]]
    self.punch = punch
    self.kekkai = kekkai
    print(index_sprite)

    """collisions"""
    if map_activates == 'free_battle':
        """if indice_lugares == 0:

            #casa
            collision_kame_house(self,(305,320),480,0)
            collision_kame_house(self,(100,340),640,0)
            #palmeras
            collision_kame_house(self,(50,50),850,100)
            collision_kame_house(self, (50, 50), 810, 340)
        if indice_lugares == 1:
            print('a')
        if indice_lugares == 2:
            collision_grand_kai_tournament(self)"""
    """maps"""
    if map_activates == 'free_battle':
        lugar_actual = mapita[indice_lugares]
        screen.blit(lugar_actual, (0, -200))

    elif map_activates == 'tournament':
        if p1.type_surface == 'variable':
            print('xd')
        if not p1.type_surface == 'variable':
            screen.blit(gta,(0,-200))
        #collision_grand_kai_tournament(self)
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
        map_copy_alpha.set_colorkey((0,0,0))
        screen.blit(map_copy_alpha,(0,0))
        #create_character(self,mainer)
        collide_for_color(self,(248,0,0),west_copy_subsurf,1,(32,32))
        draw_the_surf_in_other(invisible_object(p1.s_rect,(32,32),west_copy_subsurf,colorin_allowed),map_copy_alpha)
        move_npc_for_enemy(self,the_npc_0,300)
        create_character(self,mainer)
        #screen.blit(prob[index_sprite][index_sprite],(0,0))
        #move_in_map(self,500,recto,objetos_de_west_city)
        #print(west_city_x,west_city_y)
        if p1.moverse['up'] == True:
            enem.e_rect.y += p1.velocidad
            if west_city_y > 0:
                west_city_y -= p1.velocidad
        if p1.moverse['down'] == True:
            enem.e_rect.y -= p1.velocidad
            if west_city_y < 2300:
                west_city_y += p1.velocidad
        if p1.moverse['left'] == True:
            if west_city_x > 0:
                west_city_x -= p1.velocidad
        if p1.moverse['right'] == True:
            if west_city_x < 1900:
                west_city_x += p1.velocidad
    elif map_activates == 'training':

        screen.blit(p1_actual,(0,100))
        screen.blit(p2_actual,(1200,100))
        skill_current = skills_imgs[round(index_skills)]
        skill_current.set_colorkey(colorkeys[round(index_skills)])
        screen.blit(skill_current,(0,300))
        string_blit(skills_names[round(index_skills)],(0,450),45,(255,0,0))
    if map_activates != 'training':
        p1.vel_trasicion_img = 0.1
surf_tournament = pygame.Surface((200,200))
color_tour = (0,255,0)

surf_free_battle = pygame.Surface((200,200))
color_free = (138,43,226)

surf_history = pygame.Surface((200,200))
color_history = (193,255,193)

surf_training = pygame.Surface((200,200))
training_color = (205,85,85)
def change_map(self):
    global map_activates,the_character,indice_lugares,the_enemy,index_skills
    rgb = (random.randint(0,250),random.randint(0,250),random.randint(0,250),random.randint(0,250))

    """cambiar portrait"""
    cambiar_portada(self)
    if pygame.mouse.get_pressed()[1] == True:
        map_activates = 'training'
    if menu.active == True:
        string_blit(str(map_activates),(900,50),50,rgb)
        """boton tour"""
        #surf_tournament.fill(color_tour)
        surf_tournament.fill(rgb)
        screen.blit(surf_tournament,(500,100))
        string_blit('Tournament',(500,100),43,(255,255,255))
        """boton free"""
        #surf_free_battle.fill(color_free)
        surf_free_battle.fill((255,255,255))
        screen.blit(surf_free_battle,(800,100))
        string_blit('Free_battle', (800, 100), 43, (255,0,0))
        """boton_history"""
        #surf_history.fill(color_history)
        surf_history.fill((238,201,0))
        screen.blit(surf_history,(200,100))
        string_blit('History',(200,100),43,(0,0,0))
        """boton training"""
        #surf_training.fill(training_color)
        surf_training.fill((0,0,0))
        screen.blit(surf_training,(200,300))
        string_blit('Training',(200,300),42,(255,255,255))
        """hover"""
        if map_activates != 'free_battle':
            if hover(self,pygame.mouse.get_pos(),(500,100),(200,200)):
                if pygame.mouse.get_pressed()[0] == True:
                    map_activates = 'tournament'
            if hover(self, pygame.mouse.get_pos(), (800, 100), (200, 200)):
                if pygame.mouse.get_pressed()[0] == True:
                    map_activates = 'free_battle'
            if hover(self, pygame.mouse.get_pos(), (200, 100), (200, 200)):
                if pygame.mouse.get_pressed()[0] == True:
                    map_activates = 'history'
            if hover(self, pygame.mouse.get_pos(), (200, 300), (200, 200)):
                if pygame.mouse.get_pressed()[0] == True:
                    map_activates = 'training'
        """change character"""
        """change free battle"""
        if map_activates == 'free_battle':
            #collision(self, (200,200), (840, 390),p1.s_rect, p1.velocidad)
            """hover"""
            if hover(self, pygame.mouse.get_pos(), (200, 200), (64, 64)):
                if pygame.mouse.get_pressed()[0] == True:
                    the_character = 'broly'
            if hover(self, pygame.mouse.get_pos(), (300, 200), (64, 64)):
                if pygame.mouse.get_pressed()[0] == True:
                    the_character = 'goku'
            if hover(self, pygame.mouse.get_pos(), (400, 200), (64, 64)):
                if pygame.mouse.get_pressed()[0] == True:
                    the_character = 'vegeta'
            """hover"""
            if hover(self, pygame.mouse.get_pos(), (200, 200), (64, 64)):
                if pygame.mouse.get_pressed()[2] == True:
                    the_enemy = 'broly'
            if hover(self, pygame.mouse.get_pos(), (300, 200), (64, 64)):
                if pygame.mouse.get_pressed()[2] == True:
                    the_enemy = 'goku'
            if hover(self, pygame.mouse.get_pos(), (400, 200), (64, 64)):
                if pygame.mouse.get_pressed()[2] == True:
                    the_enemy = 'vegeta'
            """map"""
            if hover(self, pygame.mouse.get_pos(), (200, 600), (100, 100)):
                if pygame.mouse.get_pressed()[0] == True:
                    indice_lugares = 0
            if hover(self, pygame.mouse.get_pos(), (350, 600), (100, 100)):
                if pygame.mouse.get_pressed()[0] == True:
                    indice_lugares = 1
            if hover(self, pygame.mouse.get_pos(), (500, 600), (100, 100)):
                if pygame.mouse.get_pressed()[0] == True:
                    indice_lugares = 2
            if hover(self, pygame.mouse.get_pos(), (650, 600), (100, 100)):
                if pygame.mouse.get_pressed()[0] == True:
                    indice_lugares = 3
            seleccion_free_battle(self)
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

