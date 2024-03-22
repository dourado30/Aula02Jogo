# C
import pygame

COLOR_ORANGE = (255, 128, 0)  # Nomeia o RGB
COLOR_RED = (235, 51, 36)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 254, 145)

# M
MENU_OPTION = ('NOVO JOGO 1P',
               'NOVO JOGO 2P - MODO FÁCIL',
               'NOVO JOGO 2P - MODO DIFÍCIL',
               'SAIR')

# W
WIN_WIDTH = 576  # tamanho da imagem a ser ajustada
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Player1': 2,
                'Player2': 2,
                'Enemy1': 4,
                'Enemy2': 4,
                }
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
