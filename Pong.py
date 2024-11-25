import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações de FPS
FPS = 60

# Resolução padrão
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
try:
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
except Exception as e:
    print(f"Erro ao obter resolução nativa: {e}")

# Cores
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 255, 0)

# Configurações da raquete
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Configurações da bola
BALL_WIDTH, BALL_HEIGHT = 10, 10

# Pontuação para vencer
WINNING_SCORE = 10

# Inicializando tela em tela cheia
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Pong com Mesa de Ping Pong")
clock = pygame.time.Clock()

# Carregar a imagem de fundo
background = pygame.image.load('table.jpg')  # Verifique se o caminho da imagem está correto
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonte
font = pygame.font.Font(None, 50)

# Estados do jogo
menu_active = True
game_active = False
pause_active = False
menu_options = [
    "Velocidade da Bola: Lenta",
    "Velocidade da Bola: Média",
    "Velocidade da Bola: Rápida",
    "Velocidade da Bola: Impossível",
    "Velocidade da Raquete: Lenta",
    "Velocidade da Raquete: Normal",
    "Velocidade da Raquete: Rápida",
    "Começar o Jogo",
]
selected_option = 0

# Variáveis globais
ball_speed_x, ball_speed_y = 6, 6
paddle_speed = PADDLE_SPEED
player1_score, player2_score = 0, 0

# Configuração inicial das raquetes e bola
def setup_game_objects():
    global player1, player2, ball
    player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)

# Reinicia a bola
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x = random.choice([-6, 6])
    ball_speed_y = random.choice([-6, 6])

# Função para mostrar o vencedor
def show_winner():
    winner_text = "Jogador 1 Venceu!" if player1_score >= WINNING_SCORE else "Jogador 2 Venceu!"
    winner_surface = font.render(winner_text, True, WHITE)
    screen.fill((0, 0, 0))
    screen.blit(winner_surface, (SCREEN_WIDTH // 2 - winner_surface.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Manipula o movimento da bola
def handle_ball_movement():
    global ball_speed_x, ball_speed_y, player1_score, player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    if ball.left <= 0:
        player2_score += 1
        reset_ball()

    if ball.right >= SCREEN_WIDTH:
        player1_score += 1
        reset_ball()

    if player1_score >= WINNING_SCORE or player2_score >= WINNING_SCORE:
        show_winner()

# Manipula o movimento dos jogadores
def handle_player_movement(keys):
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += paddle_speed

    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += paddle_speed

# Desenha os objetos do jogo
def draw_objects():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

# Desenha o menu
def draw_menu():
    screen.fill((0, 0, 0))
    title_text = font.render("Bem-vindo ao Pong", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
    for i, option in enumerate(menu_options):
        color = HIGHLIGHT_COLOR if i == selected_option else WHITE
        option_text = font.render(option, True, color)
        screen.blit(option_text, (SCREEN_WIDTH // 2 - option_text.get_width() // 2, 150 + i * 50))

# Desenha a tela de pausa
def draw_pause():
    pause_text = font.render("Jogo Pausado - Pressione P para Continuar", True, WHITE)
    screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2))

# Manipula a entrada do menu
def handle_menu_input():
    global menu_active, game_active, selected_option, ball_speed_x, ball_speed_y, paddle_speed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        selected_option = (selected_option - 1) % len(menu_options)
        pygame.time.wait(200)

    elif keys[pygame.K_DOWN]:
        selected_option = (selected_option + 1) % len(menu_options)
        pygame.time.wait(200)

    elif keys[pygame.K_RETURN]:
        if selected_option == 0:
            ball_speed_x, ball_speed_y = 4, 4
        elif selected_option == 1:
            ball_speed_x, ball_speed_y = 6, 6
        elif selected_option == 2:
            ball_speed_x, ball_speed_y = 8, 8
        elif selected_option == 3:
            ball_speed_x, ball_speed_y = 15, 15
        elif selected_option == 4:
            paddle_speed = 5
        elif selected_option == 5:
            paddle_speed = 7
        elif selected_option == 6:
            paddle_speed = 10
        elif selected_option == 7:
            menu_active = False
            game_active = True
            setup_game_objects()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and game_active:
                pause_active = not pause_active
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    if menu_active:
        draw_menu()
        handle_menu_input()
    elif game_active:
        if not pause_active:
            keys = pygame.key.get_pressed()
            handle_player_movement(keys)
            handle_ball_movement()
            draw_objects()
        else:
            draw_pause()

    pygame.display.flip()
    clock.tick(FPS)
