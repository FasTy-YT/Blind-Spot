import random
import pygame

from models.savemanager import SaveManager
from models.scene import Scene
from models.pet import Pet
from models.button import Button
from models.config import (
    WIDTH, HEIGHT,
    WHITE, BLACK,
    PET_COLORS,
    PET_START_POSITIONS,
    PET_DEFAULT_NAMES,
    SCREAMER_LINES,
    SCREAMER_DURATION,
    DAY5_ANGRY_DURATION,
    DAY5_SILENT_DURATION,
    CRASH_DURATION,
    INPUT_X, INPUT_Y, INPUT_W, INPUT_H,
    BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
    BTN_LEFT_X, BTN_LEFT_Y, BTN_LEFT_W, BTN_LEFT_H,
    BTN_RIGHT_X, BTN_RIGHT_Y, BTN_RIGHT_W, BTN_RIGHT_H, CRASH_FULLSCREEN
)

class WarningScene(Scene):
    def enter(self, game):
        game.state.day = "Предупреждение"
        game.state.dialogue_text = []
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Я понимаю, продолжить",
                   lambda: game.change_scene(Day1Scene()))
        ]

    def draw(self, game, surf):
        surf.fill((0, 0, 0))

        font_warn  = pygame.font.SysFont("Consolas", 40, bold=True)
        font_text  = pygame.font.SysFont("Consolas", 20)
        font_small = pygame.font.SysFont("Consolas", 16)

        # заголовок
        warn = font_warn.render("⚠ ВНИМАНИЕ ⚠", True, (255, 60, 60))
        surf.blit(warn, warn.get_rect(center=(WIDTH // 2, 80)))

        # текст
        lines = [
            "Эта игра содержит:",
            "",
            "• Резкие вспышки и мерцание",
            "• Внезапные громкие звуки (скримеры)",
            "• Резкую смену изображения",
            "• Психологический хоррор",
            "• Мета-хоррор (игра обращается к вам по имени)",
            "",
            "НЕ ИГРАЙТЕ, если у вас эпилепсия,",
            "мигрени, тревожность или проблемы с сердцем.",
            "",
            "Игра безопасна для компьютера.",
            "Демо создаёт names_pets.txt на рабочем столе.",
        ]

        y = 150
        for line in lines:
            color = WHITE
            font = font_text
            if line.startswith("•"):
                color = (255, 200, 100)
            elif "НЕ ИГРАЙТЕ" in line:
                color = (255, 80, 80)
                font = font_small
            txt = font.render(line, True, color)
            surf.blit(txt, txt.get_rect(center=(WIDTH // 2, y)))
            y += 24

        # кнопка
        super().draw(game, surf)


# =========================================================
#  ДЕНЬ 1
# =========================================================
class Day1Scene(Scene):
    def enter(self, game):
        game.state.day = "День1"
        game.state.dialogue_text = [
            "День 1: Вы запускаете игру. На фальшивом компьютере появляется Глаз.",
            "Глаз: 'На сегодня всё. Яйцам нужно время. Можешь закрыть игру и прийти завтра'."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Перейти на второй день",
                   lambda: game.change_scene(Day2Scene()))
        ]


# =========================================================
#  ДЕНЬ 2 — 1-й пет
# =========================================================
class Day2Scene(Scene):
    def enter(self, game):
        game.state.day = "День2"
        if len(game.state.pets) < 1:
            game.state.pets.append(
                Pet(PET_COLORS[0], PET_START_POSITIONS[0][0],
                    PET_START_POSITIONS[0][1], kind="красный с гитарой")
            )
        game.state.dialogue_text = [
            "ДЕНЬ НОМЕР ДВА. Буквы стали красными, раздается звук 'Ммм...'",
            "Вы нажимаете на стрелочку. Яйцо ломается! Появляется красный пет с гитарой без ног.",
            "Вы перетаскиваете его. Он грустит, что один, и уходит в свою файл-комнату."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Перейти к следующему дню",
                   lambda: game.change_scene(Day3Scene()))
        ]


# =========================================================
#  ДЕНЬ 3 — 2-й пет
# =========================================================
class Day3Scene(Scene):
    def enter(self, game):
        game.state.day = "День3"
        if len(game.state.pets) < 2:
            game.state.pets.append(
                Pet(PET_COLORS[1], PET_START_POSITIONS[1][0],
                    PET_START_POSITIONS[1][1], kind="розовый бегемотик")
            )
        # сдвигаем первых двух чуть влево
        if game.state.pets:
            game.state.pets[0].x, game.state.pets[0].y = 280, 210
        if len(game.state.pets) > 1:
            game.state.pets[1].x, game.state.pets[1].y = 400, 220

        game.state.dialogue_text = [
            "День 3: Снова звуки. 1-й пет ждет у инкубатора. Вылупляется 2-й пет - розовый бегемотик.",
            "1-й пет радуется: 'Привет! Пошли знакомиться с Глазом!' и бежит.",
            "2-й пет ничего не понимает, издает сонный звук и летит за ним."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Наступил следующий день",
                   lambda: game.change_scene(Day4Scene()))
        ]


# =========================================================
#  ДЕНЬ 4 — скример
# =========================================================
class Day4Scene(Scene):
    def enter(self, game):
        game.state.day = "День4"
        if game.state.eye:
            game.state.eye.mood = "sleeping"
        game.state.dialogue_text = [
            "День 4: Никто не вылупился. Игра просит открыть ящик. Там МЯЧ. Петы играют с ним.",
            "2-й пет: 'Пошли в мою комнату, я проголодался'. Они уходят. Глаз засыпает (z z z).",
            "Вы начинаете кликать по Глазу, чтобы разбудить его..."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Кликнуть на спящего Глаза",
                   lambda: game.change_scene(ScreamerScene()))
        ]


class ScreamerScene(Scene):
    def enter(self, game):
        game.state.day = "Скример"
        game.state.dialogue_text = ["БАНГ! Экран искажается страшными цифровыми помехами!"]
        self.buttons = []
        self.timer = SCREAMER_DURATION

    def update(self, game, dt):
        self.timer -= dt
        if self.timer <= 0:
            game.change_scene(Day5Scene())

    def draw(self, game, surf):
        surf.fill(BLACK)
        for _ in range(SCREAMER_LINES):
            x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            pygame.draw.line(surf, WHITE, (x1, y1), (x2, y2), 2)


# =========================================================
#  ДЕНЬ 5 — выбор
# =========================================================
class Day5Scene(Scene):
    def enter(self, game):
        game.state.day = "День5"
        if game.state.eye:
            game.state.eye.mood = "angry"
        if len(game.state.pets) < 3:
            game.state.pets.append(
                Pet(PET_COLORS[2], 600, 210, kind="умная девочка-кошка")
            )
        game.state.dialogue_text = [
            "Глаз яростно открывается: 'ЧТО НАДО?!? Зачем разбудил?!'",
            "В инкубаторе треск. Рождается 3-й пет - умная девочка-кошка в очках. Она говорит: 'Крутые очки!'",
            "Глаз молчит и читает книгу в очках. Что вы сделаете?"
        ]
        self.buttons = [
            Button(BTN_LEFT_X, BTN_LEFT_Y, BTN_LEFT_W, BTN_LEFT_H,
                   "Наехать на него",
                   lambda: game.change_scene(Day5AngryScene())),
            Button(BTN_RIGHT_X, BTN_RIGHT_Y, BTN_RIGHT_W, BTN_RIGHT_H,
                   "Промолчать",
                   lambda: game.change_scene(Day5SilentScene())),
        ]


class Day5AngryScene(Scene):
    def enter(self, game):
        game.state.day = "ЗлостьГлаза"
        game.state.dialogue_text = [
            f"Глаз захлопывает книгу: 'ЕСЛИ НЕ ОТВЕЧАЮ, ЗНАЧИТ НЕ МОГУ, {game.get_system_name().upper()}!!!'",
            "Петы пугаются, кроме Девочки. Вы говорите 'Воу, воу...'. Все расходятся по комнатам."
        ]
        self.buttons = []
        self.timer = DAY5_ANGRY_DURATION

    def update(self, game, dt):
        self.timer -= dt
        if self.timer <= 0:
            game.change_scene(Night5Scene())


class Day5SilentScene(Scene):
    def enter(self, game):
        game.state.day = "ЗлостьГлаза"
        game.state.dialogue_text = [
            "Вы промолчали. Атмосфера накалилась. Петы тихо расходятся по своим файлам-комнатам."
        ]
        self.buttons = []
        self.timer = DAY5_SILENT_DURATION

    def update(self, game, dt):
        self.timer -= dt
        if self.timer <= 0:
            game.change_scene(Night5Scene())


# =========================================================
#  НОЧЬ 5-ГО ДНЯ
# =========================================================
class Night5Scene(Scene):
    def enter(self, game):
        game.state.day = "НочьДень5"
        if game.state.eye:
            game.state.eye.mood = "sleeping"
        game.state.dialogue_text = [
            "Спустя 3 часа... Ночь. Все файлы спят (z z z), Глаз спит. Но в комнате 3-го пета горит свет.",
            "Вы заходите. Она грустит: 'Мы смотрели кино, там убили человека. 1 и 2 пет плакали, а мне фиолетово.'",
            "'Они назвали меня бездушной...'. Вы успокаиваете девочку, едите пиццу и делаете красивое фото."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Сделать фото на память и лечь спать",
                   lambda: game.change_scene(Day6Scene()))
        ]


# =========================================================
#  ДЕНЬ 6 — 4-й пет
# =========================================================
class Day6Scene(Scene):
    def enter(self, game):
        game.state.day = "День6"
        if game.state.eye:
            game.state.eye.mood = "normal"
        if len(game.state.pets) < 4:
            game.state.pets.append(
                Pet(PET_COLORS[3], 400, 230, kind="стильный желтый бунтарь")
            )
        # расстановка в линию над окном
        positions = [(150, 210), (280, 220), (550, 210), (400, 230)]
        for i, (x, y) in enumerate(positions):
            if i < len(game.state.pets):
                game.state.pets[i].x, game.state.pets[i].y = x, y

        game.state.dialogue_text = [
            "День 6: 1 и 2 пет играют в догонялки. 3 пет читает книгу. Треск! Глаз закатывает зрачок: 'Еще один...'",
            "Рождается 4-й пет - стильный, желтый с зелеными линиями и крутой челкой. Он кланяется Девочке.",
            "Она смущается и закатывает глаза. 4-й пет весело играет со всеми. Глаз полностью игнорирует его.",
            "В конце дня Глаз приказывает: 'Завтра родится 5-й пет. Ты ДОЛЖЕН дать всем имена. Готовься'."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Наступило утро 7-го дня",
                   lambda: game.change_scene(Day7Scene()))
        ]


