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
    vel_trasicion_img = 0.1
    indice = 0
    bool_game = True
    num_change = 1
    life_color = (200,0,20)
    life_position = (100,50)
    """background"""
    color_fondo = (255,0,0)
    """punch speed multiplier"""
    punch_speed_multiplier = 3
    """index string"""
    index_string = ['up','down','left','right']
    """max frames y y max index"""
    max_frames = 5
    #max_index =
    """superficies y rects"""
    superficie = [pygame.Surface((100, 100))]
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
    def __init__(self, screen, width,height):
        """asignar"""
        self.screen = screen
        #self.lista_img = lista_img
        self.width = width
        self.height = height
        """verificar lista"""

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
                self.variables = [self.lista_img[0],self.lista_img[1],self.lista_img[2],self.lista_img[3]]
                self.tmp = max(self.variables)
                self.index = self.variables.index(self.tmp)
                if self.punch is not None:
                    if self.index < 4:
                        for punchin in punch:
                            self.variables.append(punchin)
                if self.kekkai is not None:
                    if self.index < 8:
                        for kek in kekkai:
                            self.variables.append(kek)



                self.img_actual = pygame.transform.rotozoom(pygame.image.load(f"{self.variables[self.indice]}{self.numero_redondeado}{self.formato}").convert(),0,self.scale_surf)
                self.img_actual.set_colorkey(self.color_back_surf)
                """outline"""
                self.perfect_outline(self.screen,self.img_actual,self.s_rect,1)
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
                self.num_change = 1
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
        if self.enem_class.indice_enem == 1:
            self.indice = 0
        elif self.enem_class.indice_enem == 0:
            self.indice = 1
        elif self.enem_class.indice_enem == 2:
            self.indice = 3
        elif self.enem_class.indice_enem == 3:
            self.indice = 2
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
            self.num_change = 1
        if self.indice > 3:
            if self.num_change > 4:
                self.num_change = 1
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
            #mostrar_desde_variable(self.screen, self.surf, self.img_actual, self.e_rect, (0, 128, 128))
class Monsters:
    amount = 5
    def __init__(self,screen):
        self.screen = screen





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

    #def
