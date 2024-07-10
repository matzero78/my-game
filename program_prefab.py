
import math
import random
import pygame
import copy
from xd import value

from utiles import mostrar_desde_variable
from funciones_de_calculo import *
from funciones_de_diccionario import *
from funciones_para_mostrar_img import *
from funciones_para_guardar_img import *
from videos import *
from buttons import *
from metas_xp import value_metas
"""ancho y alto,fps"""
width = 1280
heigth = 720
fps = 60
"""iniciar pantalla"""
lista_de_pantalla = [pygame.RESIZABLE,pygame.FULLSCREEN]
index_pantalla = 0
pantalla = lista_de_pantalla[index_pantalla]
pygame.init()
pygame.joystick.init()
joysticks = []
screen = pygame.display.set_mode((width, heigth), pantalla)
pygame.display.set_caption('')
icon = pygame.Surface((32,32))
pygame.display.set_icon(icon)


def return_spritesheet_with_auto_width(img,pos,cantidad_frame,color_back):
    listi = []
    index_img = 0
    anchos = []
    ancho = 0
    alto = 30
    detect_color = img.get_at((pos[0], pos[1]))
    for i in range(1,cantidad_frame+1):
        pos[0] += 1
        if detect_color == color_back:
            anchos.append(ancho)
            ancho = 0
            if encontrar_maximo_de_elementos(anchos) > 0:
                listi.append(pygame.Surface.subsurface(img,(pos[0],pos[1]),(anchos[index_img],alto))) 
            if encontrar_maximo_de_elementos(listi) > 0:
                index_img += 1
        if detect_color != color_back:
            ancho += 1
    return listi



def erase_color_list(surface,list_color,color_replace):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            color = surface.get_at((x,y))
            if color in list_color:
                surface.set_at((x, y), color_replace)
    return surface
def return_spritesheet(img,loc,dimensions,cantidad_frame,vertical_bool,horizontal_bool,list_bool_flip,scale):
    listi = []
    for i in range(1,cantidad_frame+1):
        listi.append(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(img,(loc[0],loc[1]),(dimensions[0],dimensions[1])),0,scale),list_bool_flip[0],list_bool_flip[1]))
        if horizontal_bool == True:
            loc[0] += dimensions[0]
        if vertical_bool == True:
            loc[1] += dimensions[1]
    return listi
def return_spritesheet_V2(img,loc,dimensions,cantidad_frame,vertical_bool,horizontal_bool,reverse_horizontal_bool,reverse_vertical_bool,list_bool_flip,scale):
    listi = []
    for i in range(1,cantidad_frame+1):
        listi.append(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(img,(loc[0],loc[1]),(dimensions[0],dimensions[1])),0,scale),list_bool_flip[0],list_bool_flip[1]))
        if horizontal_bool == True:
            loc[0] += dimensions[0]
        if vertical_bool == True:
            loc[1] += dimensions[1]
        if reverse_horizontal_bool == True:
            loc[0] -= dimensions[0]
        if reverse_vertical_bool == True:
            loc[1] -= dimensions[1]
    return listi
def return_spritesheet_without_bg(img,loc,dimensions,cantidad_frame,vertical_bool,horizontal_bool,list_bool_flip,scale,list_color,replace_color):
    listi = []
    for i in range(1,cantidad_frame+1):
        listi.append(erase_color_list(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(img,(loc[0],loc[1]),(dimensions[0],dimensions[1])),0,scale),list_bool_flip[0],list_bool_flip[1]),list_color,replace_color))
        if horizontal_bool == True:
            loc[0] += dimensions[0]
        if vertical_bool == True:
            loc[1] += dimensions[1]
    return listi

def charge_img(name,max,extension,scale,angle):
    lista_imgs = []
    for i in range(1,max):
        lista_imgs.append(pygame.transform.rotozoom(pygame.image.load(f'{name}{i}{extension}').convert(),angle,scale))
    return lista_imgs
def charge_img_to_vid(name,max,extension,scale,angle,rect,list_bool_flip):
    lista_imgs = []
    for i in range(1,max):
        lista_imgs.append(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(pygame.image.load(f'{name}{i}{extension}').convert(),rect),angle,scale),list_bool_flip[0],list_bool_flip[1]))
    return lista_imgs
def charge_img_without_background(name,max,extension,scale,angle,rect,list_bool_flip,background_colors,color_replace):
    lista_imgs = []
    for i in range(1,max):
        lista_imgs.append(erase_color_list(pygame.transform.flip(pygame.transform.rotozoom(pygame.Surface.subsurface(pygame.image.load(f'{name}{i}{extension}').convert(),rect),angle,scale),list_bool_flip[0],list_bool_flip[1]),background_colors,color_replace))

    return lista_imgs

def save_surf_repeated(amount,surf):
    surfs = []
    for i in range(1,amount+1):
        surfs.append(surf)
    return surfs
"""videos"""
vid_ghost = charge_img('videos/frames/bishoujo_ghostface/Video1-Frame',10,'.jpg',0.4 ,0)
video_ghostface = {'video_frames':vid_ghost,'max_frames':encontrar_maximo_de_elementos(vid_ghost)-1,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False,'restart':False
                   }
