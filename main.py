import pygame
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man bolado")
branco = (255,255,255)
preto = (0,0,0)
posicaoXpersona = 400
posicaoYpersona = 300
movimentoXpersona = 0
movimentoYpersona = 0
posicaoXmissel = 400  
posicaoYmissel = -240 
velocidadeMissel = 30
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
missileSound = pygame.mixer.Sound("assets/missile.wav") # é som, não musica
pygame.mixer.Sound.play(missileSound)
fonte = pygame.font.SysFont("comicsans",14) # cria uma fonte
pygame.mixer.music.load ("assets/ironsound.mp3") #carrega a musica
pygame.mixer.music.play(-1) # começa a musica
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT: # se o evento que aconteceu for pressionar uma tecla e a tecla q aconteceu for direita
            movimentoXpersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT: 
            movimentoXpersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT: # se eu paro de pressionar a tecla, o movimento fica
            movimentoXpersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXpersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP: # se o evento que aconteceu for pressionar uma tecla e a tecla q aconteceu for direita
            movimentoYpersona = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN: 
            movimentoYpersona = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP: # se eu paro de pressionar a tecla, o movimento fica
            movimentoYpersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYpersona = 0
    
    posicaoXpersona = posicaoXpersona + movimentoXpersona
    posicaoYpersona = posicaoYpersona + movimentoYpersona
    if posicaoXpersona <0:
        posicaoXpersona = 0
    elif posicaoXpersona >600:
        posicaoXpersona = 600

    if posicaoYpersona <0:
        posicaoYpersona = 0
    elif posicaoYpersona >473:
        posicaoYpersona = 473
    import random
    tela.fill(branco)
    tela.blit (fundo, (0,0)) # fundo adicionado
    tela.blit(iron, (posicaoXpersona,posicaoYpersona)) # adiciona o a imagem
    posicaoYmissel = posicaoYmissel + velocidadeMissel
    if posicaoYmissel > 600:
        posicaoYmissel = -240
        posicaoXmissel = random.randint(0,800)
        velocidadeMissel = velocidadeMissel +1

    tela.blit(missel,(posicaoXmissel, posicaoYmissel) )
    texto = fonte.render(str(posicaoXpersona)+"-"+str(posicaoYpersona), True, branco) # renderiza o texto e em 

    tela.blit(texto, (posicaoXpersona, posicaoYpersona)) # blit é para colocar elemento na tela, colocar o texto e depois a posição
    
    pygame.display.update()
    relogio.tick(60)

