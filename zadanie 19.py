class Matrix:
    def __init__(self, macierz):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in macierz.splitlines()
        ]
    
    def __repr__(self):
        return '\n'.join([
            (' '.join([str(i) for i in row]))
            for row in self.matrix
        ])
    
    def row(self, number):
        return self.matrix[number]

    def column(self, kolumna):
        lista = []
        for row in self.matrix:
            lista.append(row[kolumna])
        return lista

m = Matrix('3 4\n5 6\n7 8')
print(m.matrix)
print(m.__repr__)
print(m.row(2))
print(m.column(1))