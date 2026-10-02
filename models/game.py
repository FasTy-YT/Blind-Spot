import os
import pygame
from models.config import (
    WIDTH, HEIGHT, CAPTION, FPS,
    BLUE, DARK_BLUE, RED, DARK_BOX, WHITE,
    DIALOG_BOX_Y, DIALOG_BOX_H, DIALOG_TEXT_X, DIALOG_TEXT_Y,
    DIALOG_LINE_H, DIALOG_MAX_CHARS,
    FALLBACK_USERNAME, FONT_NAME, FONT_SIZE, UNSAVEABLE_STATES, CRASH_HIDE_UI, BLACK
)
from models.gamestate import GameState
from models.savemanager import SaveManager
from models.scenes import SCENE_REGISTRY, Day1Scene, WarningScene
from models.topbar import TopBar
from models.menu_overlay import MenuOverlay
from models.config import TOAST_DURATION, TOAST_X, TOAST_Y, WHITE, WIDTH


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

        self.state = GameState()
        self.save_manager = SaveManager(slot=1)
        self.scene = None
        self.running = True

        # тосты
        self.toast_text = ""
        self.toast_timer = 0

        # UI
        self.topbar = TopBar(
            on_menu=self.open_menu,
            on_save=self.save,
            on_load=self.load,
        )
        self.menu = MenuOverlay(on_close=self.close_menu)

        self.change_scene(WarningScene())

    # ---------- утилиты ----------
    def open_menu(self):
        self.menu.open()

    def close_menu(self):
        self.menu.close()

    def show_toast(self, text):
        self.toast_text = text
        self.toast_timer = TOAST_DURATION

    def get_system_name(self):
        try:
            return os.getlogin()
        except Exception:
            return FALLBACK_USERNAME

    def change_scene(self, scene):
        if self.scene is not None:
            old_day = self.state.day
            if old_day not in UNSAVEABLE_STATES:
                self.save()
        self.scene = scene
        scene.enter(self)

    # ---------- сохранение / загрузка ----------
    def save(self):
        if self.state.day in UNSAVEABLE_STATES:
            self.show_toast("Здесь нельзя сохраниться")
            return
        ok = self.save_manager.save(self.state)
        self.show_toast("Сохранено" if ok else "Ошибка сохранения")

    def load(self):
        loaded = self.save_manager.load()
        if loaded is None:
            self.show_toast("Сейв не найден")
            return False
        self.state = loaded
        scene_class = SCENE_REGISTRY.get(self.state.day, Day1Scene)
        self.change_scene(scene_class())
        self.show_toast("Загружено")
        return True

    # ---------- отрисовка ----------
    def draw(self):
        if CRASH_HIDE_UI and self.state.day == "КрахСистемы":
            self.screen.fill(BLACK)
            self.scene.draw(self, self.screen)
            return

        # фон
        if self.state.day in ("ЗлостьГлаза", "КрахСистемы"):
            self.screen.fill(RED)
        elif self.state.day == "НочьДень5":
            self.screen.fill(DARK_BLUE)
        elif self.state.day == "Скример":
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill(BLUE)

        # петы
        for pet in self.state.pets:
            pet.draw(self.screen)

        # глаз
        if self.state.eye and self.state.day != "Скример":
            self.state.eye.draw(self.screen, self.font)

        # сцена (кнопки, поле ввода)
        self.scene.draw(self, self.screen)

        # диалоговое окно
        self.draw_dialogue()

        # кнопки сверху
        for btn in self.scene.buttons:
            btn.draw(self.screen)

    def draw_dialogue(self):
        pygame.draw.rect(self.screen, DARK_BOX,
                         (0, DIALOG_BOX_Y, WIDTH, DIALOG_BOX_H))

        y = DIALOG_TEXT_Y
        for line in self.state.dialogue_text:
            words = line.split(' ')
            current = ""
            for word in words:
                if len(current) + len(word) + 1 <= DIALOG_MAX_CHARS:
                    current += word + " "
                else:
                    txt = self.font.render(current.strip(), True, WHITE)
                    self.screen.blit(txt, (DIALOG_TEXT_X, y))
                    y += DIALOG_LINE_H
                    current = word + " "
            if current:
                txt = self.font.render(current.strip(), True, WHITE)
                self.screen.blit(txt, (DIALOG_TEXT_X, y))
                y += DIALOG_LINE_H
        self.topbar.draw(self.screen)

        # тост
        if self.toast_timer > 0 and self.toast_text:
            txt = self.font.render(self.toast_text, True, WHITE)
            rect = txt.get_rect(topleft=(TOAST_X, TOAST_Y))
            bg = pygame.Surface((rect.width + 20, rect.height + 10), pygame.SRCALPHA)
            bg.fill((0, 0, 0, 180))
            self.screen.blit(bg, (rect.x - 10, rect.y - 5))
            self.screen.blit(txt, rect)

        # оверлей меню поверх всего
        self.menu.draw(self.screen)

    # ---------- главный цикл ----------
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)

            if self.toast_timer > 0:
                self.toast_timer -= dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

                # если открыто меню — оно глотает всё
                if self.menu.handle_event(event):
                    continue

                # верхняя панель
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        self.save()
                        continue
                    elif event.key == pygame.K_F9:
                        self.load()
                        continue

                if self.topbar.handle_event(event):
                    continue

                # события сцены
                self.scene.handle_event(self, event)

            # обновляем сцену только если меню закрыто
            if not self.menu.visible:
                self.scene.update(self, dt)

            self.draw()
            pygame.display.flip()

        self.save()
        pygame.quit()