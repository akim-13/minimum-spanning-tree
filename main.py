import sys
import logging
from logging import debug as D

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s] -----> [%(lineno)s]: %(msg)s')

MAX_INT = sys.maxsize


def main():
    vertices = input_vertices()
    edges = input_edges(vertices)


def input_vertices():
    inp_vertices = input('Please input vertices (A-Z): ')
    vertices = get_list_of_vertices_from_string(inp_vertices)
    vertices = eliminate_duplicates_from_list(vertices)
    print_vertices(vertices)
    return vertices


def get_list_of_vertices_from_string(string):
    vertices = []
    if type(string) is not str:
        raise TypeError(f'"{string}" is "{type(string)}", not a string.')

    for char in string:
        vertex = Vertex(char)
        if vertex.is_valid():
            vertices.append(vertex.get_name())
        else:
            print(f'WARNING: Invalid vertex "{char}". Skipping...')

    return vertices


def eliminate_duplicates_from_list(list_):
    return list(dict.fromkeys(list_))


def print_vertices(vertices):
    print('\nEntered vertices:', end=' ')
    vertices.sort()
    for vertex in vertices:
        print(vertex, end=' ')
    print('\n')


def input_edges(vertices):
    edges = []
    while True:
        inp_edge = input('Enter an edge (AB-YZ): ')
        if inp_edge == 'q' or inp_edge == 'Q': 
            break

        edge = Edge(inp_edge, None)

        if not edge.name_is_valid():
            print(f'ERROR: invalid edge "{inp_edge}"')
            continue

        edge_name = edge.get_name()

        if not edge.exists(vertices):
            print(f'ERROR: "{edge_name}" does not exist.')
            continue

        if edge_is_duplicate(edge_name, edges):
            print(f'ERROR: edge {edge_name} already exists.')
            continue

        inp_length = input(f'Enter {edge_name} length: ')

        if not inp_length.isnumeric():
            print(f'ERROR: edge length must be an integer.')
            continue

        try:
            edge.set_length(inp_length)
        except ValueError as e:
            print(e)
            continue

        edges.append(edge)

    print_edges(edges)
    return edges


def edge_is_duplicate(edge_name, existing_edges):
    for existing_edge in existing_edges:
        existing_edge_name = existing_edge.get_name()
        if edge_name == existing_edge_name:
            return True

    return False


def print_edges(edges):
    print('\nEntered edges:', end=' ')
    for edge in edges:
        name = edge.get_name()
        length = edge.get_length()
        print(f'[{name}]={length}', end=' ')


class Vertex():
    def __init__(self, name):
        self.name = str(name)


    def get_name(self):
        if self.is_valid():
            return self.__capitilize()
        else:
            raise ValueError(f'Invalid vertex "{self.name}".')


    def is_valid(self):
        if self.name.isalpha():
            return True
        else:
            return False


    def __capitilize(self):
        return self.name.upper()


class Edge():
    def __init__(self, string, length):
        try:
            string = string.upper()
        except:
            pass
        self.name = string
        self.length = length


    def get_name(self):
        if self.name_is_valid():
            vertices = self.get_vertices()
            return vertices[0] + vertices[1]
        else:
            raise ValueError(f'Invalid edge name "{self.name}".')


    def get_length(self):
        if self.length_is_valid():
            return self.length
        else:
            raise ValueError(f'Invalid edge length "{self.length}".')


    def get_vertices(self):
        if self.name_is_valid():
            vertices = [ self.name[0], self.name[1] ] 
            vertices.sort()
            return vertices
        else:
            raise ValueError(f'Invalid edge "{self.name}".')


    def set_length(self, length):
        self.length = length
        if not self.length_is_valid():
            raise ValueError(f'Invalid length "{length}".')


    def length_is_valid(self):
        if self.length.isnumeric():
            return True
        else:
            return False


    def name_is_valid(self):
        if len(self.name)==2 and self.name.isalpha():
            return True
        else:
            return False


    def exists(self, vertices):
        vertex_1 = self.get_vertices()[0]
        vertex_2 = self.get_vertices()[1]
        if (vertex_1 and vertex_2) in vertices:
            return True
        else:
            return False


if __name__ == '__main__':
    main()
