from .pde import PDE

class PDESolver:
    def __init__(self, method: str, tolerance: float = 1e-6):
        pass

    def set_discretization_method(self, method: str):
        pass

    def solve(self, pde: PDE):
        pass

class FiniteDifferenceSolver(PDESolver):
    def __init__(self, grid_size: tuple, space_step: tuple):
        super().__init__("finite_difference")

    def solve(self, pde: PDE):
        pass