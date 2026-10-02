# =========================================================
#  ОКНО
# =========================================================
WIDTH, HEIGHT = 800, 600
FPS = 60
CAPTION = "Слепая зона (Blind Spot) - ПОЛНАЯ ДЕМО ВЕРСИЯ"


# =========================================================
#  ЦВЕТА
# =========================================================
BLUE       = (30, 100, 200)
DARK_BLUE  = (10, 20, 50)
RED        = (150, 0, 0)
DARK_BOX   = (20, 20, 20)
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)

# глаз
EYE_WHITE  = (255, 255, 255)
EYE_BLUE   = (0, 150, 255)
EYE_BLACK  = (0, 0, 0)
EYE_RED    = (255, 0, 0)

# кнопки
BUTTON_BG     = (50, 50, 50)
BUTTON_BORDER = WHITE
BUTTON_TEXT   = WHITE

# петы
PET1_COLOR = (255, 50, 50)
PET2_COLOR = (255, 150, 150)
PET3_COLOR = (50, 200, 50)
PET4_COLOR = (255, 255, 0)
PET5_COLOR = (100, 150, 255)
PET_RADIUS = 25
PET_COLORS = [PET1_COLOR, PET2_COLOR, PET3_COLOR, PET4_COLOR, PET5_COLOR]


# =========================================================
#  ШРИФТЫ
# =========================================================
FONT_NAME       = "Arial"
FONT_SIZE       = 18
FONT_SIZE_LARGE = 22
FONT_BOLD       = True


# =========================================================
#  ГЛАЗ
# =========================================================
EYE_X = 400
EYE_Y = 110
EYE_RADIUS_OUTER       = 50
EYE_RADIUS_INNER       = 20
EYE_RADIUS_PUPIL       = 10
EYE_RADIUS_ANGRY       = 70
EYE_RADIUS_ANGRY_PUPIL = 15


# =========================================================
#  ВЕРХНЯЯ ПАНЕЛЬ
# =========================================================
TOPBAR_H        = 40
TOPBAR_BG       = (15, 15, 15)
TOPBAR_BTN_W    = 110
TOPBAR_BTN_H    = 28
TOPBAR_BTN_Y    = 6
TOPBAR_BTN_GAP  = 8
TOPBAR_BTN_X0   = 10

TOPBAR_MENU_X   = TOPBAR_BTN_X0
TOPBAR_SAVE_X   = TOPBAR_MENU_X + TOPBAR_BTN_W + TOPBAR_BTN_GAP
TOPBAR_LOAD_X   = TOPBAR_SAVE_X + TOPBAR_BTN_W + TOPBAR_BTN_GAP


# =========================================================
#  ОВЕРЛЕЙ МЕНЮ
# =========================================================
MENU_OVERLAY_BG     = (0, 0, 0, 200)
MENU_PANEL_COLOR    = (25, 25, 35)
MENU_PANEL_X        = 150
MENU_PANEL_Y        = 80
MENU_PANEL_W        = 500
MENU_PANEL_H        = 440
MENU_TEXT_X         = MENU_PANEL_X + 30
MENU_TEXT_Y         = MENU_PANEL_Y + 30
MENU_LINE_H         = 26
MENU_CLOSE_BTN_X    = MENU_PANEL_X + MENU_PANEL_W // 2 - 80
MENU_CLOSE_BTN_Y    = MENU_PANEL_Y + MENU_PANEL_H - 55
MENU_CLOSE_BTN_W    = 160
MENU_CLOSE_BTN_H    = 35


# =========================================================
#  ТОСТЫ
# =========================================================
TOAST_DURATION  = 1500
TOAST_X         = 560
TOAST_Y         = 8


# =========================================================
#  ДИАЛОГОВОЕ ОКНО
# =========================================================
DIALOG_BOX_Y      = 280
DIALOG_BOX_H      = 320
DIALOG_TEXT_X     = 20
DIALOG_TEXT_Y     = 300
DIALOG_LINE_H     = 24
DIALOG_MAX_CHARS  = 88


# =========================================================
#  ПОЛЕ ВВОДА ИМЕНИ
# =========================================================
INPUT_X        = 300
INPUT_Y        = 470
INPUT_W        = 200
INPUT_H        = 30
INPUT_PADDING  = 10
INPUT_MAX_LEN  = 20


# =========================================================
#  КНОПКИ
# =========================================================
BTN_CENTER_X   = 250
BTN_CENTER_Y   = 540
BTN_CENTER_W   = 300
BTN_CENTER_H   = 35

BTN_LEFT_X     = 150
BTN_LEFT_Y     = 540
BTN_LEFT_W     = 200
BTN_LEFT_H     = 35

BTN_RIGHT_X    = 450
BTN_RIGHT_Y    = 540
BTN_RIGHT_W    = 200
BTN_RIGHT_H    = 35


# =========================================================
#  ПЕТЫ — над диалоговым окном (DIALOG_BOX_Y = 280)
# =========================================================
PET_START_POSITIONS = [
    (150, 210),
    (280, 220),
    (550, 210),
    (400, 230),
    (650, 220),
]

PET_DEFAULT_NAMES = ["Юри", "Зуд", "Мия", "Рик", "Лулу"]


# =========================================================
#  СОХРАНЕНИЯ
# =========================================================
SAVE_FILE_PATTERN = "save_{slot}.json"
SAVE_SLOT_DEFAULT = 1
SAVE_VERSION      = 1

# состояния, которые НЕ сохраняются
UNSAVEABLE_STATES = [
    "Скример",
    "ЗлостьГлаза",
    "КрахСистемы",
]


# =========================================================
#  ТАЙМЕРЫ (мс)
# =========================================================
SCREAMER_DURATION      = 1000
DAY5_ANGRY_DURATION    = 4000
DAY5_SILENT_DURATION   = 2000
CRASH_DURATION         = 5000


# =========================================================
#  СОСТОЯНИЯ
# =========================================================
STATE_DAY1     = "День1"
STATE_DAY2     = "День2"
STATE_DAY3     = "День3"
STATE_DAY4     = "День4"
STATE_SCREAMER = "Скример"
STATE_DAY5     = "День5"
STATE_ANGRY    = "ЗлостьГлаза"
STATE_NIGHT5   = "НочьДень5"
STATE_DAY6     = "День6"
STATE_DAY7     = "День7"
STATE_NAMING   = "ВводИмен"
STATE_CRASH    = "КрахСистемы"

# =========================================================
#  FULLSCREEN (крах системы)
# =========================================================
CRASH_FULLSCREEN = True     # переключать ли окно в fullscreen на крахе
CRASH_HIDE_UI    = True     # прятать topbar / диалог / кнопки во время краха

# =========================================================
#  ПРОЧЕЕ
# =========================================================
FALLBACK_USERNAME = "Игрок"
SCREAMER_LINES    = 200