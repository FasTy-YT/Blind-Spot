import pygame
from models.config import (
    EYE_X, EYE_Y,
    EYE_RADIUS_OUTER, EYE_RADIUS_INNER, EYE_RADIUS_PUPIL,
    EYE_RADIUS_ANGRY, EYE_RADIUS_ANGRY_PUPIL,
    EYE_WHITE, EYE_BLUE, EYE_BLACK, EYE_RED, WHITE,
)


class Eye:
    def __init__(self, x=EYE_X, y=EYE_Y):
        self.x = x
        self.y = y
        self.mood = "normal"  # normal / sleeping / angry / broken

    def to_dict(self):
        return {"x": self.x, "y": self.y, "mood": self.mood}

    @classmethod
    def from_dict(cls, d):
        e = cls(d["x"], d["y"])
        e.mood = d["mood"]
        return e

    def draw(self, surf, font=None):
        if self.mood in ("angry", "broken"):
            pygame.draw.circle(surf, EYE_BLACK, (self.x, self.y), EYE_RADIUS_ANGRY)
            pygame.draw.circle(surf, EYE_RED, (self.x, self.y), EYE_RADIUS_ANGRY_PUPIL)
        else:
            pygame.draw.circle(surf, EYE_WHITE, (self.x, self.y), EYE_RADIUS_OUTER)
            pygame.draw.circle(surf, EYE_BLUE, (self.x, self.y), EYE_RADIUS_INNER)
            pygame.draw.circle(surf, EYE_BLACK, (self.x, self.y), EYE_RADIUS_PUPIL)

        if self.mood == "sleeping" and font:
            zzz = font.render("z z z", True, WHITE)
            surf.blit(zzz, (self.x + 60, self.y - 40))