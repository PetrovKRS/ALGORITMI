from __future__ import annotations
from typing import Optional


class Spaceman:

    def __init__(
            self,
            name: str,
            space_experience: int,
            father: Optional[Spaceman] = None,
            mother: Optional[Spaceman] = None,
    ):
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


class DynastyExperienceCounter:

    def __init__(self, spaceman: Spaceman):
        self.root = spaceman
        self.total_experience: int = 0
        self.father = spaceman.father
        self.mother = spaceman.mother

    def count_dynasty_experience(self, node):
        # Доработайте метод, чтобы он считал
        # суммарный опыт династии космонавтов.
        if self.total_experience == 0:
            self.total_experience += self.root.space_experience
        if node.father:
            self.total_experience += node.father.space_experience
            self.count_dynasty_experience(node.father)
        if node.mother:
            self.total_experience += node.mother.space_experience
            self.count_dynasty_experience(node.mother)

        return self.total_experience


yu_a_tatarin = Spaceman(
    name='Юрий Алексеевич Макарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Макарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)

counter = DynastyExperienceCounter(yu_a_tatarin)
result = counter.count_dynasty_experience(yu_a_tatarin)
print(result)
