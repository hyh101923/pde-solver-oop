from .mesh import Mesh
from .source import Source

class PDE:
    def __init__(self, mesh: Mesh, source: Source):
        pass

    def set_boundary_conditions(self, conditions: dict):
        pass

    def set_coefficients(self, coeffs: dict):
        pass

    def get_solution_domain(self):
        pass