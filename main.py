# A Python Program to convert LaTeX to python code or vice versa.


def latex_to_py(latex, use_standard=True):
    """Converts LaTeX to python code."""
    latex = latex.replace("\\", "\\\\")
    latex = latex.replace("{", "{{")
    latex = latex.replace("}", "}}")
    latex = latex.replace("(", "{")
    latex = latex.replace(")", "}")
    latex = latex.replace("^", "**")
    latex = latex.replace("sqrt", "math.sqrt")
    latex = latex.replace("frac", "Fraction")
    latex = latex.replace("pi", "math.pi")
    latex = latex.replace("sin", "math.sin")
    latex = latex.replace("cos", "math.cos")
    latex = latex.replace("tan", "math.tan")
    latex = latex.replace("cot", "math.cot")
    latex = latex.replace("sec", "math.sec")
    latex = latex.replace("csc", "math.csc")
    latex = latex.replace("log", "math.log")
    latex = latex.replace("ln", "math.ln")
    latex = latex.replace("e", "math.e")
    latex = latex.replace("lim", "Limit")
    latex = latex.replace("int", "Integral")
    latex = latex.replace("sum", "Sum")
    latex = latex.replace("prod", "Product")
    latex = latex.replace("to", "to")
    latex = latex.replace("infty", "oo")
    latex = latex.replace("infinity", "oo")
    latex = latex.replace("in", "in")
    return latex


if __name__ == "__main__":
    latex = 
    print(latex_to_py(latex))