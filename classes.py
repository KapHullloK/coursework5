from dataclasses import dataclass

from skills import Skill, Jerk, Stealing


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="warrior",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.8,
    armor=1.1,
    skill=Jerk()
)

ThiefClass = UnitClass(
    name="thief",
    max_health=50.0,
    max_stamina=40.0,
    attack=0.6,
    stamina=0.9,
    armor=1.4,
    skill=Stealing()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
