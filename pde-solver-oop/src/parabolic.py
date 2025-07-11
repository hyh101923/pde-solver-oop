from .pde import PDE

class ParabolicPDE(PDE):
    def __init__(self, mesh: Mesh, source: Source):
        super().__init__(mesh, source)

    def set_time_parameters(self, step: float, time_range: tuple):
        pass

    def get_solution_domain(self):
        pass