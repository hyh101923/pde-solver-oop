from .mesh import Mesh

class Source(Mesh):
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)

    def make_sin(self, omega: float):
        pass

    def make_gaussian(self, pos: float, sigma: float):
        pass

    def __str__(self) -> str:
        pass