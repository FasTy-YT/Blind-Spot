import pygame
from models.config import (
    WIDTH, HEIGHT,
    MENU_OVERLAY_BG, MENU_PANEL_COLOR,
    MENU_PANEL_X, MENU_PANEL_Y, MENU_PANEL_W, MENU_PANEL_H,
    MENU_TEXT_X, MENU_TEXT_Y, MENU_LINE_H,
    MENU_CLOSE_BTN_X, MENU_CLOSE_BTN_Y, MENU_CLOSE_BTN_W, MENU_CLOSE_BTN_H,
    WHITE, FONT_NAME, FONT_SIZE,
)


class MenuOverlay:
    """Оверлей меню со справкой. Открывается кнопкой 'Меню'."""

    HELP_LINES = [
        "СЛЕПАЯ ЗОНА (Blind Spot)",
        "",
        "Управление:",
        "  • ЛКМ по кнопкам — переходы и выборы",
        "  • ЛКМ по полю ввода — печатать имена петов",
        "  • Enter — подтвердить имя",
        "  • Backspace — стереть символ",
        "  • F5 — сохранить игру",
        "  • F9 — загрузить игру",
        "  • ESC — закрыть это меню",
        "",
        "О игре:",
        "  Милая игра про петов... которая знает",
        "  больше, чем должна. Следи за Глазом.",
        "",
        "Удачи, игрок.",
    ]

    def __init__(self, on_close):
        self.on_close = on_close
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.font_bold = pygame.font.SysFont(FONT_NAME, FONT_SIZE, bold=True)
        self.visible = False

        self.close_btn = pygame.Rect(
            MENU_CLOSE_BTN_X, MENU_CLOSE_BTN_Y,
            MENU_CLOSE_BTN_W, MENU_CLOSE_BTN_H,
        )

    def open(self):
        self.visible = True

    def close(self):
        self.visible = False

    def toggle(self):
        self.visible = not self.visible

    def handle_event(self, event):
        if not self.visible:
            return False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.close()
            return True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.close_btn.collidepoint(event.pos):
                self.close()
                return True

        # пока меню открыто — глотаем все события
        return True

    def draw(self, surf):
        if not self.visible:
            return

        # затемняем фон
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill(MENU_OVERLAY_BG)
        surf.blit(overlay, (0, 0))

        # панель
        pygame.draw.rect(surf, MENU_PANEL_COLOR,
                         (MENU_PANEL_X, MENU_PANEL_Y, MENU_PANEL_W, MENU_PANEL_H))
        pygame.draw.rect(surf, WHITE,
                         (MENU_PANEL_X, MENU_PANEL_Y, MENU_PANEL_W, MENU_PANEL_H), 2)

        # текст
        y = MENU_TEXT_Y
        for i, line in enumerate(self.HELP_LINES):
            font = self.font_bold if i == 0 else self.font
            color = WHITE
            txt = font.render(line, True, color)
            surf.blit(txt, (MENU_TEXT_X, y))
            y += MENU_LINE_H

        # кнопка закрытия
        pygame.draw.rect(surf, (50, 50, 50), self.close_btn)
        pygame.draw.rect(surf, WHITE, self.close_btn, 1)
        close_txt = self.font.render("Закрыть (ESC)", True, WHITE)
        surf.blit(close_txt, close_txt.get_rect(center=self.close_btn.center))