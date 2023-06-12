# A Python Program to convert LaTeX to python code or vice versa.
from process_latex import process_sympy

def latex_to_py(latex, use_standard=True):
    """Converts LaTeX to Python code."""
    sympy = process_sympy(latex)
    # TODO: Convert sympy to python code
    return sympy

def py_to_latex(py):
    """Converts Python code to LaTeX."""
    pass

if __name__ == "__main__":
    latex = "\\delta \\ln{(R_{avg})}=\\sqrt{\\left(\\frac{\\partial \\ln{R_{avg}}}{\\partial R_{avg}}\\delta R_{avg} \\right)^2}"
    print(latex_to_py(latex))