import math
import sys
import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Basquete Pygame - Arremesso Livre")
relogio = pygame.time.Clock()

# Cores (RGB)
COR_FUNDO = (30, 30, 40)
COR_BOLA = (230, 110, 35)
COR_CESTA = (200, 50, 50)
COR_TABUELA = (220, 220, 220)
COR_TEXTO = (255, 255, 255)
COR_MIRA = (100, 200, 255)

# Propriedades do Jogo
GRAVIDADE = 0.5
pontos = 0
tentativas = 0

# Posição e Raio da Bola
POS_INICIAL_BOLA = [150, 500]
pos_bola = list(POS_INICIAL_BOLA)
vel_bola = [0.0, 0.0]
raio_bola = 18
em_voo = False

# Mira e Força
angulo = 45  # Graus
forca = 0
carregando_forca = False

# Posições da Cesta e Tabuela
cesta_x, cesta_y = 650, 250
largura_cesta = 60


def reiniciar_bola():
    global pos_bola, vel_bola, em_voo, forca, carregando_forca
    pos_bola = list(POS_INICIAL_BOLA)
    vel_bola = [0.0, 0.0]
    em_voo = False
    forca = 0
    carregando_forca = False


fonte = pygame.font.SysFont("arial", 24)

# Loop Principal
rodando = True
while rodando:
    dt = relogio.tick(60)

    # --- Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if not em_voo:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    carregando_forca = True
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE and carregando_forca:
                    # Lança a bola
                    rad = math.radians(angulo)
                    vel_bola[0] = forca * math.cos(rad)
                    vel_bola[1] = -forca * math.sin(rad)
                    em_voo = True
                    carregando_forca = False
                    tentativas += 1

    # Controles da Mira (Seta Esquerda / Direita)
    teclas = pygame.key.get_pressed()
    if not em_voo:
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            angulo = min(85, angulo + 1.5)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            angulo = max(10, angulo - 1.5)

        if carregando_forca:
            forca = min(25, forca + 0.4)  # Força máxima = 25

    # --- Física da Bola ---
    if em_voo:
        pos_bola[0] += vel_bola[0]
        pos_bola[1] += vel_bola[1]
        vel_bola[1] += GRAVIDADE  # Gravidade atuando na bola

        # Colisão com a Tabuela (rebate na parede vertical atrás da cesta)
        if pos_bola[0] + raio_bola >= 710 and 150 <= pos_bola[1] <= 300:
            vel_bola[0] *= -0.6

        # Checa Cesta (Acerto)
        distancia_cesta_x = abs(pos_bola[0] - (cesta_x + largura_cesta / 2))
        distancia_cesta_y = abs(pos_bola[1] - cesta_y)

        if (
            distancia_cesta_x < largura_cesta / 2
            and distancia_cesta_y < 15
            and vel_bola[1] > 0
        ):
            pontos += 1
            reiniciar_bola()

        # Reseta se sair da tela ou cair no chão
        if (
            pos_bola[1] > ALTURA + 50
            or pos_bola[0] > LARGURA + 50
            or pos_bola[0] < -50
        ):
            reiniciar_bola()

    # --- Desenho na Tela ---
    tela.fill(COR_FUNDO)

    # Chao
    pygame.draw.rect(tela, (50, 50, 60), (0, 550, LARGURA, 50))

    # Tabuela e Cesta
    pygame.draw.rect(
        tela, COR_TABUELA, (710, 150, 15, 120)
    )  # Madeiramento da tabuela
    pygame.draw.line(
        tela, (180, 180, 180), (710, 250), (cesta_x, cesta_y), 6
    )  # Suporte do aro
    pygame.draw.line(
        tela,
        COR_CESTA,
        (cesta_x, cesta_y),
        (cesta_x + largura_cesta, cesta_y),
        8,
    )  # Aro

    # Linha de Mira (quando pronta para arremessar)
    if not em_voo:
        rad = math.radians(angulo)
        mira_x = POS_INICIAL_BOLA[0] + math.cos(rad) * (60 + forca * 2)
        mira_y = POS_INICIAL_BOLA[1] - math.sin(rad) * (60 + forca * 2)
        pygame.draw.line(tela, COR_MIRA, POS_INICIAL_BOLA, (mira_x, mira_y), 2)

    # Bola
    pygame.draw.circle(
        tela, COR_BOLA, (int(pos_bola[0]), int(pos_bola[1])), raio_bola
    )

    # Barra de Força (carregamento)
    if carregando_forca:
        largura_barra = int((forca / 25) * 100)
        pygame.draw.rect(
            tela, (100, 100, 100), (POS_INICIAL_BOLA[0] - 50, 540, 100, 12)
        )
        pygame.draw.rect(
            tela, (255, 50, 50), (POS_INICIAL_BOLA[0] - 50, 540, largura_barra, 12)
        )

    # Placar e Instruções
    texto_pontos = fonte.render(
        f"Pontos: {pontos}  |  Tentativas: {tentativas}", True, COR_TEXTO
    )
    texto_ajuda = fonte.render(
        "Setas Esq/Dir: Ângulo | Espaço (segurar): Força", True, (180, 180, 180)
    )
    tela.blit(texto_pontos, (20, 20))
    tela.blit(texto_ajuda, (20, 550))

    pygame.display.flip()

pygame.quit()
sys.exit()