import pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class DisplayBar:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.max_font_size = 75
        self.font_size = self.max_font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.text = self.font.render("0", True, BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def update_text(self, value, reset=False):
        if reset:
            self.font = pygame.font.Font(None, self.max_font_size)

        self.text = self.font.render(str(value), True, BLACK)
        while self.text.get_width() > self.rect.width:
            self.font_size -= 1
            self.font = pygame.font.Font(None, self.font_size)
            self.text = self.font.render(
                str(value), True, BLACK)

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        surface.blit(self.text, self.text_rect.topleft)
