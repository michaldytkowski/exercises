class Matrix:
    def __init__(self, macierz):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in macierz.splitlines()
        ]

m = Matrix('3 4\n5 6\n7 8')
print(m.matrix)
