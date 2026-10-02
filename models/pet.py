from models.config import WHITE, WIDTH, HEIGHT, PET_COLORS, FONT_SIZE, BLACK, PET_RADIUS
import pygame
from pygame import font

class Pet:
    def __init__(self, color, x, y, name="", kind=""):
        self.color = color
        self.x = x
        self.y = y
        self.name = name
        self.kind = kind

    def to_dict(self):
        return {
            "color": list(self.color),
            "x": self.x,
            "y": self.y,
            "name": self.name,
            "kind": self.kind,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            color=tuple(d["color"]),
            x=d["x"],
            y=d["y"],
            name=d.get("name", ""),
            kind=d.get("kind", ""),
        )

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), PET_RADIUS)
