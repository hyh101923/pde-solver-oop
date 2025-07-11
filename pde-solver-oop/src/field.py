from .mesh import Mesh

class Field(Mesh):
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)

    def __str__(self) -> str:
        pass