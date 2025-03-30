import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_PINK, COLOR_BLUE


class AddSecretWord:
    def __init__(self, window):
        pygame.init()
        # Carregar a imagem de fundo
        self.window = window
        self.background_image = pygame.image.load(
            'C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\Level.png'
        )
        # Redimensionar a imagem para ocupar a tela inteira
        self.background_image = pygame.transform.scale(self.background_image, (WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        running = True
        text_size = 40
        text = "Digite a palavra secreta:"
        text_color = COLOR_PINK
        text_center_pos = (WIN_WIDTH // 2, 100)
        font = pygame.font.Font(None, text_size)

        secret_word = ""
        word_color = COLOR_BLUE
        line_top_pos = WIN_HEIGHT // 2 + 30
        line_length = 300

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # encerrar o programa quando apeta o X
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(f"Palavra Secreta: {secret_word}")
                        return secret_word  # Retorna a palavra para o chamador
                    elif event.key == pygame.K_BACKSPACE:
                        secret_word = secret_word[:-1]
                    else:
                        secret_word += event.unicode

            self.window.blit(self.background_image, (0, 0))
            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=text_center_pos)
            self.window.blit(text_surface, text_rect)

            word_surface = font.render(secret_word, True, word_color)
            word_rect = word_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            self.window.blit(word_surface, word_rect)

            pygame.draw.line(self.window, COLOR_BLUE,
                             (WIN_WIDTH // 2 - line_length // 2, line_top_pos),
                             (WIN_WIDTH // 2 + line_length // 2, line_top_pos), 3)

            pygame.display.flip()


import pygame
from code.AddSecretWord import AddSecretWord
from code.MenuScreen import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

def main():
    pygame.init()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Dress Up - Add Secret Word")

    menu = Menu(window)  # Instancia o menu



if __name__ == "__main__":
    main()