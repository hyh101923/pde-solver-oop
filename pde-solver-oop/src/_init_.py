# 基础几何与数据类
from .mesh import Mesh
from .field import Field
from .source import Source

# PDE核心类
from .pde import PDE
from .elliptic import EllipticPDE, LaplaceEq
from .parabolic import ParabolicPDE

# 求解器类
from .solver import PDESolver, FiniteDifferenceSolver

# 工厂类
from .factory import PDEFactory