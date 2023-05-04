from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class Jerk(Skill):
    _name: str = 'рывок'
    _stamina: float = 7
    _damage: float = 10

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> float:
        return self._stamina

    @property
    def damage(self) -> float:
        return self._damage

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использовал {self.name} и нанёс {self.damage} урона {self.target.name}"


class Stealing(Skill):
    _name: str = 'кражу'
    _stamina: float = 7
    _damage: float = 1
    _steal_stamina = 6

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> float:
        return self._stamina

    @property
    def damage(self) -> float:
        return self._damage

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        if self.target.stamina >= self._steal_stamina:
            self.target.stamina -= self._steal_stamina
            return f"{self.user.name} использовал {self.name}, нанёс {self.damage} урон и" \
                   f" украл {self._steal_stamina} стамины у {self.target.name}"
        else:
            self.target.stamina = 0
            return f"{self.user.name} использовал {self.name}, нанёс {self.damage} урон и" \
                   f" украл последнею стамину у {self.target.name}"