class Map_world:
    """transport to coordenates"""

    """ocean"""
    ocean = None
    """floor"""
    floor = None
    floor_x = 0
    floor_y = 0
    x_sub = 100
    y_sub = 100
    heigth_floor = 500
    width_floor = 500
    floor_dimentions = (2000,2000)

    """obj"""
    home_list = None
    pos_x = None
    pos_y = None
    wid = None
    high = None
    """scale"""
    dimentions = (200,200)
    """event movement"""

    """tiles"""
    tilepos = [0,1,0]
    tile_wid = 100
    tile_height = 100
    """distance cooling"""
    distance_cooling = 500
    distance_cooling_place = 2000
    """collition"""
    collide = False
    def __init__(self,screen,player_pos,move_velocity,screen_wid,screen_height):
        self.screen = screen
        self.player_pos = player_pos
        self.move_velocity = move_velocity
        self.core_surface = (self.dimentions[0] // 2,self.dimentions[1] // 2)
        #print(self.core_surface)
        if self.home_list is not None and self.pos_x is not None and self.pos_y is not None:
            for home,x,y,wid,high in zip(self.home_list,self.pos_x,self.pos_y,self.wid,self.high):
                self.blit_cooling(home, x, y, self.player_pos,self.distance_cooling)
                if self.hover(self.player_pos,(x,y),(wid,high)):
                    self.collide = True
                    if self.player_pos.x > x + self.core_surface[0]:
                        self.player_pos.x += move_velocity
                    if self.player_pos.x < x + self.core_surface[0]:
                        self.player_pos.x -= move_velocity
                    if self.player_pos.y > y + self.core_surface[1]:
                        self.player_pos.y += move_velocity
                    if self.player_pos.y < y + self.core_surface[1]:
                        self.player_pos.y -= move_velocity
                #else:
                    #self.collide = False
            #self.blit_cooling(self.home_list[0],self.pos_x[0],self.pos_y[0],self.player_pos,self.distance_cooling)
    def hover(self,surf_pos,button_pos,scale):
        if surf_pos.x > button_pos[0] and surf_pos.x < button_pos[0] + scale[0] and surf_pos.y > button_pos[1] and surf_pos.y < button_pos[1] + scale[1]:
            return True
        else:
            return False

    def blit_cooling(self,surface_map,rect_map_x,rect_map_y,rect_surf,distance):
        if (math.sqrt(((rect_map_x - rect_surf.x) ** 2) + ((rect_map_y - rect_surf.y) ** 2))) < distance:

            self.screen.blit(surface_map, (rect_map_x,rect_map_y))

class Ki:
    """asignar a ki usable"""
    cantidad = 100
    desgaste = 1
    color = (255,127,36)
    """asignar a la barra de ki"""
    height_bar = 20
    ki_bar = pygame.Surface((cantidad,height_bar))
    color_bar = (0,0,255)
    ki_bar_pos = (0,50)
    """ki blast"""

    ki_blast = pygame.Surface((10,10))
    ki_blast_pos = ki_blast.get_rect()
    ki_blast_velocity = 10
    crono_explode = 0
    crono_vel = 0.1
    """damage"""
    damage = 100
    """ki follow"""
    distance = 10000
    """back vel"""
    back_vel = 10
    def __init__(self,screen):
        self.screen = screen

        #self.ki_blast_pos = self.ki_blast.get_rect()
        self.ki_bar.fill(self.color_bar)
        self.screen.blit(self.ki_bar,self.ki_bar_pos)
        self.ki_blast.fill(self.color)
        self.screen.blit(self.ki_blast,self.ki_blast_pos)







class Shaders:
    """color surfaces"""
    color_screen_surface = (255,0,0)
    outline_color = (0,0,0)
    """dimensiones del screen_surface"""
    dimensiones = (50,50)
    """transparencia"""
    trans_screen_surface = 100
    """superficies"""
    red_screen = pygame.Surface((dimensiones[0],dimensiones[1]),pygame.SRCALPHA)
    #outline = pygame.Surface(())
    def __init__(self,screen):
        self.screen = screen
        self.red_screen.fill((0, 0, 0, self.trans_screen_surface))
        self.screen.blit(self.red_screen, (0, 0))
class NPC:
    """objetos"""
    only_1_img = None

    """sprites"""
    sprites_list = None
    up_index = 0
    down_index = 1
    left_index = 2
    right_index = 3
    indice = up_index
    """prefab"""
    scale_prefab = 100
    color_prefab = (139,115,85)
    surface_person = pygame.Surface((scale_prefab,scale_prefab))
    """pos"""
    pos = surface_person.get_rect(center=(0,0))
    """objetivo"""
    objetivo = (0,0)
    """velocity"""
    npc_velocity = 2
    """switch"""
    active = True
    """contador"""
    contador = 0
    point_change = 50
    def __init__(self,screen):
        self.screen = screen
        """aumentar"""
        #print(self.pos)
        print(self.indice)
        """IA"""
        self.up_boolean = random.choice([True, False])
        self.down_boolean = random.choice([True, False])
        self.left_boolean = random.choice([True, False])
        self.right_boolean = random.choice([True, False])
        """ejecutar"""
        if self.up_boolean == True:
            if self.contador > self.point_change:
                self.up()
        if self.down_boolean == True:
            if self.contador > self.point_change:
                self.down()
        if self.left_boolean == True:
            if self.contador > self.point_change:
                self.left()
        if self.right_boolean == True:
            if self.contador > self.point_change:
                self.right()
        """verificar"""
        if self.only_1_img is None:
            self.surface_person.fill(self.color_prefab)
            self.screen.blit(self.surface_person,self.pos)

            #self.screen.blit(self.only_1_img,self.pos)
        if self.sprites_list is not None:
            self.current_img = pygame.transform.rotozoom(pygame.image.load(self.sprites_list[self.indice]), 0, 1)
            self.screen.blit(self.current_img,self.pos)
    def up(self):
        self.pos.y -= self.npc_velocity
        if self.sprites_list is not None:
            self.indice = self.up_index
    def down(self):
        self.pos.y += self.npc_velocity
        if self.sprites_list is not None:
            self.indice = self.down_index
    def left(self):
        self.pos.x -= self.npc_velocity
        if self.sprites_list is not None:
            self.indice = self.left_index
    def right(self):
        self.pos.x += self.npc_velocity
        if self.sprites_list is not None:
            self.indice = self.right_index
#print(NPC.random_boolean)

class History:
    """intro"""
    intro_text = 'xd'
    """dialogos"""
    Dialogo = None
    """creditos"""
    credits_txt = 'matzero 78'

class Sound:
    sound_track = None
    effect_punch = None
    effect_footprints = None
    effect_shunpo = None
    effecf_shoot = None
class EXP:
    amount = 10
    vel_amount = 1
    heigth = 20
    surface_amount = pygame.Surface((amount,heigth))
    color = (0,255,0)
    pos = (0,0)
    """level"""
    nvl = 0
    to_next_level = 60
    def __init__(self,screen,event_to_increase):
        self.screen = screen
    def amount_increase(self):
        self.amount += self.vel_amount
    def next_level(self):
        if self.amount > self.to_next_level:
            self.nvl += 1
class Transform:
    base = None
    fase_1 = None
    def __init__(self):
        self.xd_xd = 'xd'
    def xd(self,lista,lista2):
        print(lista)
class Aura:
    thickness = 1

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