# =========================================================
#  ДЕНЬ 7 — 5-й пет
# =========================================================
class Day7Scene(Scene):
    def enter(self, game):
        game.state.day = "День7"
        if len(game.state.pets) < 5:
            game.state.pets.append(
                Pet(PET_COLORS[4], 650, 220, kind="скромная девочка-слоненок")
            )
        game.state.dialogue_text = [
            "День 7: Утро. Проснулись 1 и 3 пет. 1-й пет стоит на руках от скуки и ест шоколадку.",
            "Затем просыпаются все. 1, 2 и 4 пет играют в угадайку 'Кто ударил' (4 пет - вода). 3 пет поливает цветы.",
            "Вдруг треск! 4 пет шутит: 'Это новорожденный пет!'. Все смеются, даже Глаз усмехнулся.",
            "Вылупляется 5-й пет - голубая девочка с ушами слоненка. Она тихо говорит: 'О, привет...'."
        ]
        self.buttons = [
            Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                   "Построить всех в линию для ввода имён",
                   lambda: game.change_scene(NamingScene()))
        ]


# =========================================================
#  ВВОД ИМЁН
# =========================================================
class NamingScene(Scene):
    DEFAULTS = PET_DEFAULT_NAMES
    PROMPTS = [
        "Глаз кашляет: 'КХМ-КХМ! Вводи имена!'.\nВведите имя для 1-го пета (Красный, предложено: Юри):",
        "Введите имя для 2-го пета (Розовый бегемотик, предложено: Зуд):",
        "Введите имя для 3-го пета (Умная девочка-кошка, предложено: Мия):",
        "Введите имя для 4-го пета (Стильный желтый бунтарь, предложено: Рик):",
        "Введите имя для 5-го пета (Скромная девочка-слоненок, предложено: Лулу):",
    ]

    def enter(self, game):
        game.state.day = "ВводИмен"
        game.state.input_text = ""
        if game.state.current_pet_naming >= 5:
            game.state.current_pet_naming = 0
        self.update_prompt(game)

    def update_prompt(self, game):
        idx = game.state.current_pet_naming
        if idx < 5:
            game.state.dialogue_text = self.PROMPTS[idx].split('\n')
            self.buttons = [
                Button(BTN_CENTER_X, BTN_CENTER_Y, BTN_CENTER_W, BTN_CENTER_H,
                       "Подтвердить", lambda: self.confirm_name(game))
            ]
        else:
            game.change_scene(CrashScene())

    def confirm_name(self, game):
        idx = game.state.current_pet_naming
        text = game.state.input_text.strip()
        name = text if text else self.DEFAULTS[idx]

        game.state.names[idx] = name
        if idx < len(game.state.pets):
            game.state.pets[idx].name = name

        game.state.current_pet_naming += 1
        game.state.input_text = ""
        self.update_prompt(game)

    def handle_event(self, game, event):
        super().handle_event(game, event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game.state.input_text = game.state.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.confirm_name(game)
            elif event.unicode and event.unicode.isprintable():
                if len(game.state.input_text) < 20:
                    game.state.input_text += event.unicode

    def draw(self, game, surf):
        # поле ввода — поверх диалогового окна
        pygame.draw.rect(surf, WHITE, (INPUT_X, INPUT_Y, INPUT_W, INPUT_H), 2)
        txt = game.font.render(game.state.input_text, True, WHITE)
        surf.blit(txt, (INPUT_X + 10, INPUT_Y + 5))
        super().draw(game, surf)


# =========================================================
#  КРАХ СИСТЕМЫ
# =========================================================
class CrashScene(Scene):
    PHASE_BSOD   = 0
    PHASE_STORY  = 1
    PHASE_JOKE   = 2
    PHASE_DONE   = 3

    PHASE_BSOD_DURATION  = 10000
    PHASE_STORY_DURATION = 5000
    PHASE_JOKE_DURATION  = 2000

    def enter(self, game):
        game.state.day = "КрахСистемы"
        if game.state.eye:
            game.state.eye.mood = "broken"

        # запоминаем старое окно, чтобы вернуть
        self.prev_screen = game.screen
        self.prev_size   = (WIDTH, HEIGHT)

        # переключаем в fullscreen
        if CRASH_FULLSCREEN:
            game.screen = pygame.display.set_mode(
                (0, 0), pygame.FULLSCREEN
            )
            self.fs_size = game.screen.get_size()
        else:
            self.fs_size = self.prev_size

        # --- тексты ---
        self.story_text = [
            f"Глаз издает жуткий смех: 'Имена приняты! Ловушка захлопнулась, {game.get_system_name()}!'",
            "Экран заливается кровью. В корневой папке твоей системы создаются файлы петов...",
            "ЭТА ИГРА — БОЛЬШЕ НЕ ИГРА.",
        ]

        self.bsod_lines = [
            "Ваш компьютер столкнулся с проблемой и должен быть перезагружен.",
            "Мы собираем данные об ошибке...",
            "",
            "STOP CODE: BLIND_SPOT_TRAP",
            f"Ошибка вызвана: {game.get_system_name().upper()}",
            f"Номер ошибки: 0x{random.randint(0x1000, 0xFFFF):04X}",
        ]

        self.joke_lines = [
            "ШУТКА. :)",
            "",
            "Никакие файлы не созданы.",
            "Твой компьютер в порядке.",
            "",
            "Но имена петов ты уже не забудешь.",
        ]

        self.buttons = []
        self.phase = self.PHASE_BSOD
        self.timer = self.PHASE_BSOD_DURATION
        self.blink = 0

        # шрифты под fullscreen — крупнее
        self.font_bsod   = pygame.font.SysFont("Consolas", 28)
        self.font_sad    = pygame.font.SysFont("Consolas", 140, bold=True)
        self.font_title  = pygame.font.SysFont("Consolas", 72, bold=True)
        self.font_small  = pygame.font.SysFont("Consolas", 22)

    def update(self, game, dt):
        self.timer -= dt
        self.blink += dt

        if self.timer <= 0:
            if self.phase == self.PHASE_BSOD:
                self.phase = self.PHASE_STORY
                self.timer = self.PHASE_STORY_DURATION
            elif self.phase == self.PHASE_STORY:
                self.phase = self.PHASE_JOKE
                self.timer = self.PHASE_JOKE_DURATION
            elif self.phase == self.PHASE_JOKE:
                self.phase = self.PHASE_DONE

                # вернуть окно
                if CRASH_FULLSCREEN:
                    game.screen = pygame.display.set_mode(self.prev_size)

                SaveManager.create_desktop_file(game)
                game.save_manager.delete()
                game.running = False

    def draw(self, game, surf):
        if self.phase == self.PHASE_BSOD:
            self._draw_bsod(surf)
        elif self.phase == self.PHASE_STORY:
            self._draw_story(game, surf)
        elif self.phase == self.PHASE_JOKE:
            self._draw_joke(game, surf)

    # ---------- ФАЗА 1: BSOD ----------
    def _draw_bsod(self, surf):
        W, H = self.fs_size
        surf.fill((0, 0, 170))

        # ":(" — огромный, слева сверху
        sad = self.font_sad.render(":(", True, WHITE)
        surf.blit(sad, (W * 0.08, H * 0.10))

        # основной текст — под смайликом
        y = int(H * 0.42)
        for line in self.bsod_lines:
            if line:
                txt = self.font_bsod.render(line, True, WHITE)
                surf.blit(txt, (int(W * 0.08), y))
            y += 42

        # прогресс-бар внизу
        progress = 1.0 - (self.timer / self.PHASE_BSOD_DURATION)
        bar_x = int(W * 0.08)
        bar_y = int(H * 0.88)
        bar_w = int(W * 0.55)
        bar_h = 26

        pygame.draw.rect(surf, WHITE, (bar_x, bar_y, bar_w, bar_h), 3)
        pygame.draw.rect(surf, WHITE,
                         (bar_x + 4, bar_y + 4,
                          int((bar_w - 8) * progress), bar_h - 8))

        pct = self.font_small.render(f"{int(progress * 100)}%", True, WHITE)
        surf.blit(pct, (bar_x + bar_w + 30, bar_y))

    # ---------- ФАЗА 2: текст ловушки ----------
    def _draw_story(self, game, surf):
        W, H = self.fs_size
        surf.fill((0, 0, 0))

        # пульсирующая красная рамка
        pulse = int(abs((self.blink / 200) % 2 - 1) * 100 + 100)
        pygame.draw.rect(surf, (pulse, 0, 0), (0, 0, W, H), 12)

        # текст по центру, крупный
        font_big = pygame.font.SysFont("Consolas", 32)
        y = int(H * 0.30)
        for line in self.story_text:
            words = line.split(' ')
            current = ""
            for word in words:
                if len(current) + len(word) + 1 <= 60:
                    current += word + " "
                else:
                    txt = font_big.render(current.strip(), True, WHITE)
                    surf.blit(txt, (int(W * 0.10), y))
                    y += 44
                    current = word + " "
            if current:
                txt = font_big.render(current.strip(), True, WHITE)
                surf.blit(txt, (int(W * 0.10), y))
                y += 44
            y += 30

        # мигающая надпись
        if (self.blink // 400) % 2 == 0:
            warn_font = pygame.font.SysFont("Consolas", 40, bold=True)
            warn = warn_font.render(">>> НЕ ЗАКРЫВАЙ ИГРУ <<<", True, (255, 50, 50))
            surf.blit(warn, warn.get_rect(center=(W // 2, int(H * 0.85))))

    # ---------- ФАЗА 3: шутка ----------
    def _draw_joke(self, game, surf):
        W, H = self.fs_size
        surf.fill((0, 0, 0))

        base = [
            "ОШИБКА ВОССТАНОВЛЕНИЯ",
            "",
            "Файлы петов созданы.",
            f"Владелец: {game.get_system_name()}",
            "",
            "Продолжение следует...",
        ]

        y = int(H * 0.30)
        for i, line in enumerate(base):
            # каждая строка портится со временем
            corrupted = self._corrupt(line, self.blink // 100 + i)
            font = self.font_bsod
            color = WHITE if i != 0 else (255, 50, 50)
            txt = font.render(corrupted, True, color)
            surf.blit(txt, (int(W * 0.10), y))
            y += 50

        # внизу — растущий курсор
        cursor = "_" if (self.blink // 300) % 2 == 0 else " "
        cur_txt = self.font_bsod.render(cursor, True, WHITE)
        surf.blit(cur_txt, (int(W * 0.10), y + 30))

    def _corrupt(self, text, seed):
        """Заменяет часть символов на случайные — как повреждённый файл."""
        import random
        rng = random.Random(seed)
        glitch = "▓▒░█▄▀#@$%&?"
        result = []
        for ch in text:
            if ch != " " and rng.random() < 0.08:  # 8% символов ломаются
                result.append(rng.choice(glitch))
            else:
                result.append(ch)
        return "".join(result)


# =========================================================
#  РЕЕСТР СЦЕН
# =========================================================
SCENE_REGISTRY = {
    "День1": Day1Scene,
    "День2": Day2Scene,
    "День3": Day3Scene,
    "День4": Day4Scene,
    "Скример": ScreamerScene,
    "День5": Day5Scene,
    "ЗлостьГлаза": Day5SilentScene,
    "НочьДень5": Night5Scene,
    "День6": Day6Scene,
    "День7": Day7Scene,
    "ВводИмен": NamingScene,
    "КрахСистемы": CrashScene,
}