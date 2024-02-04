import pygame
import sys
import time

# Inicialização do Pygame
pygame.init()

# Configurações da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Os Pigs")

# Cores
green = (0, 255, 0)

# Carregar imagens dos porquinhos
pig_image = pygame.image.load("pig.png")  # Substitua "pig.png" pelo caminho real do arquivo de imagem

# Posições iniciais dos porquinhos
pig1_pos = [100, 300]
pig2_pos = [300, 300]
pig3_pos = [500, 300]

# Lista de porquinhos
pigs = [pig1_pos, pig2_pos, pig3_pos]

# Loop principal
running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    screen.fill(green)

    # Desenhar os porquinhos
    for pig_pos in pigs:
        screen.blit(pig_image, pig_pos)

    # Verificar se passaram 3 segundos
    current_time = time.time()
    if current_time - start_time >= 3:
        font = pygame.font.Font(None, 36)
        text = font.render("Os Pigs", True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
