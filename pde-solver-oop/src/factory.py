from .pde import PDE
from .elliptic import EllipticPDE, LaplaceEq
from .parabolic import ParabolicPDE
from .solver import PDESolver, FiniteDifferenceSolver
from .mesh import Mesh
from .source import Source

class PDEFactory:
    @staticmethod
    def create_pde(pde_type: str, mesh: Mesh, source: Source) -> PDE:
        pass

    @staticmethod
    def create_solver(solver_type: str, **kwargs) -> PDESolver:
        pass