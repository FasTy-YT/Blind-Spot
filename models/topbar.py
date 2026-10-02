import pygame
from models.config import (
    WIDTH, TOPBAR_H, TOPBAR_BG,
    TOPBAR_BTN_W, TOPBAR_BTN_H, TOPBAR_BTN_Y,
    TOPBAR_MENU_X, TOPBAR_SAVE_X, TOPBAR_LOAD_X,
    WHITE, FONT_NAME, FONT_SIZE,
)


class TopBar:
    """Верхняя панель с кнопками Меню / Сохранить / Загрузить."""

    def __init__(self, on_menu, on_save, on_load):
        self.on_menu = on_menu
        self.on_save = on_save
        self.on_load = on_load

        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.buttons = [
            self._make_btn(TOPBAR_MENU_X, "Меню", on_menu),
            self._make_btn(TOPBAR_SAVE_X, "Сохранить (F5)", on_save),
            self._make_btn(TOPBAR_LOAD_X, "Загрузить (F9)", on_load),
        ]

    def _make_btn(self, x, text, callback):
        # ширину подгоняем под текст
        w = max(TOPBAR_BTN_W, self.font.size(text)[0] + 20)
        return {
            "rect": pygame.Rect(x, TOPBAR_BTN_Y, w, TOPBAR_BTN_H),
            "text": text,
            "callback": callback,
        }

    def draw(self, surf):
        # фон панели
        pygame.draw.rect(surf, TOPBAR_BG, (0, 0, WIDTH, TOPBAR_H))
        pygame.draw.line(surf, (60, 60, 60), (0, TOPBAR_H), (WIDTH, TOPBAR_H), 1)

        for btn in self.buttons:
            r = btn["rect"]
            pygame.draw.rect(surf, (50, 50, 50), r)
            pygame.draw.rect(surf, WHITE, r, 1)
            txt = self.font.render(btn["text"], True, WHITE)
            surf.blit(txt, txt.get_rect(center=r.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for btn in self.buttons:
                if btn["rect"].collidepoint(event.pos):
                    btn["callback"]()
                    return True
        return False