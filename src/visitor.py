class Visitor():
    def __init__(self, components):
        self.components = components

    def __default__(self, ast, env):
        raise

    def component(self, ast, env):
        return ''.join([self.visit(child_ast, env) for child_ast in ast.children])

    def element(self, ast, env):
        key = self.visit(ast.children[0], env)
        return self.visit(self.components[key], env)

    def expr(self, ast, env):
        return self.visit(ast.children[1], env)

    def identifier(self, ast, env):
        return ''.join([child.value for child in ast.children])

    def text(self, ast, env):
        return ''.join([child.value for child in ast.children])

    def string_literal(self, ast, env):
        return ast.children[0].value

    def visit(self, ast, env):
        try:
            f = getattr(self, ast.data)
        except Exception as e:
            print(ast.data)
            raise e

        f(ast, env)

        return f(ast, env)
