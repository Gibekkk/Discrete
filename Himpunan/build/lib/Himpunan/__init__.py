class Himpunan:

    def __init__(self, *elemen):
        self.elemen = list(set(elemen))  # Hindarin elemen duplikat

    def __len__(self):
        return len(self.elemen)

    def __contains__(self, item):
        return item in self.elemen

    def __eq__(self, other):
        return sorted(self.elemen) == sorted(other.elemen)

    def __le__(self, other):
        return all(item in other.elemen for item in self.elemen)

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return other <= self

    def __floordiv__(self, other):
        return set(self.elemen) == set(other.elemen)
    
    def Komplemen(self, semesta):
        return semesta - self
    
    def komplement(self, semesta):
        self.Komplemen(semesta)

    def __add__(self, other):
        if isinstance(other, Himpunan):
            return Himpunan(*(self.elemen + other.elemen))
        else:
            return Himpunan(*(self.elemen + [other]))

    def __sub__(self, other):
        return Himpunan(*(item for item in self.elemen if item not in other.elemen))

    def __truediv__(self, other):  # Intersect
        return Himpunan(*(item for item in self.elemen if item in other.elemen))

    def __mul__(self, other):  # Symmetric Difference
        return Himpunan(*((set(self.elemen) ^ set(other.elemen))))

    def __pow__(self, other):  # Cartesian Product
        return Himpunan(*[(x, y) for x in self.elemen for y in other.elemen])
    
    def ListKuasa(self):
        from itertools import chain, combinations
        power_set = list(chain.from_iterable(combinations(self.elemen, r) for r in range(len(self.elemen) + 1)))
        return [Himpunan(*subset) for subset in power_set]

    def __abs__(self):  # Power Set
        return len(self.ListKuasa())

    def __repr__(self):
        return f"{"{"}{', '.join(map(str, sorted(self.elemen)))}{"}"}"