vid_ichigo_vs_kenpachi = charge_img('videos/frames/ichigo vs kenpachi/Video1-Frame',3000,'.jpg',0.5,0)
video_bleach = {'video_frames':vid_ichigo_vs_kenpachi,'max_frames':encontrar_maximo_de_elementos(vid_ichigo_vs_kenpachi)-1,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_goku_sad = {'video_frames':charge_img('videos/frames/goku sad/Video1-Frame',1,'.jpg',5,0),'max_frames':90,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_saitama_meme = {'video_frames':charge_img('videos/frames/saitama achicado/Video1-Frame',1,'.jpg',0.5,0),'max_frames':130,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':1.5,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_dante_dr_fauss = {'video_frames':charge_img('videos/frames/dante dr_fauss/Video1-Frame',1,'.jpg',0.5,0),'max_frames':56,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.8,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
#3d false
def return_3d_avatar(up_spritesheet,down_spritesheet,right_spritesheet,rect_sprites,pos_player,scale_of_surf,frames):
    rects = [rect_sprites,[0,0,250,250],[0,0,250,250],[0,0,250,250]]
    vids = [
        return_spritesheet(pygame.image.load(up_spritesheet).convert_alpha(),rects[0],[rect_sprites[2],rect_sprites[3]],frames,False,True,(False,False),scale_of_surf),
        return_spritesheet(pygame.image.load(down_spritesheet).convert_alpha(),rects[1],[rect_sprites[2],rect_sprites[3]],frames,False,True,(False,False),scale_of_surf),
        return_spritesheet(pygame.image.load(right_spritesheet).convert_alpha(),rects[2],[rect_sprites[2],rect_sprites[3]],frames,False,True,(True,False),scale_of_surf),
        return_spritesheet(pygame.image.load(right_spritesheet).convert_alpha(),rects[3],[rect_sprites[2],rect_sprites[3]],frames,False,True,(False,False),scale_of_surf),
        ]
    vids_dict = [
        {'video_frames':vids[0],'max_frames':encontrar_maximo_de_elementos(vids[0])-1,'sound':'','vel':0.8,'indice':0,'pos':pos_player,'bool_pause':False},
        {'video_frames':vids[1],'max_frames':encontrar_maximo_de_elementos(vids[1])-1,'sound':'','vel':0.8,'indice':0,'pos':pos_player,'bool_pause':False},
        {'video_frames':vids[2],'max_frames':encontrar_maximo_de_elementos(vids[2])-1,'sound':'','vel':0.8,'indice':0,'pos':pos_player,'bool_pause':False},
        {'video_frames':vids[3],'max_frames':encontrar_maximo_de_elementos(vids[3])-1,'sound':'','vel':0.8,'indice':0,'pos':pos_player,'bool_pause':False},
    ]
    return vids_dict

#briggite
briggite_scale = (250,250)
scale_pre_render = 1.5
pos_player = [200,350]
pos_enem = [600,350]

briggite_idle = return_3d_avatar('personaje pre render/briggite/idle/back.png','personaje pre render/briggite/idle/front.png','personaje pre render/briggite/idle/right.png',[0,0,250,250],pos_enem,scale_pre_render,91)
briggite_move = return_3d_avatar('personaje pre render/briggite/move/back.png','personaje pre render/briggite/move/front.png','personaje pre render/briggite/move/right.png',[0,0,250,250],pos_enem,scale_pre_render,31)
briggite_punch = return_3d_avatar('personaje pre render/briggite/punch/back.png','personaje pre render/briggite/punch/front.png','personaje pre render/briggite/punch/right.png',[0,0,250,250],pos_enem,scale_pre_render,90)
briggite_emote = return_3d_avatar('personaje pre render/briggite/gesto/back.png','personaje pre render/briggite/gesto/front.png','personaje pre render/briggite/gesto/right.png',[0,0,250,250],pos_enem,scale_pre_render,83)
briggite_idle.extend(briggite_move)
briggite_idle.extend(briggite_punch)
briggite_idle.extend(briggite_emote)
#master
master_scale = (250,250)

master_idle = return_3d_avatar('personaje pre render/master chief/idle/back.png','personaje pre render/master chief/idle/front.png','personaje pre render/master chief/idle/right.png',[0,0,250,250],pos_player,scale_pre_render,75)
master_move = return_3d_avatar('personaje pre render/master chief/walk/back.png','personaje pre render/master chief/walk/front.png','personaje pre render/master chief/walk/right.png',[0,0,250,250],pos_player,scale_pre_render,31)
master_punch = return_3d_avatar('personaje pre render/master chief/punch/back.png','personaje pre render/master chief/punch/front.png','personaje pre render/master chief/punch/right.png',[0,0,250,250],pos_player,scale_pre_render,81)
master_emote = return_3d_avatar('personaje pre render/master chief/gesto/back.png','personaje pre render/master chief/gesto/front.png','personaje pre render/master chief/gesto/right.png',[0,0,250,250],pos_player,scale_pre_render,85)
master_idle.extend(master_move)
master_idle.extend(master_punch)
master_idle.extend(master_emote)
#kratos
kratos_idle = return_3d_avatar('personaje pre render/kratos/idle/back.png','personaje pre render/kratos/idle/front.png','personaje pre render/kratos/idle/right.png',[0,0,250,250],pos_player,scale_pre_render,67)
kratos_move = return_3d_avatar('personaje pre render/kratos/walk/back.png','personaje pre render/kratos/walk/front.png','personaje pre render/kratos/walk/right.png',[0,0,250,250],pos_player,scale_pre_render,31)
kratos_punch = return_3d_avatar('personaje pre render/kratos/punch/back.png','personaje pre render/kratos/punch/front.png','personaje pre render/kratos/punch/right.png',[0,0,250,250],pos_player,scale_pre_render,42)
kratos_emote = return_3d_avatar('personaje pre render/kratos/gesto/back.png','personaje pre render/kratos/gesto/front.png','personaje pre render/kratos/gesto/right.png',[0,0,250,250],pos_player,scale_pre_render,85)
kratos_idle.extend(kratos_move)
kratos_idle.extend(kratos_punch)
kratos_idle.extend(kratos_emote)
#dante
dante_idle = return_3d_avatar('personaje pre render/dante/idle/back.png','personaje pre render/dante/idle/front.png','personaje pre render/dante/idle/right.png',[0,0,250,250],pos_player,scale_pre_render,121)
dante_move = return_3d_avatar('personaje pre render/dante/walk/back.png','personaje pre render/dante/walk/front.png','personaje pre render/dante/walk/right.png',[0,0,250,250],pos_player,scale_pre_render,42)
dante_punch = return_3d_avatar('personaje pre render/dante/punch/back.png','personaje pre render/dante/punch/front.png','personaje pre render/dante/punch/right.png',[0,0,250,250],pos_player,scale_pre_render,56)
dante_emote = return_3d_avatar('personaje pre render/dante/gesto/back.png','personaje pre render/dante/gesto/front.png','personaje pre render/dante/gesto/right.png',[0,0,250,250],pos_player,scale_pre_render,67)
dante_idle.extend(dante_move)
dante_idle.extend(dante_punch)
dante_idle.extend(dante_emote)
#character
briggite_character = {'imgs':briggite_idle,'index':2,'index_sum':0,'index_sum_2':0,'index_sum_3':0}
master_character = {'imgs':master_idle,'index':0,'index_sum':0,'index_sum_2':0,'index_sum_3':0}
kratos_character = {'imgs':kratos_idle,'index':0,'index_sum':0,'index_sum_2':0,'index_sum_3':0}
dante_character = {'imgs':dante_idle,'index':0,'index_sum':0,'index_sum_2':0,'index_sum_3':0}

index_character = 2
characters = [master_character,kratos_character,dante_character,briggite_character]
index_character_enem = 0
characters_enem = [briggite_character]
map_3d_fake = {}
def camera_follow(screen,map_dict,videos_dict,up_bool,down_bool,left_bool,right_bool,punch_bool,emote_bool,pos,vel):
    #print(briggite_move)
    #print(videos_dict['index_sum'],'ttttttttttttttttt')
    #punch
    if punch_bool == True and emote_bool == False:
        videos_dict['index_sum'] = 8
    if punch_bool == False:
        videos_dict['index_sum'] = 0
    #emote
    if emote_bool == True and punch_bool == False:
        videos_dict['index_sum_3'] = 12
    if emote_bool == False:
        videos_dict['index_sum_3'] = 0
    #move
    if up_bool == True:
        videos_dict['index'] = 0
    if down_bool == True:
        videos_dict['index'] = 1
    if left_bool == True:
        pos[0] -= vel
        videos_dict['index'] = 2
    if right_bool == True:
        pos[0] += vel
        videos_dict['index'] = 3 
    img = videos_dict['imgs'][videos_dict['index'] + videos_dict['index_sum'] + videos_dict['index_sum_2'] + videos_dict['index_sum_3']]
    img['pos'] = pos
    if up_bool == False and down_bool == False and left_bool == False and right_bool == False:
        videos_dict['index_sum_2'] = 0
    if up_bool == True or down_bool == True or left_bool == True or right_bool == True:
        videos_dict['index_sum_2'] = 4
        videos_dict['index_sum'] = 0
        videos_dict['index_sum_3'] = 0
        #img['indice'] = 0
        #if img['indice'] >= 20:
            #img['indice'] -= img['vel']
    blit_video(screen,img)
def redirect_enem(pos,pos_enem,distance):
    avis = avistamiento('p',pos,pos_enem,distance)
    if avis == True:
        if pos[0] < pos_enem[0]:
            return {'left':False,'right':True}
        if pos[0] > pos_enem[0]:
            return {'left':True,'right':False}
        else:
            return {'left':False,'right':False}
    if avis == False:
        return {'left':False,'right':False}
def pre_render_npc(videos_dict,screen,pos,pos_enem):
    
    #ver
    
    

    #rect
    rect_player = [pos[0],pos[1],250,250]
    rect_enem = [pos_enem[0],pos_enem[1],250,250]
    #seguir
    avis = redirect_enem(pos,pos_enem,400)
    

        
    
    #collide

    camera_follow(screen,map_3d_fake,videos_dict,False,False,avis['left'],avis['right'],Colliderect(rect_player,rect_enem),False,pos,1)


class player:
    """fps"""
    fps = 60
    moverse = {'up':False,'down':False,'left':False,'right':False,'punch':False,'kekkai':False,'shunpo':False,'ki_blast':False,'grab':False,'charge':False,'esp':False,'esp_2':False}
    posicion = [100,200]
    bool_game = True
    """background"""
    color_fondo = (255,0,0)
    """punch speed multiplier"""
    punch_speed_multiplier = 3
    """max frames y y max index"""
    max_frames = 4
    """superficies y rects"""
    superficie = [pygame.Surface((40, 60))]
    s_rect = superficie[0].get_rect(center=(posicion[0], posicion[1]))
    """minimap"""
    minimap = None
    """menu"""
    menu = None
    """function extras"""
    function_normal = None
    function_in_menu = None
    function_keyboard = None
    def __init__(self, screen, width,height):
        """asignar"""
        self.screen = screen
        """utilizar"""
        while self.bool_game == True:

            pygame.time.Clock().tick(fps)
            if self.function_normal is not None:
                self.function_normal()
            """mostrar"""
            if self.menu is not None:
                self.menu(self.screen)
                if self.function_in_menu is not None:
                    self.function_in_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bool_game = False
                    #pygame.quit()
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

                    if event.key == pygame.K_g:  #grab
                        self.moverse['grab'] = True
                    if event.key == pygame.K_r:  #esp
                        self.moverse['esp'] = True
                    if event.key == pygame.K_t:  #esp_2
                        self.moverse['esp_2'] = True

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
                    if event.key == pygame.K_g:  #grab
                        self.moverse['grab'] = False
                    if event.key == pygame.K_r:  #esp
                        self.moverse['esp'] = False
                    if event.key == pygame.K_t:  #esp_2
                        self.moverse['esp_2'] = False
            #charge
            if pygame.mouse.get_pressed()[1] == True:
                self.moverse['charge'] = True
            if pygame.mouse.get_pressed()[1] == False:
                self.moverse['charge'] = False
            #punch
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


    


class Menu:
    image_background = None
    palabra = {'txt':'dbz legacy of battle','pos':(0,680),'scale':42,'color':(255,255,255)}
    """activar o desactivar menu"""
    active = True
    """especial"""
    version = {'txt':'1.0.0','pos':(0,500),'scale':32,'color':(255,0,0)}
    def __init__(self,screen):
        self.screen = screen
        if self.active == True:
            if self.image_background is not None:
                self.screen.blit(self.image_background,(0,0))
            string_blit(self.version['txt'],self.version['pos'],self.version['scale'],self.version['color'],screen)
            string_blit(self.palabra['txt'],self.palabra['pos'],self.palabra['scale'],self.palabra['color'],screen)
    
"""menu"""
img_back = pygame.image.load('tema de menu principal/goku_kaioken vs vegeta.jpg')
menu = Menu
menu.image_background = img_back




"""character main"""
scala_sprites = 1.5
#spritesheet
#goku
goku_spritesheet = pygame.image.load('movimiento/goku_spritesheet.png').convert_alpha()
goku_ssg_spritesheet = pygame.image.load('movimiento/goku_spritesheet_goku_ssg.png').convert_alpha()
goku_ultrainstinc_spritesheet = pygame.image.load('movimiento/goku_spritesheet_goku_ultra_instinc.png').convert_alpha()
goku_spritesheet_db_log_1 = pygame.image.load('personajes/goku/39936.png').convert_alpha()
#broly
Broly_spritesheet = pygame.image.load('movimiento/goku_spritesheet.png').convert_alpha()
#vegeta
vegeta_spritesheet = pygame.image.load('personajes/vegeta/75737.png').convert_alpha()
vegeta_ssg_spritesheet = pygame.image.load('personajes/vegeta/vegeta_ssg.png').convert_alpha()
vegeta_MI_spritesheet = pygame.image.load('personajes/vegeta/vegeta_MI.png').convert_alpha()
#trunks
trunks_spritesheet = pygame.image.load('personajes/trunks/14504 (1).png').convert_alpha()
trunks_kid_spritesheet = pygame.image.load('personajes/trunks/14503.png').convert_alpha()
#picoro

piccolo_spritesheet = pygame.image.load('personajes/piccoro/14502.png').convert_alpha()
piccolo_orange_spritesheet = pygame.image.load('personajes/piccoro/picolo_orange.png').convert_alpha()
piccolo_red_spritesheet = pygame.image.load('personajes\piccoro\picolo_red.png').convert_alpha()

#dante
dante_spritesheet = pygame.image.load('personajes/dante sparda/dante.png').convert_alpha()
#saitama
saitama_spritesheet = pygame.image.load('personajes/saitama/saitama.png').convert_alpha()
#gogeto
gogeto_sprite = pygame.image.load('personajes/gogeto/58808.png').convert_alpha()
#vegito
vegito_sprite = pygame.image.load('personajes/vegito/49926.png').convert_alpha()
#satan
spritesheet_mr_satan = pygame.image.load('personajes/mr satan/75736 (1).png').convert_alpha()
#broly
spritesheet_broly = pygame.image.load('personajes/broly/156873.png').convert_alpha()
#bulma
spritesheet_bulma = pygame.image.load('personajes/To npc/bulma.png')
#milk
spritesheet_milk = pygame.image.load('personajes/To npc/milk.png')

"""scales"""
#goku
goku_log1_scale = (20,33)
goku_scale = (17,33)
goku_scale_punch = (22,33)
#vegeta
vegeta_scale = [(17,33),(22,33),(21,33)]
#gogeto
gogeto_scale = (17,32)
#vegito
vegito_scale = (19,32)
#piccolo
piccolo_scale = [(16,32),(30,33)]
#satan
satan_scale = (17,32)
satan_scale_punch = (23,32)
#broly
broly_scale = (60,65)
"""the sprites"""
#goku
goku_sprite_list = [return_spritesheet(goku_spritesheet,[1,66],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,0],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,33],goku_scale,4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,33],goku_scale,4,False,True,(False,False),scala_sprites),
                    
                    return_spritesheet(goku_ssg_spritesheet,[276,66],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[292,0],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(False,False),scala_sprites)
                    ]
goku_ssj_sprite_list = [return_spritesheet(goku_spritesheet,[1,199],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,133],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,166],goku_scale,4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[18,166],goku_scale,4,False,True,(False,False),scala_sprites),
                    
                    return_spritesheet(goku_ssg_spritesheet,[276,199],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[292,133],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,166],(24,33),4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,166],(24,33),4,False,True,(False,False),scala_sprites)
                    ]
goku_UI_sprite_list = [return_spritesheet(goku_ultrainstinc_spritesheet,[1,66],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[18,0],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[18,33],goku_scale,4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[18,33],goku_scale,4,False,True,(False,False),scala_sprites),
                    
                    return_spritesheet(goku_ultrainstinc_spritesheet,[276,199],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[292,133],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[387,166],(24,33),4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ultrainstinc_spritesheet,[387,166],(24,33),4,False,True,(False,False),scala_sprites)
                    ]

goku_log1_sprite_list = [return_spritesheet(goku_spritesheet_db_log_1,[220,86],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet_db_log_1,[18,86],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet_db_log_1,[461,86],goku_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet_db_log_1,[461,86],goku_scale,4,False,True,(True,False),scala_sprites),
                    
                    return_spritesheet(goku_ssg_spritesheet,[276,66],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[292,0],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(False,False),scala_sprites)
                    ]
