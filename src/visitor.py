class Visitor():
    def __init__(self, components):
        self.components = components

    def __default__(self, ast, env):
        raise

    def component(self, ast, env):
        visited = [self.visit(sub_ast, env) for sub_ast in ast.children]
        return ''.join(visited)

    def component_ref(self, ast, env):
        key = self.visit(ast.children[0], env)
        component = self.components[key]
        return self.visit(component, env)

    def component_name(self, ast, env):
        return ast.children[0].value

    def string(self, ast, env):
        string = ''.join([child.value for child in ast.children])
        return string

    def visit(self, ast, env):
        f = getattr(self, ast.data, self.__default__)

        try:
            f(ast, env)
        except:
            print(ast.data)
            raise

        return f(ast, env)
