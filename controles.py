import pygame


def mouse(mouse):
    while True:
        #Faz o Objeto se mover (Retângulo) 
        mouse = (10,10)
        return mouse
    
def cima(cima):
    while True:
        cima = (0,-10)
        return cima
    
def direita(direita):
    while True:
        direita = (10,0)
        return direita

def esquerda(esquerda):
    while True:
        esquerda = (-10,0)
        return esquerda

def baixo(baixo):
    while True:
        baixo = (0,10)
        return baixo
    
teclas = {'click':pygame.MOUSEBUTTONDOWN,
          'cima':pygame.K_UP,
          'direita':pygame.K_RIGHT,
          'esquerda':pygame.K_LEFT,
          'baixo':pygame.K_DOWN,
          'ESC':pygame.K_ESCAPE,
          }

#98 981569274
