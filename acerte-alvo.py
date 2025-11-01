# Baixar o Pygame a importar o Pygame
import pygame
import random

# Inicia o Pygame
pygame.init()

# Variaveis relevantes para o jogo
altura_tela = 600
largura_tela = 800

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Acerte o Alvo!')

# Cores
roxo = (31, 0, 49)
amarelo = (255, 241, 169)
rosa = (255, 137, 173)

relogio = pygame.time.Clock()
rodando = True


pontos = 0
fonte = pygame.font.SysFont("bahnschrift", 35)

# Largura e altura do alvo
tamanho_alvo = 50

# Onde ele vai estar
alvo_rect = pygame.Rect(375, 275, tamanho_alvo, tamanho_alvo)

while rodando:

    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if alvo_rect.collidepoint(evento.pos):
                alvo_rect.x = random.randrange(0, largura_tela, tamanho_alvo)
                alvo_rect.y = random.randrange(0, altura_tela, tamanho_alvo)
                pontos += 1
    
    tela.fill(roxo)
    pygame.draw.rect(tela, rosa, alvo_rect)
    # Renderiza o texto (transforma em imagem)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, amarelo)
    # Desenha o texto na tela
    tela.blit(texto_pontos, (10, 10))



    pygame.draw.rect(tela, rosa, alvo_rect)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()