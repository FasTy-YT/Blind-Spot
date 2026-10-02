from models.config import WHITE, WIDTH, HEIGHT, PET_COLORS, FONT_SIZE, BLACK
import pygame
from pygame import font

class Scene:
    def __init__(self):
        self.buttons = []          # кнопки этой сцены
        self.dialogue_text = []    # текст этой сцены

    def enter(self, game):
        """Вызывается при входе в сцену. Настройка состояния."""
        pass

    def handle_event(self, game, event):
        """Обработка событий (клики, клавиши)."""
        for btn in self.buttons:
            btn.handle_event(event)

    def update(self, game, dt):
        """Обновление логики (таймеры, анимации). dt — мс с прошлого кадра."""
        pass

    def draw(self, game, surf):
        """Отрисовка сцены поверх общего фона."""
        for btn in self.buttons:
            btn.draw(surf)

    def next_scene(self, game):
        """Возвращает следующую сцену или None."""
        return None