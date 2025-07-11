from .pde import PDE
from .field import Field

class EllipticPDE(PDE):
    def __init__(self, mesh: Mesh, source: Source):
        super().__init__(mesh, source)

    def set_elliptic_parameters(self, params: dict):
        pass

    def get_solution_domain(self):
        pass

class LaplaceEq(EllipticPDE):
    def __init__(self, mesh: Mesh, source: Source):
        super().__init__(mesh, source)

    def build_diff_matrix(self):
        pass

    def solve(self):
        pass

    def save_fig(self, filename: str):
        pass