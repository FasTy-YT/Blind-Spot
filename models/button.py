import pygame
from models.config import (
    WHITE, BUTTON_BG, BUTTON_BORDER, BUTTON_TEXT,
    FONT_NAME, FONT_SIZE,
)

if not pygame.font.get_init():
    pygame.font.init()

FONT = pygame.font.SysFont(FONT_NAME, FONT_SIZE)


class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback

    def draw(self, surf):
        pygame.draw.rect(surf, BUTTON_BG, self.rect)
        pygame.draw.rect(surf, BUTTON_BORDER, self.rect, 2)
        txt_surf = FONT.render(self.text, True, BUTTON_TEXT)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surf.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()