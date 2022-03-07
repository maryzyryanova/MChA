import sympy
import iterations_method
import newton_method

(x, y) = sympy.symbols('x y')
eps = 0.0001
f1 = sympy.tan(x*y + 0.1) - x
f2 = 0.8*x**2 + 2*y**2 - 1

plots = sympy.plot_implicit(sympy.Eq(f1, 0), (x, -2, 2), (y, -2, 2), line_color = "blue", show = False)
plots.extend(sympy.plot_implicit(sympy.Eq(f2, 0), (x, -2, 2), (y, -2, 2), line_color = "red", show = False))
plots.show()

first_approximation = [0.35, 0.65]
print("1. Simple iterations method: ")
iterations_method.print_result(first_approximation, eps)
print("2. Newton method: ")
newton_method.print_result(first_approximation, eps)
