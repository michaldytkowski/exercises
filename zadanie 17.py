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
    

m = Matrix('3 4\n5 6\n7 8')
print(m.matrix)
print(m.__repr__)
