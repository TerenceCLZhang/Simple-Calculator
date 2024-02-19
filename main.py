import pygame
import sys

from Components.Button import Button, NumberButton, OperationButton
from Components.DisplayBar import DisplayBar

# Window Dimensions
WIDTH = 400
HEIGHT = 610
WINDOW_SIZE = (WIDTH, HEIGHT)

# Colours
WHITE = (255, 255, 255)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)

MAXIMUM_LENGTH = 10


class Calculator:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Simple Calculator")

        # Icon source: https://iconduck.com/icons/183747/math
        icon = pygame.image.load("math.ico")
        pygame.display.set_icon(icon)

        # Numbers
        self.previous = "0"
        self.current = "0"
        self.operation = ""

        # Flags
        self.pressed_equals = False
        self.pressed_operation = False
        self.pressed_special = False

        # Display Bar
        X_START = 25
        Y_START = 25

        DISPLAY_BAR_WIDTH = WIDTH - X_START * 2
        DISPLAY_BAR_HEIGHT = 100

        self.display_bar = DisplayBar(
            X_START, Y_START, DISPLAY_BAR_WIDTH, DISPLAY_BAR_HEIGHT)

        # Buttons
        BUTTON_SPACING = 15
        button_width = (DISPLAY_BAR_WIDTH - BUTTON_SPACING * 3) / 4
        button_height = button_width

        # Button y start
        buttons_row_1_y_start = 150
        buttons_row_2_y_start = buttons_row_1_y_start + button_width + BUTTON_SPACING
        buttons_row_3_y_start = buttons_row_2_y_start + button_width + BUTTON_SPACING
        buttons_row_4_y_start = buttons_row_3_y_start + button_width + BUTTON_SPACING
        buttons_row_5_y_start = buttons_row_4_y_start + button_width + BUTTON_SPACING

        # Row 1 Buttons
        self.percentage = Button(pygame.Rect(
            X_START, buttons_row_1_y_start, button_width, button_height), "%", self.perform_percentage)
        self.square = Button(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                         buttons_row_1_y_start, button_width, button_height), "x²", self.perform_square)
        self.square_root = Button(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                              buttons_row_1_y_start, button_width, button_height), "√x", self.perform_square_root)
        self.button_c = Button(pygame.Rect(
            X_START + 3 * (button_width + BUTTON_SPACING), buttons_row_1_y_start, button_width, button_height), "c", self.perform_clear)

        # Row 2 Buttons
        self.button_7 = NumberButton(pygame.Rect(
            X_START, buttons_row_2_y_start, button_width, button_height), "7", self.handle_number, 7)
        self.button_8 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_2_y_start, button_width, button_height), "8", self.handle_number, 8)
        self.button_9 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_2_y_start, button_width, button_height), "9", self.handle_number, 9)
        self.button_add = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                      buttons_row_2_y_start, button_width, button_height), "+", self.handle_operation, "+")

        # Row 3 Buttons
        self.button_4 = NumberButton(pygame.Rect(
            X_START, buttons_row_3_y_start, button_width, button_height), "4", self.handle_number, 4)
        self.button_5 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_3_y_start, button_width, button_height), "5", self.handle_number, 5)
        self.button_6 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_3_y_start, button_width, button_height), "6", self.handle_number, 6)
        self.button_subtract = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                           buttons_row_3_y_start, button_width, button_height), "-", self.handle_operation, "-")

        # Row 4 Buttons
        self.button_1 = NumberButton(pygame.Rect(
            X_START, buttons_row_4_y_start, button_width, button_height), "1", self.handle_number, 1)
        self.button_2 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_4_y_start, button_width, button_height), "2", self.handle_number, 2)
        self.button_3 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_4_y_start, button_width, button_height), "3", self.handle_number, 3)
        self.button_multiply = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                           buttons_row_4_y_start, button_width, button_height), "x", self.handle_operation, "*")

        # Row 5 Buttons
        self.decimal = Button(pygame.Rect(
            X_START, buttons_row_5_y_start, button_width, button_height), ".", self.handle_decimal)
        self.button_0 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_5_y_start, button_width, button_height), "0", self.handle_number, 0)
        self.button_equal = Button(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                               buttons_row_5_y_start, button_width, button_height), "=", self.perform_calculate)
        self.button_divide = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                         buttons_row_5_y_start, button_width, button_height), "/", self.handle_operation, "/")

        self.buttons = [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
                        self.button_8, self.button_9, self.button_add, self.button_subtract, self.button_multiply, self.button_divide, self.button_c,
                        self.button_equal, self.percentage, self.square, self.square_root, self.decimal]

    def run(self):
        running = True
        while running:
            self.window.fill(DARK_GREY)

            self.display_bar.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for button in self.buttons:
                button.draw(self.window)
                button.handle_event(event)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def handle_number(self, number):
        if self.pressed_equals and not self.pressed_operation or self.pressed_special:
            self.perform_clear()

        if self.current == "0":
            self.current = str(number)
        elif self.count_digits(self.current) + 1 <= MAXIMUM_LENGTH:
            self.current += str(number)
        self.display_bar.update_text(self.current)

    def count_digits(self, input_string):
        digit_count = sum(char.isdigit() for char in input_string)
        return digit_count

    def handle_operation(self, operation):
        self.pressed_operation = True
        self.pressed_special = False
        self.previous = self.current
        self.operation = operation
        self.display_bar.update_text(self.current, reset=True)
        self.current = "0"

    def perform_calculate(self):
        self.pressed_operation = False
        self.pressed_equals = True
        if self.operation:
            self.current = str(
                self.check_integer(eval(f"{self.previous} {self.operation} { self.current}")))
        self.display_bar.update_text(self.current, reset=True)

    def perform_clear(self):
        self.current = "0"
        self.previous = "0"
        self.operation = ""
        self.pressed_equals = False
        self.pressed_operation = False
        self.pressed_special = False
        self.display_bar.update_text(self.current, reset=True)

    def handle_decimal(self):
        if self.pressed_equals and not self.pressed_operation or self.pressed_special:
            self.perform_clear()

        if self.current == "0":
            self.current = "0."
        elif "." not in self.current:
            self.current += "."
        self.display_bar.update_text(self.current)

    def perform_percentage(self):
        self.pressed_special = True
        self.current = str(eval(f"{self.current} / 100"))
        self.display_bar.update_text(self.current)

    def perform_square(self):
        self.pressed_special = True
        self.current = str(self.check_integer(eval(f"{self.current} ** 2")))
        self.display_bar.update_text(self.current)

    def perform_square_root(self):
        self.pressed_special = True
        self.current = str(self.check_integer(eval(f"{self.current} ** 0.5")))
        self.display_bar.update_text(self.current)

    def check_integer(self, num):
        if num % 1 == 0:
            num = int(num)
        return num


def main():
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
