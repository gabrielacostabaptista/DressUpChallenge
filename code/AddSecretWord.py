import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, \
    COLOR_PINK  # Certifique-se de que as constantes estão definidas

class AddSecretWord:
    def __init__(self, window):
        self.window = window

        # Carregar a imagem de fundo
        self.background_image = pygame.image.load(
            'C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\Level.png'
        )
        # Redimensionar a imagem para ocupar a tela inteira
        self.background_image = pygame.transform.scale(self.background_image, (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        running = True
        # Definir o texto e a fonte
        text_size = 40  # Tamanho da fonte
        text = "Digite a palavra secreta:"  # Texto que será exibido
        text_color = COLOR_PINK  # Cor do texto
        text_center_pos = (WIN_WIDTH // 2, 100)  # Posição do texto (centralizado na parte superior)

        # Criar a fonte
        font = pygame.font.Font(None, text_size)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechar a janela
                    running = False

            # Desenhar a imagem de fundo
            self.window.blit(self.background_image, (0, 0))
            # Criar a superfície com o texto
            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=text_center_pos)  # Posicionar o texto

            # Desenhar o texto na janela
            self.window.blit(text_surface, text_rect)

            # Atualizar a tela
            pygame.display.flip()

        pygame.quit()

# Função main para inicializar a janela e a execução do jogo
def main():
    pygame.init()
    window = pygame.display.set_mode((576, 324))  # As dimensões da janela
    pygame.display.set_caption("Add Secret Word Test")

    # Instanciando a tela de AddSecretWord
    add_secret_word_screen = AddSecretWord(window)
    add_secret_word_screen.run()  # Chama a função que desenha a janela

if __name__ == "__main__":
    main()

#def verificar_letra(self, letra):
        #pass

    #def letra_adivinhada(self, letra):
        #pass