goku_yardrat_sprite_list = [return_spritesheet(goku_spritesheet,[422,267],goku_scale,4,False,False,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[87,267],goku_scale,4,False,False,(False,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[174,267],goku_scale,4,False,False,(True,False),scala_sprites),
                    return_spritesheet(goku_spritesheet,[174,267],goku_scale,4,False,False,(False,False),scala_sprites),
                    
                    return_spritesheet(goku_ssg_spritesheet,[276,66],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[292,0],goku_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(True,False),scala_sprites),
                    return_spritesheet(goku_ssg_spritesheet,[387,34],(24,33),4,False,True,(False,False),scala_sprites)
                    ]
nube_voladora_sprite = pygame.image.load('item/nube.png').convert_alpha()
nube_voladora_scale = (32,16)
nube_voladora_scale_total = 1.5
nube_voladora = [return_spritesheet(nube_voladora_sprite,[0,48],nube_voladora_scale,4,False,True,(False,False),nube_voladora_scale_total),
                    return_spritesheet(nube_voladora_sprite,[0,16],nube_voladora_scale,4,False,True,(False,False),nube_voladora_scale_total),
                    return_spritesheet(nube_voladora_sprite,[0,32],nube_voladora_scale,4,False,True,(False,False),nube_voladora_scale_total),
                    return_spritesheet(nube_voladora_sprite,[0,32],nube_voladora_scale,4,False,True,(True,False),nube_voladora_scale_total)]
#vegeta
vegeta_sprite_list = [
    return_spritesheet(vegeta_spritesheet,[1,66],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[18,0],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[18,33],vegeta_scale[0],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[18,33],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
                    
    return_spritesheet(vegeta_spritesheet,[205,200],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[222,135],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[228,167],vegeta_scale[2],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_spritesheet,[228,167],vegeta_scale[2],4,False,True,(False,False),scala_sprites)
]
vegeta_ssg_sprite_list = [
    return_spritesheet(vegeta_ssg_spritesheet,[1,66],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[18,0],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[18,33],vegeta_scale[0],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[18,33],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
                    
    return_spritesheet(vegeta_ssg_spritesheet,[205,200],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[222,135],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[228,167],vegeta_scale[2],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_ssg_spritesheet,[228,167],vegeta_scale[2],4,False,True,(False,False),scala_sprites)
]
vegeta_MI_sprite_list = [
    return_spritesheet(vegeta_MI_spritesheet,[1,200],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[18,135],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[18,167],vegeta_scale[0],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[18,167],vegeta_scale[0],4,False,True,(False,False),scala_sprites),
                    
    return_spritesheet(vegeta_MI_spritesheet,[205,66],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[222,0],vegeta_scale[1],4,False,True,(False,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[228,34],vegeta_scale[2],4,False,True,(True,False),scala_sprites),
    return_spritesheet(vegeta_MI_spritesheet,[228,34],vegeta_scale[2],4,False,True,(False,False),scala_sprites)
]
#trunks
trunks_scale = (17,34)
trunks_scale_punch = (22,32)
trunks_sprite_list = [
    return_spritesheet(trunks_spritesheet,[0,69],trunks_scale,4,False,True,(False,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[18,0],trunks_scale,4,False,True,(False,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[18,34],trunks_scale,4,False,True,(True,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[18,34],trunks_scale,4,False,True,(False,False),scala_sprites),

    return_spritesheet(trunks_spritesheet,[203,69],trunks_scale_punch,4,False,True,(False,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[223,0],trunks_scale_punch,4,False,True,(False,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[449,37],(26,34),4,False,True,(True,False),scala_sprites),
    return_spritesheet(trunks_spritesheet,[449,37],(26,34),4,False,True,(False,False),scala_sprites),
]

#gogeto
gogeto_scale_punch = (21,32)
gogeto_sprite_list = [return_spritesheet(gogeto_sprite,[0,67],gogeto_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[17,0],gogeto_scale,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[17,33],gogeto_scale,4,False,True,(True,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[17,33],gogeto_scale,4,False,True,(False,False),scala_sprites),
                    
                    return_spritesheet(gogeto_sprite,[354,67],gogeto_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[368,2],gogeto_scale_punch,4,False,True,(False,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[420,33],gogeto_scale_punch,4,False,True,(True,False),scala_sprites),
                    return_spritesheet(gogeto_sprite,[420,33],gogeto_scale_punch,4,False,True,(False,False),scala_sprites),
                    ]

#vegito
vegito_scale_punch = (24,32)
vegito_sprite_list = [return_spritesheet(vegito_sprite,[22,111],vegito_scale,4,False,True,(False,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[22,40],vegito_scale,4,False,True,(False,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[22,76],vegito_scale,4,False,True,(True,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[22,76],vegito_scale,4,False,True,(False,False),scala_sprites),
                         
                         return_spritesheet(vegito_sprite,[101,219],vegito_scale,4,False,True,(False,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[96,149],vegito_scale,4,False,True,(False,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[1,183],(28,32),4,False,True,(True,False),scala_sprites),
                         return_spritesheet(vegito_sprite,[1,183],(28,32),4,False,True,(False,False),scala_sprites),
                         ]

satan_sprite_list = [return_spritesheet(spritesheet_mr_satan,[0,66],satan_scale,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_mr_satan,[17,0],satan_scale,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_mr_satan,[17,33],satan_scale,4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_mr_satan,[17,33],satan_scale,4,False,True,(False,False),1.5),

                         return_spritesheet(spritesheet_mr_satan, [87, 67], satan_scale, 4, False, True, (False, False),1.5),
                         return_spritesheet(spritesheet_mr_satan, [104, 0], satan_scale, 4, False, True, (False, False),1.5),
                         return_spritesheet(spritesheet_mr_satan, [103, 33], satan_scale_punch, 4, False, True, (True, False),1.5),
                         return_spritesheet(spritesheet_mr_satan, [103, 33], satan_scale_punch, 4, False, True, (False, False),1.5),]
#piccoro
piccolo_sprite_list = [return_spritesheet(piccolo_spritesheet,[19,202],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_spritesheet,[18,135],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_spritesheet,[14,168],piccolo_scale[0],4,False,True,(True,False),1.5),
                         return_spritesheet(piccolo_spritesheet,[14,168],piccolo_scale[0],4,False,True,(False,False),1.5),
                         

                         return_spritesheet(piccolo_spritesheet, [507, 200], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_spritesheet, [530, 132], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (True, False),
                                            1.5),
                         return_spritesheet(piccolo_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         ]
piccolo_orange_sprite_list = [
                        return_spritesheet(piccolo_orange_spritesheet,[19,202],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_orange_spritesheet,[18,135],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_orange_spritesheet,[14,168],piccolo_scale[0],4,False,True,(True,False),1.5),
                         return_spritesheet(piccolo_orange_spritesheet,[14,168],piccolo_scale[0],4,False,True,(False,False),1.5),
                         

                         return_spritesheet(piccolo_orange_spritesheet, [507, 200], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_orange_spritesheet, [530, 132], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_orange_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (True, False),
                                            1.5),
                         return_spritesheet(piccolo_orange_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         ]
piccolo_red_sprite_list = [
                        return_spritesheet(piccolo_red_spritesheet,[19,202],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_red_spritesheet,[18,135],piccolo_scale[0],4,False,True,(False,False),1.5),
                         return_spritesheet(piccolo_red_spritesheet,[14,168],piccolo_scale[0],4,False,True,(True,False),1.5),
                         return_spritesheet(piccolo_red_spritesheet,[14,168],piccolo_scale[0],4,False,True,(False,False),1.5),
                         

                         return_spritesheet(piccolo_red_spritesheet, [507, 200], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_red_spritesheet, [530, 132], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(piccolo_red_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (True, False),
                                            1.5),
                         return_spritesheet(piccolo_red_spritesheet, [577, 166], piccolo_scale[1], 4, False, True, (False, False),
                                            1.5),
                         ]
#broly
broly_sprite_list = [return_spritesheet(spritesheet_broly,[160,101],broly_scale,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_broly,[161,19],broly_scale,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_broly,[165,172],broly_scale,4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_broly,[165,172],broly_scale,4,False,True,(False,False),1.5),

                         return_spritesheet(spritesheet_broly, [455, 101], broly_scale, 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(spritesheet_broly, [455, 19], broly_scale, 4, False, True, (False, False),
                                            1.5),
                         return_spritesheet(spritesheet_broly, [455, 172], broly_scale, 4, False, True, (True, False),
                                            1.5),
                         return_spritesheet(spritesheet_broly, [455, 172], broly_scale, 4, False, True, (False, False),
                                            1.5),
                         ]
#bulma
bulma_sprite_list = [return_spritesheet(spritesheet_bulma,[60,85],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,9],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,46],(22,38),4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,46],(22,38),4,False,True,(False,False),1.5),
                         
                         return_spritesheet(spritesheet_bulma,[60,200],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,124],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,162],(22,38),4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_bulma,[60,162],(22,38),4,False,True,(False,False),1.5),
                         ]
#milk
milk_scale = (22,38)
milk_scale_punch = (25,38)
milk_sprite_list = [return_spritesheet(spritesheet_milk,[60,85],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_milk,[60,9],(22,38),4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_milk,[60,46],(22,38),4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_milk,[60,46],(22,38),4,False,True,(False,False),1.5),

                         return_spritesheet(spritesheet_milk,[161,92],milk_scale_punch,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_milk,[157,10],milk_scale_punch,4,False,True,(False,False),1.5),
                         return_spritesheet(spritesheet_milk,[148,51],milk_scale_punch,4,False,True,(True,False),1.5),
                         return_spritesheet(spritesheet_milk,[148,51],milk_scale_punch,4,False,True,(False,False),1.5),
                         ]
#maron
maron_sprite = pygame.image.load('personajes/To npc/Maron.png').convert_alpha()
maron_scale = (22,38)
maron_scale_punch = (24,32)
maron_sprite_list = [
    return_spritesheet(maron_sprite,[314,589],maron_scale,4,False,True,(False,False),1.5),
    return_spritesheet(maron_sprite,[14,589],maron_scale,4,False,True,(False,False),1.5),
    return_spritesheet(maron_sprite,[168,589],maron_scale,4,False,True,(True,False),1.5),
    return_spritesheet(maron_sprite,[168,589],maron_scale,4,False,True,(False,False),1.5),

    return_spritesheet(maron_sprite,[294,47],maron_scale_punch,4,False,True,(False,False),1.5),
    return_spritesheet(maron_sprite,[6,47],maron_scale_punch,4,False,True,(False,False),1.5),
    return_spritesheet(maron_sprite,[150,47],maron_scale_punch,4,False,True,(True,False),1.5),
    return_spritesheet(maron_sprite,[150,47],maron_scale_punch,4,False,True,(False,False),1.5),
]
#luffy 
luffy_sprite = pygame.image.load('personajes/luffy/41187.png')
luffy_scala = (18,18)
luffy_tamaño = 2
luffy_sprite_list = [
    return_spritesheet(luffy_sprite,[2,80],luffy_scala,4,False,True,(False,False),luffy_tamaño),
    return_spritesheet(luffy_sprite,[2,60],luffy_scala,4,False,True,(False,False),luffy_tamaño),
    return_spritesheet(luffy_sprite,[3,120],luffy_scala,4,False,True,(True,False),luffy_tamaño),
    return_spritesheet(luffy_sprite,[3,120],luffy_scala,4,False,True,(False,False),luffy_tamaño),

    return_spritesheet(luffy_sprite,[7,108],luffy_scala,4,False,True,(False,False),1.5),
    return_spritesheet(luffy_sprite,[7,2],luffy_scala,4,False,True,(False,False),1.5),
    return_spritesheet(luffy_sprite,[7,71],luffy_scala,4,False,True,(True,False),1.5),
    return_spritesheet(luffy_sprite,[7,71],luffy_scala,4,False,True,(False,False),1.5),
]
#ki blast
ki_spritesheet = pygame.image.load('skills/main.png')
ki_scale = (16,11)
ki_sprite_list = [
    return_spritesheet(ki_spritesheet,[394,445],ki_scale,4,False,True,(False,False),scala_sprites),
    return_spritesheet(ki_spritesheet,[394,445],ki_scale,4,False,True,(False,False),scala_sprites),
    return_spritesheet(ki_spritesheet,[394,445],ki_scale,4,False,True,(False,False),scala_sprites),
    return_spritesheet(ki_spritesheet,[394,445],ki_scale,4,False,True,(False,False),scala_sprites),
]
"""npc follow posis"""
pasos_broly = {'delay_list':[5,7],'delay_list_inverse':[1,16],'max_delay':90,'posiciones':[(40,420),(160,680),(40,700),(500,370),(300,370)],'index':0,'max_index':4,'specific_index':0,'vel':0.7,
         'vel_npc':5,'random_move':False,'time':0,'max_time':70}

pasos_bulma = {'delay_list':[5,7],'delay_list_inverse':[1,16],'max_delay':90,'posiciones':[(880,600),(1100,600)],'index':0,'max_index':1,'specific_index':0,'vel':0.7,
         'vel_npc':2,'random_move':False,'time':0,'max_time':70}

pasos_milk = {'delay_list':[5,7],'delay_list_inverse':[1,16],'max_delay':90,'posiciones':[(880,100),(1100,100)],'index':0,'max_index':1,'specific_index':0,'vel':0.7,
         'vel_npc':2,'random_move':False,'time':0,'max_time':50}
"""only list"""
index_sprite = 0
index_sprite_enem = 0
list_all_sprites = [goku_sprite_list,piccolo_sprite_list,satan_sprite_list,vegeta_sprite_list]
list_all_sprites_alt = [goku_ssj_sprite_list,piccolo_orange_sprite_list,satan_sprite_list,vegeta_ssg_sprite_list]
list_all_sprites_alt_2 = [goku_UI_sprite_list,piccolo_red_sprite_list,satan_sprite_list,vegeta_MI_sprite_list]
#add

"""functs"""
def get_locs(amount,x,y,bool_list_vert_or_hor,dimensions):
    locs = [(x,y)]
    for i in range(1,amount+1):
        if bool_list_vert_or_hor[0] == True and bool_list_vert_or_hor[1] == False:
            y += dimensions[1]
        elif bool_list_vert_or_hor[0] == False and bool_list_vert_or_hor[1] == True:
            x += dimensions[0]
        locs.append((x,y))
    return locs
def draw_repeated(list_surf,list_pos):
    for surf,pos in zip(list_surf,list_pos):
        screen.blit(surf,pos)
def collide_for_color(color,surface_pos,screen_scale,surface_for_detect,length,dimentions,vel):
    rect = [surface_pos[0],surface_pos[1],dimentions[0],dimentions[1]]

    color_box = Color_box(rect,surface_for_detect,length,[0, 0, screen_scale[0],screen_scale[1]])
    if color_box[0] == color:
        surface_pos[1] += vel
    if color_box[1] == color:
        surface_pos[1] -= vel

    if color_box[2] == color:
        surface_pos[0] += vel
    if color_box[3] == color:
        surface_pos[0] -= vel
def get_rect_list(list_surfs,center_list):
    rects = []
    for surfs,center in zip(list_surfs,center_list):
        rects.append(surfs.get_rect(center=center))
    return rects
def get_color_in_img(img):
    width = img.get_width()
    height = img.get_height()
    colores_unicos = []

    for x in range(width):
        for y in range(height):
            color = img.get_at((x, y))

            if color not in colores_unicos:
                colores_unicos.append(color)
    return colores_unicos
def index_for_angle(dict_ind,pos_surf,pos_cursor):
    angul = round(angle(pos_surf,pos_cursor))
    list_anguls = [90,-90,180,0]
    dict_ind['indice'][0] = indice_numero_mas_cercano(list_anguls,angul)
def create_the_npcs(list_imgs,cantidad,area_pos,area_dimention,vel_tran,vel_move,dimention_surf,max_num_lag,life,max_life,id_map):
    npcs = {'id_map':id_map,'cantidad':cantidad,'list_img': list_imgs,'rect_list':[],'center_rect':[(0,0)],'vel_transition':vel_tran,'vel_move':vel_move,'life_list':life,'max_life':max_life,'vel_recovery':1,'indice':[],'number_change':[],'max_num_change':3,'scale':dimention_surf,'num_lag':0,'max_num_lag':max_num_lag,'sum_index':0,'multiply_index':1,'inmortal_bool':True}
    indice_obtencion = 0
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
def Avatar(screen,npc_dict,up_bool,down_bool,left_bool,right_bool,punch_bool,defense_bool):
    indice = 0
    print(round(npc_dict['number_change'][indice]))
    for pos, index in zip(npc_dict['rect_list'], npc_dict['indice']):
        surf_life = pygame.Surface((npc_dict['life_list'] // 10, npc_dict['life_list'] // 20))
        surf_life.fill((255, 0, 0))
        screen.blit(surf_life, npc_dict['rect_list'][indice])
        screen.blit(npc_dict['list_img'][npc_dict['indice'][indice]+ npc_dict['sum_index'] * npc_dict['multiply_index']][round(npc_dict['number_change'][indice])], npc_dict['rect_list'][indice])
        if up_bool == True:
            npc_dict['indice'][indice] = 0
            npc_dict['rect_list'][indice][1] -= npc_dict['vel_move']
        if down_bool == True:
            npc_dict['indice'][indice] = 1
            npc_dict['rect_list'][indice][1] += npc_dict['vel_move']
        if left_bool == True:
            npc_dict['indice'][indice] = 2
            npc_dict['rect_list'][indice][0] -= npc_dict['vel_move']
        if right_bool == True:
            npc_dict['indice'][indice] = 3
            npc_dict['rect_list'][indice][0] += npc_dict['vel_move']
        """mover multiplicador"""
        if punch_bool == True:
            npc_dict['sum_index'] = 4
        if punch_bool == False:
            npc_dict['sum_index'] = 0
        if defense_bool == True:
            npc_dict['multiply_index'] = 2
        if defense_bool == False:
            npc_dict['multiply_index'] = 1
        """mover frames"""

        if up_bool == True or down_bool == True or left_bool == True or right_bool == True or punch_bool == True:
            npc_dict['number_change'][indice] += npc_dict['vel_transition']

            if round(npc_dict['number_change'][indice]) >= npc_dict['max_num_change']:
                npc_dict['number_change'][indice] = 0
        if up_bool == False and down_bool == False and left_bool == False and right_bool == False and punch_bool == False:
            npc_dict['number_change'][indice] = 0

def Colliderect(rect,rect2):
    hit = Hit_box(rect,rect2,0)
    if hit[0] == True or hit[1] == True or hit[2] == True or hit[3] == True:
        return True
    else:
        return False

def move_npc_for_enemy(screen,npc_dict,npc_dict_2,distancia_mostrar,bool_exist,id_map_current,fight_bool,damage_bool,surf_player_pos):
    indice = indice_punto_mas_cercano(surf_player_pos,npc_dict['rect_list'])
    surf_life = pygame.Surface((npc_dict['life_list']//10,npc_dict['life_list']//20))
    surf_life.fill((255,0,0))
    if npc_dict['inmortal_bool'] == True:
        npc_dict['life_list'] = npc_dict['max_life']
    for pos,index,num_img in zip(npc_dict['rect_list'],npc_dict['indice'],npc_dict['number_change']):

        if id_map_current == npc_dict['id_map']:
            if avistamiento('a',pos,surf_player_pos,distancia_mostrar):
                if bool_exist == True:
                    screen.blit(surf_life,pos)
                    screen.blit(npc_dict['list_img'][index+npc_dict['multiply_index']][round(num_img)],pos)#
            if fight_bool == True:
        
                if damage_bool == True:
                    npc_dict['life_list'] -= npc_dict['vel_move']
                if Colliderect(npc_dict['rect_list'][indice],npc_dict_2['rect_list'][indice]) == True:
                    #print('entroooooooooo')
                    npc_dict['multiply_index'] = 4
                    npc_dict_2['life_list'] -= npc_dict['vel_move']
                else:
                    npc_dict['multiply_index'] = 0
            if avistamiento('a', pos, surf_player_pos, distancia_mostrar//3):
                index_for_angle(npc_dict,npc_dict['rect_list'][indice],surf_player_pos)
                npc_dict['number_change'][indice] += npc_dict['vel_transition']
                if round(npc_dict['number_change'][indice]) >= npc_dict['max_num_change']:
                    npc_dict['number_change'][indice] = 0
                """arriba y abajo"""
                x = indice
                if npc_dict['rect_list'][indice][1] > surf_player_pos[1]:
                    npc_dict['rect_list'][indice][1] -= npc_dict['vel_move']

                elif npc_dict['rect_list'][indice][1] < surf_player_pos[1]:
                    npc_dict['rect_list'][indice][1] += npc_dict['vel_move']
                """left right"""
                if npc_dict['rect_list'][indice][0] > surf_player_pos[0]:
                    npc_dict['rect_list'][indice][0] -= npc_dict['vel_move']
                elif npc_dict['rect_list'][indice][0] < surf_player_pos[0]:
                    npc_dict['rect_list'][indice][0] += npc_dict['vel_move']
            if anti_avistamiento('',pos, surf_player_pos,distancia_mostrar//3):
                npc_dict['number_change'][indice] = 0

def move_npc_for_npc(self,npc_dict,distancia_mostrar):
    valor = random.randint(0,4)
    caminar = random.choice([True,False])
    npc_dict['num_lag'] += round(npc_dict['vel_transition'])
    indice = 0
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
pasos = {'delay_list':[5,7],'delay_list_inverse':[1,16],'max_delay':90,'posiciones':[(40,420),(160,680),(40,700),(500,370),(300,370)],'index':0,'max_index':4,'specific_index':0,'vel':0.7,
         'vel_npc':5,'random_move':False,'time':0,'max_time':70}

def npc_follow(screen,npc_dict,dict_track,per_pos,id_map_current,bool_exist):
    indice = dict_track['specific_index']
    if id_map_current == npc_dict['id_map']:
        if bool_exist == True:
            screen.blit(npc_dict['list_img'][npc_dict['indice'][indice]][round(npc_dict['number_change'][indice])], npc_dict['rect_list'][indice])
    rand = random.randint(0,dict_track['max_delay'])
    if dict_track['random_move'] == True:
        if rand in dict_track['delay_list']:
            if dict_track['index'] <= dict_track['max_index']:
                dict_track['index'] += dict_track['vel']
        if rand in dict_track['delay_list_inverse']:
            if dict_track['index'] >= 0:
                dict_track['index'] -= dict_track['vel']
    if dict_track['random_move'] == False:
        dict_track['time'] += 1
        if dict_track['time'] > dict_track['max_time']:
            dict_track['index'] += dict_track['vel']
            dict_track['time'] = 0
        if dict_track['index'] > dict_track['max_index']:
            dict_track['index'] = 0

    if avistamiento('a',npc_dict['rect_list'][dict_track['specific_index']],dict_track['posiciones'][round(dict_track['index'])],10000):
        npc_dict['number_change'][indice] += npc_dict['vel_transition']
        if npc_dict['number_change'][indice] > npc_dict['max_num_change']:
            npc_dict['number_change'][indice] = 0
        if npc_dict['rect_list'][indice][1] > dict_track['posiciones'][round(dict_track['index'])][1]:
            npc_dict['rect_list'][indice][1] -= dict_track['vel_npc']
            npc_dict['indice'][indice] = 0
        elif npc_dict['rect_list'][indice][1] < dict_track['posiciones'][round(dict_track['index'])][1]:
            npc_dict['rect_list'][indice][1] += dict_track['vel_npc']
            npc_dict['indice'][indice] = 1
        """left right"""
        if npc_dict['rect_list'][indice][0] > dict_track['posiciones'][round(dict_track['index'])][0]:
            npc_dict['rect_list'][indice][0] -= dict_track['vel_npc']
            npc_dict['indice'][indice] = 2
        elif npc_dict['rect_list'][indice][0] < dict_track['posiciones'][round(dict_track['index'])][0]:
            npc_dict['rect_list'][indice][0] += dict_track['vel_npc']
            npc_dict['indice'][indice] = 3

"""interactuar"""
def create_text(cuadro_de_texto,palabras,max_delay,color_text,scale_text,maximo_de_palabras,delay_list,max_time,id_map):
    dicti = {'cuadro':cuadro_de_texto,'palabras':palabras,'delay_list':delay_list,'max_delay':max_delay,'color':color_text,'scale':scale_text,'index':0,'maximo_de_palabras_index':maximo_de_palabras,
             'random_move':False,'time':0,'max_time':max_time,'id_map':id_map}
    return dicti
def hablar(dict,pos_list,personaje_pos,screen):
    indice = indice_punto_mas_cercano(personaje_pos, pos_list)
    rand = random.randint(1,dict['max_delay'])
    rand_text = random.randint(0,dict['maximo_de_palabras_index'])
    texto = dict['palabras'][rand_text]
    #if dict['delay'] > dict['max_delay']:
    #if rand == 5:
    screen.blit(dict['cuadro'],(pos_list[indice][0] - 90,pos_list[indice][1] - 80))
    if dict['random_move'] == True:
        if rand in dict['delay_list']:
            string_blit(texto,(pos_list[indice][0] - 60,pos_list[indice][1] - 50),dict['scale'],dict['color'])
    if dict['random_move'] == False:
        string_blit(dict['palabras'][dict['index']],(pos_list[indice][0] - 60,pos_list[indice][1] - 50),dict['scale'],dict['color'],screen)
        dict['time'] += 1
        if dict['time'] > dict['max_time']:
            dict['index'] += 1
            dict['time'] = 0
        if dict['index'] > dict['maximo_de_palabras_index']:
            dict['index'] = 0
def create_place(screen,dict,dict_map,bool_press,bool_despress,per_pos,id_map):
    if id_map == dict['id']:
        pygame.draw.rect(screen,(255,0,0),dict['place_pos_door'])
        if hover('a',per_pos,(dict['place_pos_door'][0],dict['place_pos_door'][1]),(dict['place_pos_door'][2],dict['place_pos_door'][3])):
            if bool_press == True:
                dict['active'] = True
            if bool_despress == True:
                dict['active'] = False
        if dict['active'] == True:
            dict_map['bool'] = False
            #collide_for_color(p1,dict['color_collision'],per_pos,(dict['place_img'].get_width(),dict['place_img'].get_height()),dict['place_mask_collision'],1,(32,32))
            screen.blit(dict['place_img'],dict['place_pos'])
        if dict['active'] == False:
            dict_map['bool'] = True

#def destruir()
"""xp"""
def Save(dict,nombre_de_json):
    to_py = f'value = {dict}'
    with open(nombre_de_json, "w") as archivo_jsoni:
        archivo_jsoni.write(to_py)
EXP = value
objetos_de_obtencion = ['']
Misiones_list = value_metas

#Exp

def save_xp():
    Save(EXP,'xd.py')
    Save(Misiones_list,'metas_xp.py')    
def obtener_metas(rect_enem,life_enem):
    if p1.s_rect.colliderect(rect_enem) and life_enem <= 1:
        Misiones_list['kills'] += 1
    if p1.moverse['up'] == True or p1.moverse['down'] == True or p1.moverse['left'] == True or p1.moverse['right'] == True:
        Misiones_list['recorrido'] += 1
def use_xp(screen,Exp_dict,bool_sum_xp):
    if bool_sum_xp == True:
        if Exp_dict['xp'] < Exp_dict['max_xp']:
            Exp_dict['escala_barra'][0] += Exp_dict['cantidad']//10
            Exp_dict['xp'] += Exp_dict['cantidad']
    barra_xp = pygame.Surface((Exp_dict['escala_barra']))
    barra_xp.fill(Exp_dict['color_xp'])
    screen.blit(barra_xp,Exp_dict['pos'])
    string_blit(str(Exp_dict['xp']),Exp_dict['pos'],34,(255,255,255),screen)
"""skills"""
def za_warudo():
    print('za_warudo')
    
def yellow_temperance():
    global index_sprite
    p1.vida_value = 500
    index_sprite = index_sprite_enem
def one_punch():
    p1.vida_value = 400
    p1.damage = 50
    """enem.damage = 0"""
def cancel():
    p1.vel_trasicion_img = 0.15
    p1.velocidad = 5
    
def use_skills(pantalla,dict,bool_use):
    """mostrar"""
    pantalla.blit(dict['portada'], dict['portada_pos'])
    string_blit(str(dict['time']),dict['time_pos'],45,(255,0,0),pantalla)

    if bool_use == True:
        dict['bool_atack'] = True
    if dict['bool_atack'] == True:
        dict['damage'] += dict['increase']

        if dict['time'] > 0:
            dict['time'] -= dict['vel_charge']
            dict['function']()
        if dict['delay_damage'] > 0:
            dict['delay_damage'] -= dict['vel_charge']
        if dict['img'] is not None:
            pantalla.blit(dict['img'], dict['img_pos'])

    if dict['time'] < 1:
        cancel()
        dict['bool_atack'] = False
    if dict['bool_atack'] == False:
        p1.vida_value -= dict['damage']
        if dict['time'] < dict['max_time']:
            dict['time'] += dict['vel_charge']



def rotate_surf(surf,cantidad,angulo,scale):
    list_rotate = []
    dicti = {'surf_list':list_rotate,'distance':30,'min_distance':5,'max_distance':300,'vel':5,'alpha':0}
    angle = angulo
    for i in range(1,cantidad+1):
        list_rotate.append(pygame.transform.rotozoom(surf,angle,scale))
        angle += angulo
    return dicti
getsuga = rotate_surf(pygame.image.load('multiverse/effects/getsuga tenshou/getsuga tenshou_2.png').convert_alpha(),13,180,0.2)

def press_button_time(screen,list_num,max_num_random,surf_normal,surf_press_list,pos):
    num = random.randint(0,max_num_random)
    rand = random.randint(0,1)
    if num in list_num:
        screen.blit(surf_press_list[rand],pos)
    else:
        screen.blit(surf_normal, pos)

"""fighter 2d"""
def gravedad(dict,vel_impulso,vel_caida,bool_inpulso,punto_suelo):
    if bool_inpulso == True:
        dict['rect_list'][0][1] -= vel_impulso
    if dict['rect_list'][0][1] < punto_suelo:
        dict['rect_list'][0][1] += vel_caida
    if dict['rect_list'][0][1] > punto_suelo:
        dict['rect_list'][0][1] -= vel_caida

def reject_body(index_body,dict1,dict2,bool_grab):
    up_left = (dict1['rect_list'][index_body][0],dict1['rect_list'][index_body][1])
    up_right = (dict1['rect_list'][index_body][0] + dict1['rect_list'][index_body][2],dict1['rect_list'][index_body][1])
    down_left = (dict1['rect_list'][index_body][0],dict1['rect_list'][index_body][1] + dict1['rect_list'][index_body][3])
    down_right = (dict1['rect_list'][index_body][0] + dict1['rect_list'][index_body][2],dict1['rect_list'][index_body][1] + dict1['rect_list'][index_body][3])
    if hover('x',up_left,dict2['rect_list'][index_body],(dict2['rect_list'][index_body][3],dict2['rect_list'][index_body][3])) == True or hover('x',down_left,dict2['rect_list'][index_body],(dict2['rect_list'][index_body][3],dict2['rect_list'][index_body][3])) == True:
        if bool_grab == False:
            dict1['rect_list'][index_body][0] += dict1['vel']
        if bool_grab == True:
            dict2['rect_list'][index_body][0] += dict2['vel']*3
    if hover('x',up_right,dict2['rect_list'][index_body],(dict2['rect_list'][index_body][3],dict2['rect_list'][index_body][3])) == True or hover('x',down_right,dict2['rect_list'][index_body],(dict2['rect_list'][index_body][3],dict2['rect_list'][index_body][3])) == True:
        if bool_grab == False:
            dict1['rect_list'][index_body][0] -= dict1['vel']
        if bool_grab == True:
            dict2['rect_list'][index_body][0] -= dict2['vel']*3



"""fonts"""
def encontrar_posiciones(palabra, lista):
    posiciones = [i for i, elemento in enumerate(lista) if elemento == palabra]
    return posiciones if posiciones else f"La palabra '{palabra}' no se encuentra en la lista."

def create_text_by_font_img(screen,posiciones,font_imgs,pos_txt):
    for ind_pos in posiciones:
        screen.blit(font_imgs[ind_pos],pos_txt)
        #for pos in pos_txt:
def text_blit_by_far(per_pos,speaker_pos,distance_speak,text_no_far,text_far,id_map_current,bool_exist,screen):
    if bool_exist == True:
        if id_map_current == text_no_far['id_map']:
            if avistamiento('a',per_pos,speaker_pos,distance_speak):
                hablar(text_no_far,[speaker_pos],per_pos,screen)
        if id_map_current == text_far['id_map']:
            if anti_avistamiento('a',per_pos,speaker_pos,distance_speak):
                hablar(text_far, [speaker_pos], per_pos,screen)

"""asignar"""
p1 = player
"""imagenes y colision"""
indice_west_city = 1
west_city_surf_1 = [return_spritesheet(pygame.image.load('map_extended.png').convert_alpha(),[0,0],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_extended.png').convert_alpha(),[0,720],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_extended.png').convert_alpha(),[0,1440],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_extended.png').convert_alpha(),[0,2160],(1280,720),3,False,True,(False,False),1)]

west_city_surf_2 = [return_spritesheet(pygame.image.load('map_copy.png').convert(),[0,0],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy.png').convert(),[0,720],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy.png').convert(),[0,1440],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy.png').convert(),[0,2160],(1280,720),3,False,True,(False,False),1)]

west_city_surf_3 = [return_spritesheet(pygame.image.load('map_copy_transparent_2.png').convert_alpha(),[0,0],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy_transparent_2.png').convert_alpha(),[0,720],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy_transparent_2.png').convert_alpha(),[0,1440],(1280,720),3,False,True,(False,False),1),
                    return_spritesheet(pygame.image.load('map_copy_transparent_2.png').convert_alpha(),[0,2160],(1280,720),3,False,True,(False,False),1)]
west_city = {'surf_normal':west_city_surf_1,'index_x':0,'index_y':0,'max_index_x':2,'max_index_y':3,
             'surf_collide':west_city_surf_2,'surf_alpha':west_city_surf_3}
capsule_corp = {'surf_normal':west_city_surf_1,'index_x':0,'index_y':0,'max_index_x':1,'max_index_y':2,
             'surf_collide':west_city_surf_2,'surf_alpha':west_city_surf_3}

world_map = {'maps':[west_city,capsule_corp],'index':0,'max_index':1}


"""definir algo"""
p1.punch_speed_multiplier = 5
p1.s_rect.x = 400
p1.s_rect.y = 300
map_activates = 'training'
contador_de_salida = 0
"""lugares"""
indice_lugares = 0
lugares = [pygame.image.load('lugares/mini/campo_cuadricula_mini.png').convert(),pygame.image.load('lugares/mini/space_rock_mini.png').convert(),pygame.image.load('lugares/mini/grand_kai_tournament_mini.png').convert(),pygame.image.load('lugares/mini/mini_fondo.jpg').convert()]
#map
mapita = [pygame.image.load('lugares/campo_cuadricula.png').convert(),pygame.image.load('lugares/space_rock.png').convert(),pygame.image.load('lugares/papaya_tournament.png').convert(),pygame.image.load('lugares/fondo.jpg').convert()]
mapita_collision = [pygame.image.load('lugares/isla_kame_collisions.png').convert(),pygame.image.load('lugares/space_rock_collide.png').convert(),pygame.image.load('lugares/papaya_tournament_collide.png').convert(),pygame.image.load('lugares/fondo.jpg').convert()]
mapita_superpos = [pygame.image.load('lugares/isla_kame.png').convert(),pygame.image.load('lugares/papaya_tournament.png').convert(),pygame.image.load('lugares/grand_kai_tournament_2.png').convert(),pygame.image.load('lugares/fondo.jpg').convert()]
"""portadas"""
portraits = [pygame.image.load('portraits/goku.png').convert(),pygame.image.load('portraits/vegeta.png').convert(),
               pygame.image.load('portraits/trunks.png').convert(),pygame.image.load('portraits/piccoro.png').convert(),
             pygame.image.load('portraits/dante.png').convert(),pygame.transform.rotozoom(pygame.image.load('portraits/saitama.png').convert(),0,0.2)]


portrait_modos = [pygame.image.load('mode_titles/training.png').convert_alpha(),pygame.image.load('mode_titles/History.png').convert_alpha(),pygame.image.load('mode_titles/Tournament.png').convert_alpha(),
                  pygame.image.load('mode_titles/Free-battle.png').convert_alpha(),pygame.image.load('mode_titles/SIMULATION.png').convert_alpha(),pygame.image.load('mode_titles/2D-Fight.png').convert_alpha(),pygame.image.load('mode_titles/other.png').convert_alpha()]
ind_mode = 0
modos_string = ['training','history','tournament','free_battle','simulation','2D fight','other']



"""guardar"""
cosas_pa_guardar = {}
def save(name_of_py,list_surfs):
    posis = list_surfs
    to_py = f'value = {posis}'
    with open(name_of_py, "w") as archivo_jsoni:
        archivo_jsoni.write(to_py)






"""npc xd"""

bulma = create_the_npcs(bulma_sprite_list,1,(30,70),(400,400),0.15,2,(32,32),1,300,300,(1,0))
text_bulma_normal = create_text(pygame.transform.rotozoom(pygame.image.load('portraits/text box/normal.png'),0,1),
                           ['...','....'],
                           50,(255,255,255),24,1,[0,5,9,24,7,8],10,(1,0))
text_bulma_nearby = create_text(pygame.transform.rotozoom(pygame.image.load('portraits/text box/emergencia.png'),0,1),
                           ['habla con el'],
                           50,(255,255,255),24,0,[0,5,9,24,7,8],60,(1,0))
#milk
milk = create_the_npcs(milk_sprite_list,1,(30,70),(400,400),0.15,2,(32,32),1,300,300,(1,0))
text_milk_normal = create_text(pygame.transform.rotozoom(pygame.image.load('portraits/text box/normal.png'),0,1),
                           ['...','......'],
                           50,(255,255,255),24,1,[0,5,9,24,7,8],10,(1,0))
text_milk_nearby = create_text(pygame.transform.rotozoom(pygame.image.load('portraits/text box/emergencia.png'),0,1),
                           ['ENTRA YA'],
                           50,(255,255,255),24,0,[0,5,9,24,7,8],60,(1,0))





#npcs
mr_satan = create_the_npcs(satan_sprite_list,1,(850,400),(200,200),0.15,6,(32,32),30,300,300,(3,0))

piccolo = create_the_npcs(piccolo_sprite_list,1,(850,400),(200,200),0.15,1,(32,32),30,300,300,(0,0))

broly = create_the_npcs(broly_sprite_list,1,(850,400),(200,200),0.15,3,(32,32),30,300,300,(3,0))

goku = create_the_npcs(goku_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
goku_log = create_the_npcs(goku_log1_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))

maron = create_the_npcs(maron_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
gogeto = create_the_npcs(gogeto_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
vegito = create_the_npcs(vegito_sprite_list,1,p1.s_rect,p1.s_rect,0.15,7,(32,32),30,300,300,(0,0))
trunks = create_the_npcs(trunks_sprite_list,1,p1.s_rect,p1.s_rect,0.15,7,(32,32),30,300,300,(0,0))

luffy = create_the_npcs(luffy_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
#luffy['max_num_change'] = 2

Npcs = [goku,goku_log,mr_satan,piccolo,broly,milk,bulma,maron,gogeto,vegito,luffy,trunks]

avatar_main = create_the_npcs(goku_yardrat_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))

avatar_free_batle = create_the_npcs(goku_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
clon_free_batle = create_the_npcs(goku_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
ki_blast = create_the_npcs(ki_sprite_list,1,p1.s_rect,p1.s_rect,0.15,15,(32,32),30,300,300,(0,0))

avatar_training = create_the_npcs(goku_sprite_list,1,p1.s_rect,p1.s_rect,0.15,5,(32,32),30,300,300,(0,0))
avatar_enemy = create_the_npcs(goku_sprite_list,1,(900,500),(50,50),0.15,2,(32,32),30,300,300,(0,0))
#avatar_tournament =
e_rect = piccolo_spritesheet.get_rect()
"""colision en db lob"""
def Collide(fighter,enemy,vel,distance,box_map,bool_reject,impulso):
    hit_box = Hit_box([fighter['rect_list'][0][0],fighter['rect_list'][0][1],32,32], 
                      [enemy['rect_list'][0][0],enemy['rect_list'][0][1],
                       32,32],distance)
    #hit_box_of_enem = Hit_box([pos_p2.x,pos_p2.y,32,32],[pos_p1.x,pos_p1.y,32,32],0)
    #no col player
    if bool_reject == False:
        if hit_box[0] == True:
            fighter['rect_list'][0][1] = num_follow(fighter['rect_list'][0][1],box_map[1]+box_map[3],vel)
        if hit_box[1] == True:
            fighter['rect_list'][0][1] = num_follow(fighter['rect_list'][0][1],box_map[1],vel)
        if hit_box[2] == True:
            fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],box_map[0]+box_map[2],vel)
        if hit_box[3] == True:
            fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],box_map[0],vel)
    #col player
    if bool_reject == True:
        if hit_box[1] == True:
            enemy['rect_list'][0][1] = num_follow(enemy['rect_list'][0][1],box_map[1]+box_map[3],impulso)
        if hit_box[0] == True:
            enemy['rect_list'][0][1] = num_follow(enemy['rect_list'][0][1],box_map[1],impulso)
        if hit_box[3] == True:
            enemy['rect_list'][0][0] = num_follow(enemy['rect_list'][0][0],box_map[0]+box_map[2],impulso)
        if hit_box[2] == True:
            enemy['rect_list'][0][0] = num_follow(enemy['rect_list'][0][0],box_map[0],impulso)
    """if hit_box[0] == False and hit_box[1] == False and hit_box[2] == False and hit_box[3] == False:
        Damage.cant = 0
    if hit_box[0] == True or hit_box[1] == True or hit_box[2] == True or hit_box[3] == True:
        Damage.cant = 100"""
def Ultra_instinc(bool_dodge,fighter,enemy,distance,vel,box_map):
    hit_box = Hit_box([fighter['rect_list'][0][0],fighter['rect_list'][0][1],32,32],
                      [enemy['rect_list'][0][0],enemy['rect_list'][0][1],32,32],distance)
    if bool_dodge == True:
        index_for_angle(fighter,fighter['rect_list'][0],enemy['rect_list'][0])

        if hit_box[1] == True:
            fighter['rect_list'][0][1] = num_follow(fighter['rect_list'][0][1],box_map[1]+box_map[3],vel)
        if hit_box[0] == True:
            fighter['rect_list'][0][1] = num_follow(fighter['rect_list'][0][1],box_map[1],vel)
        if hit_box[3] == True:
            fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],box_map[0]+box_map[2],vel)
        if hit_box[2] == True:
            fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],box_map[0],vel)
def domain_expansion(screen,pos_begin,dimentions,pos_intruder):
    surf = pygame.Surface(dimentions)
    surf.fill((255,0,0))
    pos_zone = [pos_begin[0]-dimentions[0]/2,pos_begin[1]-dimentions[1]/2,dimentions[0],dimentions[1]]
    #screen.blit(surf,pos_zone)
    return Hover(pos_intruder,pos_zone)
def Reiatsu(bool_reiatsu,bool_zone_active,avatar_dict,dicti,power,limits_zone_rect):
    if bool_reiatsu == True:
        if bool_zone_active == True:
            #x
            if dicti['rect_list'][0][0] < avatar_dict['rect_list'][0][0]:
                dicti['rect_list'][0][0] = num_follow(dicti['rect_list'][0][0],limits_zone_rect[0],power)
            if dicti['rect_list'][0][0] > avatar_dict['rect_list'][0][0]:
                dicti['rect_list'][0][0] = num_follow(dicti['rect_list'][0][0],limits_zone_rect[2],power)
            #y
            if dicti['rect_list'][0][1] < avatar_dict['rect_list'][0][1]:
                dicti['rect_list'][0][1] = num_follow(dicti['rect_list'][0][1],limits_zone_rect[1],power)
            if dicti['rect_list'][0][1] > avatar_dict['rect_list'][0][1]:
                dicti['rect_list'][0][1] = num_follow(dicti['rect_list'][0][1],limits_zone_rect[3],power)
def Blue(bool_blue,dicti,avatar_dict,power):
    if bool_blue == True:
        #x
        if dicti['rect_list'][0][0] < avatar_dict['rect_list'][0][0] or dicti['rect_list'][0][0] > avatar_dict['rect_list'][0][0]:
            dicti['rect_list'][0][0] = num_follow(dicti['rect_list'][0][0],avatar_dict['rect_list'][0][0],power)
        #y
        if dicti['rect_list'][0][1] < avatar_dict['rect_list'][0][1] or  dicti['rect_list'][0][1] > avatar_dict['rect_list'][0][1]:
            dicti['rect_list'][0][1] = num_follow(dicti['rect_list'][0][1],avatar_dict['rect_list'][0][1],power)
def Rinegan(bool_rin,dict_avatar,dict_enemy):
    if bool_rin == True:
        print(dict_avatar['rect_list'][0])
        distancia = (math.sqrt(((dict_enemy['rect_list'][0][0] - dict_avatar['rect_list'][0][0]) ** 2) + ((dict_enemy['rect_list'][0][1] - dict_avatar['rect_list'][0][1]) ** 2)))
        #avatar
        dict_avatar['rect_list'][0][0] = num_follow(dict_avatar['rect_list'][0][0],dict_enemy['rect_list'][0][0],distancia)
        dict_avatar['rect_list'][0][1] = num_follow(dict_avatar['rect_list'][0][1],dict_enemy['rect_list'][0][1],distancia)
        #enemy
        dict_enemy['rect_list'][0][0] = num_follow(dict_enemy['rect_list'][0][0],dict_avatar['rect_list'][0][0],distancia)
        dict_enemy['rect_list'][0][1] = num_follow(dict_enemy['rect_list'][0][1],dict_avatar['rect_list'][0][1],distancia)
def Shunpo(Dict_avatar,bool_shunpo,Dict_aim):
    distancia = (math.sqrt(((Dict_aim['rect_list'][0][0] - Dict_avatar['rect_list'][0][0]) ** 2) + ((Dict_aim['rect_list'][0][1] - Dict_avatar['rect_list'][0][1]) ** 2)))
    print(distancia)
    if bool_shunpo == True:
        Dict_avatar['rect_list'][0][0] = num_follow(Dict_avatar['rect_list'][0][0],Dict_aim['rect_list'][0][0],distancia)
        Dict_avatar['rect_list'][0][1] = num_follow(Dict_avatar['rect_list'][0][1],Dict_aim['rect_list'][0][1],distancia)

def collide_2d_fighter(fighter,enemy,vel,distance):
    hit_box = Hit_box([fighter['rect_list'][0][0],fighter['rect_list'][0][1],32,32],
                      [enemy['rect_list'][0][0],enemy['rect_list'][0][1],
                       32,32],5)
    #hit_box_of_enem = Hit_box([pos_p2.x,pos_p2.y,32,32],[pos_p1.x,pos_p1.y,32,32],0)
    #col player
    if hit_box[2] == True:
        fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],1000,vel)
    if hit_box[3] == True:
        fighter['rect_list'][0][0] = num_follow(fighter['rect_list'][0][0],0,vel)
    #no col player
    """if hit_box[0] == False and hit_box[1] == False and hit_box[2] == False and hit_box[3] == False:
        Damage.cant = 0
    if hit_box[0] == True or hit_box[1] == True or hit_box[2] == True or hit_box[3] == True:
        Damage.cant = 100"""
"""personajes para un 2d fighter"""
saitama_hero_spritesheet = pygame.image.load('personajes estilo sf/saitama.png')
saitama_scale = (35,70)
saitama_scale_walk = (39,65)
saitama_scale_girar = (40,71)
#saitama_background = obtain_color_in_img(pygame.image.load('color_database/verde/symbolism-of-green.jpg'))
saitama_2d_fighter = create_the_npcs([return_spritesheet(saitama_hero_spritesheet,[39,8],saitama_scale_walk,8,False,True,(False,False),1.5),
                         return_spritesheet(saitama_hero_spritesheet,[39,8],saitama_scale_walk,8,False,True,(False,False),1.5),
                         return_spritesheet(saitama_hero_spritesheet,[0,83],saitama_scale_walk,8,False,True,(True,False),1.5),
                         return_spritesheet(saitama_hero_spritesheet,[0,83],saitama_scale_walk,8,False,True,(False,False),1.5),

                                      return_spritesheet(saitama_hero_spritesheet, [209, 2115], saitama_scale, 8, False,
                                                         True, (False, False), 1.5),
                                      return_spritesheet(saitama_hero_spritesheet, [209, 2115], saitama_scale, 8, False,
                                                         True, (False, False), 1.5),
                                      return_spritesheet(saitama_hero_spritesheet, [0, 1161], saitama_scale_girar, 8, False,
                                                         True, (True, False), 1.5),
                                      return_spritesheet(saitama_hero_spritesheet, [0, 1161], saitama_scale_girar, 8, False,
                                                         True, (False, False), 1.5)
                                      ],
                                     1,(200,400),(4,4),0.10,5,(23,63),50,300,320,(0,0))
saitama_2d_fighter['max_num_change'] = 8

luffy_spritesheet = pygame.image.load('personajes estilo sf/luffy.png').convert_alpha()
luffy_scale = (50,50)
luffy_scale_walk = (54,50)
luffy_scale_hop = (49,60)
luffy_scale_especial = (38,50)
#luffy_background = obtain_color_in_img(pygame.image.load('personajes estilo sf/backgrounds/luffy.png'))
luffy_2d_fighter = create_the_npcs([return_spritesheet(luffy_spritesheet,[24,563],luffy_scale_hop,8,False,True,(False,False),1.5),
                         return_spritesheet(luffy_spritesheet,[62,875],luffy_scale_hop,8,False,False,(False,False),1.5),
                         return_spritesheet(luffy_spritesheet,[0,287],luffy_scale_walk,8,False,True,(False,False),1.5),
                         return_spritesheet(luffy_spritesheet,[0,287],luffy_scale_walk,8,False,True,(True,False),1.5),

                                    return_spritesheet(luffy_spritesheet, [78, 4862], luffy_scale_especial, 8, False, True,
                                                       (False, False), 1.5),
                                    return_spritesheet(luffy_spritesheet, [78, 4862], luffy_scale_especial, 8, False, True,
                                                       (False, False), 1.5),
                                    return_spritesheet(luffy_spritesheet, [78, 4862], luffy_scale_especial, 8, False, True,
                                                       (True, False), 1.5),
                                    return_spritesheet(luffy_spritesheet, [78, 4862], luffy_scale_especial, 8, False, True,
                                                       (False, False), 1.5)
                                    ],
                                     1,(200,400),(4,4),0.15,2,(23,63),50,300,320,(0,0))
luffy_2d_fighter['max_num_change'] = 8

#goku
goku_supersonic_spritesheet = pygame.image.load('personajes estilo sf\Game Boy Advance - Dragon Ball Z Supersonic Warriors - Goku.png')
goku_supersonic_scale = (61,70)
goku_supersonic_scale_move = (94,60)
goku_supersonic_sprite_list = [
    return_spritesheet(goku_supersonic_spritesheet,[0,1632],goku_supersonic_scale_move,4,False,True,(False,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[0,1632],goku_supersonic_scale_move,4,False,False,(False,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[0,1632],goku_supersonic_scale_move,4,False,True,(True,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[0,1632],goku_supersonic_scale_move,4,False,True,(False,False),1.5),

    return_spritesheet(goku_supersonic_spritesheet,[88,1020],goku_supersonic_scale,4,False,True,(False,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[88,1020],goku_supersonic_scale,4,False,False,(False,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[88,1020],goku_supersonic_scale,4,False,True,(True,False),1.5),
    return_spritesheet(goku_supersonic_spritesheet,[88,1020],goku_supersonic_scale,4,False,True,(False,False),1.5),
]
goku_supersonic_warriors = create_the_npcs(goku_supersonic_sprite_list,1,(200,400),(100,200),0.20,5,(23,63),50,300,300,(0,0))


"""personajes"""
g = get_locs(3,0,0,(True,False),(20,30))
the_npc_0 = create_the_npcs(goku_sprite_list,5,(0,0),(500,670),2,5,(32,32),40,200,300,(0,0))

"""worlds"""
worlds = {}
"""valores guardados"""
#fonts
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
font_custom = [pygame.image.load('fonts/A-B-C-D-E-F-G-H-I-J-K-L-.png').convert_alpha()]
font_1 = return_spritesheet(font_custom[0],[7,0],(59,60),25,False,True,(False,False),1)
palabra_list = ['d','b']
posicion_de_las_letras = get_locs(5,500,0,(False,True),(32,32))
maximo = encontrar_maximo_de_elementos(palabra_list)
posiciones_b = [encontrar_posiciones(palabra_list[i],abc)for i in range(0,maximo)]
#buttons press time
button_press = [pygame.image.load('botones/press_1.png'),pygame.image.load('botones/press_2.png')]
button_no_press = pygame.image.load('botones/no_press.png')
#text
texto_normal = create_text(pygame.transform.rotozoom(pygame.image.load('multiverse/cuadros de texto/cuadro_1.png'),0,0.1),
                           ['Ora','ora','inutil','bastardo'],
                           50,(0,0,0),24,3,[0,5,9,24,7,8],60,(0,0))
#zones
tienda_de_antiguedades = {'id':(2,0),'place_img':pygame.image.load('places/restaurant/159967 (1).png'),'place_pos':[850,460],'place_pos_door':pygame.Rect([950,630],(40,60)),
                          'door_color_detect':(0,255,0),
                          'place_mask_collision':pygame.image.load('places/restaurant/mask.png'),'color_collision':(255,0,0),
                          'active':False,'num_press':0,'max_num_press':200}
tienda_electrónica = {'id':(2,0),'place_img':pygame.image.load('places/tienda electronica/159966.png'),'place_pos':[380,-20],'place_pos_door':pygame.Rect([433,206],(40,60)),
                          'door_color_detect':(0,255,0),
                          'place_mask_collision':pygame.image.load('places/restaurant/mask.png'),'color_collision':(255,0,0),
                          'active':False,'num_press':0,'max_num_press':200}
bulma_room = {'id':(1,0),'place_img':pygame.image.load('places/capsule corp/capsule_corp_bulma_room.png'),'place_pos':[140,160],'place_pos_door':pygame.Rect([270,440],(40,30)),
                          'door_color_detect':(0,255,0),
                          'place_mask_collision':pygame.image.load('places/restaurant/mask.png'),'color_collision':(255,0,0),
                          'active':False,'num_press':0,'max_num_press':200}
#skills
za_warudo_skill = {'img':None,'img_pos':(0,0),'portada':pygame.transform.scale(pygame.image.load('portraits/stands/THE-WORLD_2.png'),(150,30)),
                   'portada_pos':(20,120),'damage':200,'increase':5,'time':300,'max_time':300,'time_pos':[20,200],
                   'vel_charge':1,'delay_damage':300,'function':za_warudo,'bool_atack':False}
crazy_diamond = {'img':None,'img_pos':(0,0),'portada':pygame.transform.rotozoom(pygame.image.load('portraits/stands/THE-WORLD_2.png'),0,0.5),
                 'portada_pos':(20,120),'damage':200,'increase':5,'time':300,'max_time':300,'time_pos':[20,200],
                   'vel_charge':1,'delay_damage':300,'function':za_warudo,'bool_atack':False}
yellow_temperance = {'img':None,'img_pos':(0,0),'portada':pygame.transform.rotozoom(pygame.image.load('portraits/stands/yellow-temperance.png'),0,0.5),
                     'portada_pos':(20,120),'damage':200,'increase':5,'time':300,'max_time':300,'time_pos':[20,200],
                   'vel_charge':1,'delay_damage':300,'function':yellow_temperance,'bool_atack':False}
One_punch = {'img':None,'img_pos':(0,0),'portada':pygame.transform.rotozoom(pygame.image.load('portraits/stands/ONE-PUNCH-MAN.png'),0,0.5),
                     'portada_pos':(20,120),'damage':200,'increase':5,'time':300,'max_time':3000000,'time_pos':[20,200],
                   'vel_charge':100,'delay_damage':300,'function':one_punch,'bool_atack':False}

skills = {'skills':[za_warudo_skill,yellow_temperance,One_punch],'index':0,'max_index':2}
#swords
nozarashi = {'img':pygame.transform.rotozoom(pygame.image.load('multiverse/objects/zaraki_kenpachis_zanpakuto.png').convert_alpha(),0,0.2),'vel':20,
             'distance':30,'min_distance':30,'max_distance':300}
#efectos
tamaño_effect = 0.2
cantidad_getsuga_tenshou = 3
effect_Tsukiyubi = {'surf_list':[charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,90),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,270),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,180),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,360),

                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_', 3, '.png', tamaño_effect, 360),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_', 3, '.png', tamaño_effect, 180),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_', 3, '.png', tamaño_effect, 90),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_', 3, '.png', tamaño_effect, 270),

                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,90),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,180),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,270),
                              charge_img('multiverse/effects/getsuga tenshou/getsuga tenshou_',3,'.png',tamaño_effect,360)
                              ],
                              'max_frames':1,'alpha':0,'vel':30,
                    'distance':30,'min_distance':50,'max_distance':300,
                    }
#Sounds
Sounds = ["AUDIOS DE P78\A.wav","AUDIOS DE P78\B.wav","AUDIOS DE P78\K.wav"]
palabras_sound = ['a','b','c']
Sound_A = {'palabra':palabras_sound,'max_palabra':encontrar_maximo_de_elementos(Sounds)-1,'vel':0.03,'index':0}

clock_1 = {'num':0,'max':60,'vel':1,'time_perfect_range':[10,20]}
def the_clock(clock):
    print(clock['num'])
    if clock['num'] < clock['max']:
        clock['num'] += clock['vel']
    if clock['num'] == clock['max']:
        clock['num'] = 0

    if clock['num'] in range(clock['time_perfect_range'][0],clock['time_perfect_range'][1]):
        return True
    if clock['num'] != clock['time_perfect_range']:
        return False
def Play_sound(bool_play,dict):
    
    if bool_play == True:
        print(palabras_sound[round(dict['index'])])
        indice = encontrar_posiciones(palabras_sound[round(dict['index'])],abc)[0]
        Sounds[indice].set_volume(0.5)
        # get a channel to play the sound
        channel = pygame.mixer.find_channel(True) # should always find a channel
        channel.play(Sounds[indice])
        if isinstance(dict['index'], int):
            Sounds[indice].play()
    if bool_play == False:
        dict['index'] = 0
"""cinematic"""  
"""Aura"""
Aura_kaioken_sprite = pygame.image.load('auras/ki_charge_spritesheet_kaioken.png').convert_alpha()
Aura_ui_sprite = pygame.image.load('auras/ki_charge_spritesheet_ui.png').convert_alpha()
video_Aura_kaioken = {'video_frames':return_spritesheet(Aura_kaioken_sprite,[0,0],[49,35],3,False,True,(False,False),2),'max_frames':2,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.6,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
video_Aura_ui = {'video_frames':return_spritesheet(Aura_ui_sprite,[0,0],[49,35],3,False,True,(False,False),2),'max_frames':2,
                   'sound':'videos/sonido/bishoujo_ghostface.ogg','vel':0.6,'indice':0,'pos':(0,0),
                   'bool_pause':False
                   }
def cinematic_1(screen,npc_1,npc_2,distance,):
    screen.fill((255,0,0))
    print(npc_2['rect_list'][0])
    print(npc_1['rect_list'][0])
    move_npc_for_enemy(screen,npc_1,npc_2,distance,True,(0,0),True,True,npc_2['rect_list'][0])
    move_npc_for_enemy(screen,npc_2,npc_1,distance,True,(0,0),True,True,npc_1['rect_list'][0])
    Collide(npc_1,npc_2,5,0,[0,0,1280,720],True,random.choice([30,60,90]))
    Collide(npc_2,npc_1,5,0,[0,0,1280,720],True,random.choice([20,40,60]))
    if random.choice([False,True]) == True:
        npc_2['rect_list'][0][0] = num_follow(npc_2['rect_list'][0][0],random.randint(0,1280),random.randint(100,200))
        npc_2['rect_list'][0][1] = num_follow(npc_2['rect_list'][0][1],random.randint(0,1280),random.randint(100,200))
    if random.choice([False,True]) == True:
        npc_1['rect_list'][0][0] = num_follow(npc_1['rect_list'][0][0],random.randint(0,1280),random.randint(100,200))
        npc_1['rect_list'][0][1] = num_follow(npc_1['rect_list'][0][1],random.randint(0,1280),random.randint(100,200))
    if random.choice([False,True]) == True:
        npc_1['rect_list'][0][0] = num_follow(npc_1['rect_list'][0][0],npc_2['rect_list'][0][0],random.randint(100,200))
        npc_1['rect_list'][0][1] = num_follow(npc_1['rect_list'][0][1],npc_2['rect_list'][0][1],random.randint(100,200))
        npc_2['rect_list'][0][0] = num_follow(npc_2['rect_list'][0][0],npc_1['rect_list'][0][0],random.randint(100,200))
        npc_2['rect_list'][0][1] = num_follow(npc_2['rect_list'][0][1],npc_1['rect_list'][0][0],random.randint(100,200))


npc_simulation_1 = create_the_npcs(gogeto_sprite_list,1,(200,400),(4,4),0.10,5,(23,63),50,300,320,(0,0))
npc_simulation_2 = create_the_npcs(vegito_sprite_list,1,(200,400),(4,4),0.10,7,(23,63),50,300,320,(0,0))

"""items"""
dragonballs_spritesheet = pygame.image.load('item/53872.png')
dragonballs = return_spritesheet(dragonballs_spritesheet,[42,72],(17,15),7,False,True,(False,False),1.5)

def create_items(screen,img_objs,pos,xp_for_index,amount_to_index,max):
    index = 0
    if round(xp_for_index/amount_to_index) < max:
        index = round(xp_for_index/amount_to_index)
    if round(xp_for_index/amount_to_index) >= max:
        index = max 
    print(index)
    screen.blit(img_objs[index],pos)

#botones
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
    if index_sprite < encontrar_maximo_de_elementos(list_all_sprites) - 1:
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
    if index_sprite_enem < encontrar_maximo_de_elementos(list_all_sprites) - 1:
        index_sprite_enem += vel_ind

def sum_characters():
    global index_character 
    if index_character < encontrar_maximo_de_elementos(characters) - 1:
        index_character += vel_ind
def res_characters():
    global index_character 
    if index_character > - 1:
        index_character -= vel_ind

def sum_index_mode():
    global ind_mode
    if ind_mode < 6:
        ind_mode += vel_ind
def res_index_mode():
    global ind_mode
    if ind_mode > -1:
        ind_mode -= vel_ind



def sum_index_pantalla():
    global index_pantalla
    if index_pantalla < 1:
        index_pantalla += vel_ind
def res_index_pantalla():
    global index_pantalla
    if index_pantalla > -1:
        index_pantalla -= vel_ind

def res_skills_index():
    if skills['index'] > -1:
        skills['index'] -= vel_ind
def sum_skills_index():
    if skills['index'] < skills['max_index']:
        skills['index'] += vel_ind

"""active"""
def active_menu():
    menu.active = True
def desactive_menu():
    menu.active = False

def pause_sound_and_video():
    vid['bool_pause'] = True
def despause_sound_and_video():
    vid['bool_pause'] = False

button_sum_lugares = {'escala': (32, 32),'pos':(1100,500), 'color': (240, 240, 240),'color_hover':(255,50,40),
                      'string':'+','string_scale':40,'string_color':(255,255,255),
                      'funcion':sumar_indice_lugares}
button_res_lugares = {'escala': (32, 32),'pos':(1000,500), 'color': (240, 240, 240),'color_hover':(255,50,40),
                      'string':'-', 'string_scale':40,'string_color':(255,255,255),
                      'funcion':restar_indice_lugares}

button_sum_index_sprite = {'escala': (32, 32),'pos':(100,0), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':suma_index_sprite}
button_res_index_sprite = {'escala': (32, 32),'pos':(0,0), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':resta_index_sprites}

button_res_index_sprite_enem = {'escala': (32, 32),'pos':(1140,0), 'color': (255, 0, 0),'color_hover':(255,50,40),
                                'string':'-','string_scale':40,'string_color':(255,255,255),
                                'funcion':resta_index_sprites_enem}
button_sum_index_sprite_enem = {'escala': (32, 32),'pos':(1240,0), 'color': (255, 0, 0),'color_hover':(255,50,40),
                                'string':'+','string_scale':40,'string_color':(255,255,255),
                                'funcion':suma_index_sprite_enem}

button_sum_index_mode = {'escala': (32, 32),'pos':(720,300), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':sum_index_mode}
button_res_index_mode = {'escala': (32, 32),'pos':(450,300), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':res_index_mode}
button_pause = {'escala': (32, 32),'pos':(0,300), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'P','string_scale':40,'string_color':(255,255,255),
                           'funcion':pause_sound_and_video}
button_despause = {'escala': (32, 32),'pos':(0,340), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'D','string_scale':40,'string_color':(255,255,255),
                           'funcion':despause_sound_and_video}
button_sum_ind_screen = {'escala': (32, 32),'pos':(1000,600), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'>','string_scale':40,'string_color':(255,255,255),
                           'funcion':sum_index_pantalla}
button_res_ind_screen = {'escala': (32, 32),'pos':(1100,600), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'<','string_scale':40,'string_color':(255,255,255),
                           'funcion':res_index_pantalla}
""""""
button_sum_ind_skills = {'escala': (32, 32),'pos':(80,150), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':sum_skills_index}
button_res_ind_skills = {'escala': (32, 32),'pos':(40,150), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':res_skills_index}
"""button menu"""
button_desactive_menu = {'escala': (200, 200),'pos':(500,300), 'color': (255, 255, 0),'color_hover':(255,50,40),
                           'string':'New','string_scale':40,'string_color':(0,0,0),
                           'funcion':desactive_menu}
button_active_menu = {'escala': (50, 50),'pos':(1230,670), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'on','string_scale':30,'string_color':(255,255,255),
                           'funcion':active_menu}
"""button character"""
button_sum_character = {'escala': (32, 32),'pos':(80,150), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'+','string_scale':40,'string_color':(255,255,255),
                           'funcion':sum_characters}
button_res_character = {'escala': (32, 32),'pos':(40,150), 'color': (255, 0, 0),'color_hover':(255,50,40),
                           'string':'-','string_scale':40,'string_color':(255,255,255),
                           'funcion':res_characters}
"""save"""
button_save = {'escala': (50, 50),'pos':(1230,470), 'color': (0, 0, 0),'color_hover':(255,50,40),
                           'string':'save','string_scale':30,'string_color':(255,255,255),
                           'funcion':save_xp}

#vid values
videos = [video_ghostface,video_bleach,video_goku_sad,
          video_saitama_meme,video_dante_dr_fauss]
index_video = 1
vid = videos[index_video]
#map
collision_in_the_map = {'bool':True}
collide_bool = {'bool':False}
ubis_in_map = [tienda_de_antiguedades['place_pos'],tienda_de_antiguedades['place_pos_door']]

def move_map(self):

    global contador_de_salida,indice_west_city,west_city,index_sprite,pantalla,lista_img,lista_img_enem,e_rect
    pantalla = lista_de_pantalla[round(index_pantalla)]
    map_activates = modos_string[round(ind_mode)]
    cont_round = round(contador_de_salida)
    #mouse pos
    #print(pygame.mouse.get_pos(), 'mouse')
    """p1"""
    lista_img = list_all_sprites[round(index_sprite)]
    lista_img_enem = list_all_sprites[round(index_sprite_enem)]

    lista_img_alt = list_all_sprites_alt[round(index_sprite)]
    #lista_img_enem_alt = list_all_sprites_alt[round(index_sprite_enem)]

    lista_img_alt_2 = list_all_sprites_alt_2[round(index_sprite)]
    #lista_img_enem_alt_2 = list_all_sprites_alt_2[round(index_sprite_enem)]
    """maps"""
    id_map_current = (west_city['index_y'], west_city['index_x'])
    if map_activates == 'free_battle':
        """screen"""
        lugar_actual = mapita[round(indice_lugares)]
        """screen"""
        screen.blit(lugar_actual, (0, 0))
        """list img"""
        avatar_enemy['list_img'] = lista_img_enem
        if p1.moverse['kekkai'] == False and p1.moverse['charge'] == False:
            avatar_free_batle['list_img'] = lista_img
        if p1.moverse['kekkai'] == True:
            avatar_free_batle['list_img'] = lista_img_alt
        if p1.moverse['grab'] == True:
            move_npc_for_enemy(screen,ki_blast,avatar_enemy,2000,True,(0,0),False,pygame.mouse.get_pressed()[0],avatar_enemy['rect_list'][0])
        if p1.moverse['esp'] == True:
            move_npc_for_enemy(screen,clon_free_batle,avatar_enemy,2000,True,(0,0),False,pygame.mouse.get_pressed()[0],avatar_enemy['rect_list'][0])
            
            
        
        Avatar(screen, avatar_free_batle, p1.moverse['up'], p1.moverse['down'], p1.moverse['left'], p1.moverse['right'],pygame.mouse.get_pressed()[0], False)
        lista_rects_colision = [[0,0,1280,720],[480,150,200,220],[514,258,250, 230],[0,0,1280,720]]
        Reiatsu(p1.moverse['kekkai'],domain_expansion(screen,avatar_free_batle['rect_list'][0],(200,200),avatar_enemy['rect_list'][0]),
                    avatar_free_batle,
                    avatar_enemy,
                    1.4,
                    [0,0,7000,7000])
        Shunpo(avatar_free_batle,p1.moverse['shunpo'],avatar_enemy)
        Blue(p1.moverse['ki_blast'],avatar_enemy,avatar_free_batle,6)
        Rinegan(p1.moverse['esp_2'],avatar_free_batle,avatar_enemy)
        Ultra_instinc(p1.moverse['charge'],avatar_free_batle,avatar_enemy,5,100,lista_rects_colision[round(indice_lugares)])

        move_npc_for_enemy(screen,avatar_enemy,avatar_free_batle,2000,True,(0,0),True,pygame.mouse.get_pressed()[0],avatar_free_batle['rect_list'][0])

        create_button(screen, button_sum_index_sprite, pygame.mouse.get_pressed()[2])
        create_button(screen, button_res_index_sprite, pygame.mouse.get_pressed()[2])

        create_button(screen, button_res_index_sprite_enem, pygame.mouse.get_pressed()[2])
        create_button(screen, button_sum_index_sprite_enem, pygame.mouse.get_pressed()[2])
        
        #screen.blit(portraits[round(index_sprite)], (35, 0))
        #screen.blit(portraits[round(index_sprite_enem)], (1175, 0))

        

        if p1.moverse['charge'] == True:
            avatar_free_batle['list_img'] = lista_img_alt_2
            video_Aura_ui['pos'] = [avatar_free_batle['rect_list'][0][0]-25,avatar_free_batle['rect_list'][0][1]-15]
            blit_video(screen,video_Aura_ui)
        if p1.moverse['kekkai'] == True:
            video_Aura_kaioken['pos'] = [avatar_free_batle['rect_list'][0][0]-25,avatar_free_batle['rect_list'][0][1]-15]
            blit_video(screen,video_Aura_kaioken)
        """collide"""
        Collide(avatar_free_batle,avatar_enemy,5,1,lista_rects_colision[round(indice_lugares)],pygame.mouse.get_pressed()[0],100)
        Collide(avatar_enemy,avatar_free_batle,5,0,lista_rects_colision[round(indice_lugares)],False,20)
        collide_for_color((255,0,0),p1.s_rect,(1280,720),mapita_collision[round(indice_lugares)],1,(32,32),10)

        create_button(screen, button_res_lugares, pygame.mouse.get_pressed()[0])
        create_button(screen, button_sum_lugares, pygame.mouse.get_pressed()[0])

        """mostrar lugar"""
        lugar_actual = lugares[round(indice_lugares)]
        screen.blit(lugar_actual, (1020, 600))

    elif map_activates == 'tournament':
        #blit map
        screen.blit(mapita[2],(0,0))

        Avatar(screen,mr_satan,p1.moverse['up'],p1.moverse['down'],p1.moverse['left'],p1.moverse['right'],pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[2])
        move_npc_for_enemy(screen,piccolo,mr_satan,2000,True,(0,0),True,pygame.mouse.get_pressed()[0],mr_satan['rect_list'][0])
        e_rect = mr_satan['rect_list'][0]
        Collide(mr_satan,piccolo,5,0,[0,0,1280,720],False,20)
        """salir del escenario"""
        if antihover(250, 252, (514, 258), mr_satan['rect_list'][0]):
            contador_de_salida += 0.3
            string_blit(str(cont_round), (0, 0), 40, (255, 0,0),screen)
        elif antihover(250, 252, (514, 258), piccolo['rect_list'][0]):
            contador_de_salida += 0.3
            string_blit(str(cont_round), (0, 0), 40, (255, 0,0),screen)
        else:
            contador_de_salida = 0
        if contador_de_salida > 10:
            mr_satan['rect_list'][0][0],mr_satan['rect_list'][0][1] = 520,400
            piccolo['rect_list'][0][0],piccolo['rect_list'][0][1] = 620,400
            contador_de_salida = 0
    elif map_activates == 'history':
        
        screen.fill((0,random.randint(148,150),random.randint(253,255)))
        rect = avatar_main['rect_list'][0]
        
        obtener_metas([0,0,9,9],[0,0,0,0])

        screen.blit(west_city['surf_normal'][west_city['index_y']][west_city['index_x']],(0,0))
        use_xp(screen,EXP,pygame.mouse.get_pressed()[0])
        create_items(screen,dragonballs,(0,0),value['xp'],100,6)

        create_place(screen, tienda_de_antiguedades, collision_in_the_map, pygame.mouse.get_pressed()[0],
                     pygame.mouse.get_pressed()[2], rect,(west_city['index_y'],west_city['index_x']))
        create_place(screen, tienda_electrónica, collision_in_the_map, pygame.mouse.get_pressed()[0],
                     pygame.mouse.get_pressed()[2], rect, (west_city['index_y'], west_city['index_x']))
        create_place(screen, bulma_room, collision_in_the_map, pygame.mouse.get_pressed()[0],
                     pygame.mouse.get_pressed()[2], rect, (west_city['index_y'], west_city['index_x']))
        print(pygame.mouse.get_pos(),'mouse')
        """button"""
        """create_button(screen, button_sum_index_sprite, pygame.mouse.get_pressed()[0])
        create_button(screen, button_res_index_sprite, pygame.mouse.get_pressed()[0])

        create_button(screen,button_res_index_sprite_enem,pygame.mouse.get_pressed()[0])
        create_button(screen,button_sum_index_sprite_enem,pygame.mouse.get_pressed()[0])"""

        #create_button(screen, button_res_ind_skills, pygame.mouse.get_pressed()[0])
        #create_button(screen, button_sum_ind_skills, pygame.mouse.get_pressed()[0])

        #screen.blit(portraits[round(index_sprite)],(35,0))
        #use_skills(screen,skills['skills'][round(skills['index'])],pygame.mouse.get_pressed()[2])
        for rect_list in the_npc_0['rect_list']:
            rex = [rect,rect_list]
            for rects in rex:
                if collision_in_the_map['bool'] == True:
                    for color in [(248,0,0)]:
                        collide_for_color(color,rects,(1200,600),west_city['surf_collide'][west_city['index_y']][west_city['index_x']],1,(32,32),10)
        for npcs in [broly,bulma,milk]:
            Collide(avatar_main,npcs,5,0,[0,0,1280,720],pygame.mouse.get_pressed()[0],20)
        move_npc_for_enemy(screen,broly,avatar_main,1000,True,id_map_current,True,pygame.mouse.get_pressed()[0],avatar_main['rect_list'][0])
        npc_follow(screen,bulma,pasos_bulma,p1.s_rect,id_map_current,True)
        npc_follow(screen, milk,pasos_milk,p1.s_rect, id_map_current,True)
        s_rect = avatar_main['rect_list'][0]
        screen.blit(nube_voladora[avatar_main['indice'][0]][round(avatar_main['number_change'][0])],[avatar_main['rect_list'][0][0]-12,avatar_main['rect_list'][0][1]+32])
        Avatar(screen,avatar_main,p1.moverse['up'],p1.moverse['down'],p1.moverse['left'],p1.moverse['right'],pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[2])

        """dead"""
        if avatar_main['life_list'] < 2:
            avatar_main['life_list'] = 400
            west_city['index_y'] = 0
            west_city['index_x'] = 0
            s_rect[0] = 400
            s_rect[1] = 400
            value['xp'] = 0


        """sum"""
        for rect_list in the_npc_0['rect_list']:
            rex = [p1.s_rect,rect_list]
            if west_city['index_y'] < west_city['max_index_y']:
                if s_rect[1] > 700:
                    west_city['index_y'] += 1
                    s_rect[1] = 40
            if west_city['index_x'] < west_city['max_index_x']:
                if s_rect[0] > 1270:
                    west_city['index_x'] += 1
                    s_rect[0] = 20
                    rex[1][0] -= 1280
        """res"""
        if west_city['index_y'] > 0:
            if s_rect[1] < 10:
                west_city['index_y'] -= 1
                s_rect[1] = 700
        if west_city['index_x'] > 0:
            if s_rect[0] < 10:
                west_city['index_x'] -= 1
                s_rect[0] = 1260
    elif map_activates == 'training':
        screen.fill((0,0,0))
        index_for_angle(avatar_training, avatar_training['rect_list'][0],pygame.mouse.get_pos())
        Avatar(screen, avatar_training, p1.moverse['up'], p1.moverse['down'], p1.moverse['left'], p1.moverse['right'],p1.moverse['punch'], pygame.mouse.get_pressed()[2])
    elif map_activates == 'simulation':
        cinematic_1(screen,npc_simulation_1,npc_simulation_2,1000)
    elif map_activates == '2D fight':
        screen.fill((0,0,0))
        Avatar(screen,saitama_2d_fighter,p1.moverse['up'],p1.moverse['down'],p1.moverse['left'],p1.moverse['right'],pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[1])
        gravedad(saitama_2d_fighter,4,2,p1.moverse['up'],500)
        gravedad(luffy_2d_fighter,4,2,p1.moverse['up'],500)
        move_npc_for_enemy(screen,luffy_2d_fighter,saitama_2d_fighter,1000,True,(0,0),True,pygame.mouse.get_pressed()[0],saitama_2d_fighter['rect_list'][0])
        collide_2d_fighter(saitama_2d_fighter,luffy_2d_fighter,5,0)
    elif map_activates == 'other':
        screen.fill((255,0,0))
        camera_follow(screen,map_3d_fake,characters[round(index_character)],p1.moverse['up'],p1.moverse['down'],p1.moverse['left'],p1.moverse['right'],pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[1],pos_player,5)
        pre_render_npc(characters[round(index_character_enem)],screen,pos_enem,pos_player)
        create_button(screen,button_sum_character,pygame.mouse.get_pressed()[0])
        create_button(screen,button_res_character,pygame.mouse.get_pressed()[0])

def change_map(self):
    global map_activates,indice_lugares,index_video,nigga
    map_activates = modos_string[round(ind_mode)]
    rgb = (random.randint(0,250),random.randint(0,250),random.randint(0,250),random.randint(0,250))

    """map copy alpha"""
    if menu.active == False:
        create_button(screen, button_active_menu, pygame.mouse.get_pressed()[0])
        """exp"""
        #use_xp(screen,EXP,p1.s_rect.colliderect(enem['e_rect']))
        """auras"""
        #blit_aura(screen, auras[self.indice][round(self.num_change)], p1.s_rect, 5)
        #blit_sword(screen,nozarashi,p1.s_rect,enem.e_rect,self.indice,pygame.mouse.get_pressed()[2])
        #blit_effect(screen,pygame.mouse.get_pressed()[0],self.indice,p1.s_rect,effect_Tsukiyubi)
        id_map_current = (west_city['index_y'], west_city['index_x'])


        if map_activates == 'history':
            screen.blit(west_city['surf_alpha'][west_city['index_y']][west_city['index_x']],(0,0))
            text_blit_by_far(avatar_main['rect_list'][0], milk['rect_list'][0], 500, text_milk_nearby, text_milk_normal, id_map_current, True,screen)
            text_blit_by_far(avatar_main['rect_list'][0], bulma['rect_list'][0], 500, text_bulma_nearby, text_bulma_normal, id_map_current, True,screen)
    if menu.active == True:

        string_blit(str(map_activates),(900,50),50,rgb,screen)
        screen.blit(portrait_modos[round(ind_mode)],(400,200))

        create_button(screen,button_res_index_mode,pygame.mouse.get_pressed()[0])
        create_button(screen, button_sum_index_mode, pygame.mouse.get_pressed()[0])

        create_button(screen, button_desactive_menu, pygame.mouse.get_pressed()[0])

        create_button(screen, button_save, pygame.mouse.get_pressed()[0])


        create_text_by_font_img(screen, posiciones_b[random.randint(0,1)], font_1, posicion_de_las_letras[random.randint(0,1)])

        #video
        #blit_video(screen,vid)
        #Play_sound(p1.moverse['punch'],Sound_A)
        create_button(screen,button_pause,pygame.mouse.get_pressed()[0])
        create_button(screen, button_despause, pygame.mouse.get_pressed()[0])

p1.function_normal = move_map
p1.function_in_menu = change_map

p1.menu = Menu
p1(screen,1280,720)


