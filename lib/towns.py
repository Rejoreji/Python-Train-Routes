__author__ = 'Che'

class Town:
    visited = False

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        try:
            return self.name == other.name
        except:
            return False

if __name__ == "__main__":
    a1, a2, a3 = Town('foo'), Town('foo'), Town('bar')
    d = {a1: 'foo'}
    print d[a1]
