from src import Mesh, Source, PDEFactory, FiniteDifferenceSolver

def main():
    mesh = Mesh(0.0, 0.01, 100)
    source = Source(0.0, 0.01, 100)
    source.make_gaussian(pos=0.5, sigma=0.1)

    # 创建PDE和求解器
    pde = PDEFactory.create_pde("laplace", mesh, source)
    solver = PDEFactory.create_solver("finite_difference", grid_size=(100,), space_step=(0.01,))

    # 求解方程
    solver.solve(pde)
    pde.save_fig("solution.png")

if __name__ == "__main__":
    main()