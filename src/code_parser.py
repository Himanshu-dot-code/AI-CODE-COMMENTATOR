 
import ast

def extract_code_info(code):
    """Extracts functions and classes from Python code."""
    tree = ast.parse(code)
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return functions, classes
