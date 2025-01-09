import pygame
import random
from tkinter import Tk, filedialog

# Inicializar pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Ritmo")

# Configurações das notas
LARGURA_NOTA = 50
ALTURA_NOTA = 50
VELOCIDADE_NOTA = 5
COR_NOTA = (255, 0, 0)
TECLAS = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
POSICOES_X = [200, 300, 400, 500]

# Fonte para pontuação
fonte = pygame.font.Font(None, 36)

# Função para desenhar a tela do jogo
def desenhar_tela(notas, pontuacao, imagem_fundo):
    if imagem_fundo:
        TELA.blit(imagem_fundo, (0, 0))
    else:
        TELA.fill((0, 0, 0))
        
    for nota in notas:
        pygame.draw.rect(TELA, COR_NOTA, (nota['x'], nota['y'], LARGURA_NOTA, ALTURA_NOTA))
    
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    TELA.blit(texto_pontuacao, (10, 10))
    pygame.display.flip()

# Função principal do jogo
def jogo():
    notas = []
    pontuacao = 0
    jogando = True
    clock = pygame.time.Clock()
    imagem_fundo = None

    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            if evento.type == pygame.KEYDOWN:
                for nota in notas:
                    if evento.key == nota['tecla'] and nota['y'] > ALTURA_TELA - ALTURA_NOTA - 10:
                        pontuacao += 1
                        notas.remove(nota)
        
        if random.randint(1, 30) == 1:
            nova_nota = {
                'x': random.choice(POSICOES_X),
                'y': 0,
                'tecla': random.choice(TECLAS)
            }
            notas.append(nova_nota)
        
        for nota in notas:
            nota['y'] += VELOCIDADE_NOTA
            if nota['y'] > ALTURA_TELA:
                notas.remove(nota)

        desenhar_tela(notas, pontuacao, imagem_fundo)
        clock.tick(60)

    pygame.quit()

def selecionar_imagem():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal do tkinter
    caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png")])
    root.destroy()
    if caminho_imagem:
        return pygame.image.load(caminho_imagem)
    return None

if __name__ == "__main__":
    imagem_fundo = selecionar_imagem()
    jogo()
