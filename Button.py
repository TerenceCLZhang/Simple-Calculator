import pygame
import time

# Colours
LIGHT_GREY = (211, 211, 211)
DARK_GREY = (150, 150, 150)
BLACK = (0, 0, 0)

DEBOUNCE_TIME = 0.1


class Button:
    def __init__(self, rect, text, action):
        self.rect = rect
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 30)
        self.is_pressed = False

    def draw(self, surface):
        if self.is_pressed:
            button_color = DARK_GREY
        else:
            button_color = LIGHT_GREY

        pygame.draw.rect(surface, button_color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        self.check_button_pressed(event)

        if self.is_pressed and event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.action()
                time.sleep(DEBOUNCE_TIME)
                self.is_pressed = False

    def check_button_pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True


class NumberButton(Button):
    def __init__(self, rect, text, action, number):
        super().__init__(rect, text, action)
        self.number = number

    def handle_event(self, event):
        self.check_button_pressed(event)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.action(self.number)
                time.sleep(DEBOUNCE_TIME)
                self.is_pressed = False


class OperationButton(Button):
    def __init__(self, rect, text, action, operation):
        super().__init__(rect, text, action)
        self.operation = operation

    def handle_event(self, event):
        self.check_button_pressed(event)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.action(self.operation)
                time.sleep(DEBOUNCE_TIME)
                self.is_pressed = False
