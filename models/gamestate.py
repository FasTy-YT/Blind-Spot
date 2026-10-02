from models.pet import Pet
from models.eye import Eye
from models.config import PET_DEFAULT_NAMES, SAVE_VERSION


class GameState:
    def __init__(self):
        self.day = "День1"
        self.dialogue_text = []
        self.names = ["", "", "", "", ""]
        self.current_pet_naming = 0
        self.input_text = ""
        self.pets = []          # список Pet
        self.eye = Eye()        # всегда есть

    def to_dict(self):
        return {
            "day": self.day,
            "dialogue_text": self.dialogue_text,
            "names": self.names,
            "current_pet_naming": self.current_pet_naming,
            "pets": [p.to_dict() for p in self.pets],
            "eye": self.eye.to_dict() if self.eye else None,
            "version": SAVE_VERSION,
        }

    @classmethod
    def from_dict(cls, data):
        gs = cls()
        gs.day = data.get("day", "День1")
        gs.dialogue_text = data.get("dialogue_text", [])
        gs.names = data.get("names", ["", "", "", "", ""])
        gs.current_pet_naming = data.get("current_pet_naming", 0)
        gs.pets = [Pet.from_dict(p) for p in data.get("pets", [])]
        eye_data = data.get("eye")
        gs.eye = Eye.from_dict(eye_data) if eye_data else Eye()
        return gs