import sympy

(x, y) = sympy.symbols('x y')
eps = 1e-4
f1 = sympy.tan(x*y + 0.1) - x
f2 = 0.8*x**x + 2*y**2 - 1

plots = sympy.plot_implicit(sympy.Eq(f1, 0), (x, -2, 2), (y, -2, 2), line_color = "blue", show = False)
plots.extend(sympy.plot_implicit(sympy.Eq(f2, 0), (x, -2, 2), (y, -2, 2), line_color = "red", show = False))
plots.show()

first_approximation = [0.2, 0.4]

