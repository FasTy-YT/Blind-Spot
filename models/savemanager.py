import json
import os
from models.gamestate import GameState
from models.config import SAVE_FILE_PATTERN, SAVE_SLOT_DEFAULT, SAVE_VERSION
import datetime


class SaveManager:
    def __init__(self, slot=SAVE_SLOT_DEFAULT):
        self.slot = slot
        self.filename = SAVE_FILE_PATTERN.format(slot=slot)

    def exists(self):
        return os.path.exists(self.filename)

    def save(self, game_state):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(game_state.to_dict(), f, ensure_ascii=False, indent=2)
            print(f"[Сохранено в {self.filename}]")
            return True
        except Exception as e:
            print(f"[Ошибка сохранения]: {e}")
            return False

    def load(self):
        if not self.exists():
            print(f"[Файл {self.filename} не найден]")
            return None

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            if data.get("version", 1) != SAVE_VERSION:
                print("[Несовместимая версия сейва]")
                return None

            return GameState.from_dict(data)
        except Exception as e:
            print(f"[Ошибка загрузки]: {e}")
            return None

    def delete(self):
        if self.exists():
            os.remove(self.filename)
            print(f"[Сейв {self.filename} удалён]")
    
    def create_desktop_file(game):
        """Создаёт names_pets.txt на рабочем столе."""
        try:
            # путь к рабочему столу кроссплатформенно
            if os.name == "nt":  # Windows
                desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
            else:  # Linux / macOS
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")

            if not os.path.exists(desktop):
                desktop = os.path.expanduser("~")  # fallback

            path = os.path.join(desktop, "names_pets.txt")

            content = [
                "// ФАЙЛ СОЗДАН АВТОМАТИЧЕСКИ //",
                "// Игра: Слепая зона //",
                "",
                f"Владелец: {game.get_system_name()}",
                f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "",
                "Имена петов:",
            ]
            for i, name in enumerate(game.state.names, 1):
                content.append(f"  {i}. {name}")

            content.append("")
            content.append("Они запомнили эти имена.")
            content.append("")
            content.append("")
            content.append("")
            content.append("")
            content.append("")
            content.append("")
            content.append("")
            content.append("я тебя вижу ...")

            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(content))

            print(f"[Файл создан: {path}]")
        except Exception as e:
            print(f"[Не удалось создать файл: {e}]")