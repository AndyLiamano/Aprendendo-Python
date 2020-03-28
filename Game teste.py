import pygame 
import controles
x = 0
y = 0
def main():
    pygame.init()
    
    tela = pygame.display.set_mode([300,300]) # Janela e largura
    pygame.display.set_caption('Joguinho') # Titulo
    relogio = pygame.time.Clock() # Clock é com a primeira letra miuscula.

    cor_branca = (60,45,0)
    cor_azul = (108,0,0) 
    
    cor_verde = (152,231,114)
    cor_amarelo = (13, 111, 11)      
    sup = pygame.Surface((200,200)) # uma Superficie
    sup2 = pygame.Surface((100,100))
    sup3 = pygame.Surface((305,305))
    
    cor_rosa = (225,47,225)
    sup3.fill(cor_rosa)
    

    
    sup2.fill(cor_branca)
    sup.fill(cor_azul) # cor da Superficie
    
    ret = pygame.Rect(10, 10, 20, 20) # Criando o retângulo
    
    sair = False
    
    poon = pygame.mixer.Sound('audio/poon.ogg')
    #pygame.mixer.music.load('audio/music.ogg')
    #pygame.mixer.music.play(-1,0.0)
    while sair != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                

         #   if event.type == controles.teclas['click']:
                #Faz o Objeto se mover (Retângulo) 
        #        ret = ret.move(controles.mouse(x))
         #       poon.play()
                
            if event.type == pygame.MOUSEMOTION:
               #ret = ret.move(-10,-10)
                sup3.scroll(10,10)
           
            if event.type == pygame.KEYDOWN:

                if event.key == controles.teclas['ESC']:
                    sair = True
                
                if event.key == controles.teclas['cima']:
                    #Faz o Objeto se mover (Retângulo) 
                    ret = ret.move(controles.cima(x))
                    poon.play()

                if event.key == controles.teclas['baixo']:
                    ref = ret.move_ip(controles.baixo(x))
                    

                if event.key == controles.teclas['esquerda']:
                    ref = ret.move_ip(controles.esquerda(x))
                    poon.play()

                if event.key == controles.teclas['direita']:
                    ref = ret.move_ip(controles.direita(x))
                    poon.play()
                    
            if ret.left < 0:
                ret.right = 300 

            if ret.right > 300:
                ret.left = 0

            if ret.top < 0:
                ret.bottom = 300

            if ret.bottom > 300:
                ret.top = 0

        relogio.tick(30)
        tela.fill(cor_branca) # muda a cor do fundo da tela
        tela.blit(sup3,[0,0])
        tela.blit(sup,[50,50]) # coloca o Objeto na tela (x, [10,10]) é a localização do objeto
        tela.blit(sup2,[70,70])
        pygame.draw.rect(tela, cor_amarelo, ret)
        pygame.display.update() # usado para eventos
        
    pygame.quit() # parametro para fecha a janela

main()




