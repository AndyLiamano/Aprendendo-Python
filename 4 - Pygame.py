import pygame

def main():
    pygame.init()
    tela = pygame.display.set_mode([300,300]) # Janela e largura
    pygame.display.set_caption('Joguinho') # Titulo
    relogio = pygame.time.Clock() # Clock é com a primeira letra miuscula.

    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (152,231,114)
    cor_vermelho = (227, 57, 9)
    
    sup = pygame.Surface((200,200)) # uma Superficie
    sup2 = pygame.Surface((100,100))
    
    sup2.fill(cor_verde)
    sup.fill(cor_azul) # cor da Superficie

    ret = pygame.Rect(10, 10, 45, 45) # Criando o retangulo
    
    sair = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Faz o Objeto se mover (Retângulo) 
                ret = ret.move(10,10)
             

                
        relogio.tick(30)
        tela.fill(cor_branca) # muda a cor do fundo da tela
        tela.blit(sup,[50,50]) # coloca o Objeto na tela (x, [10,10]) é a localização do objeto
        tela.blit(sup2,[70,70])
        pygame.draw.rect(tela, cor_vermelho, ret)
        pygame.display.update() # usado para eventos
        
    pygame.quit() # parametro para fecha a janela
    
    

    
        
        

main()




