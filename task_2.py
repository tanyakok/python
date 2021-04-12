class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        return self._length * self._width * 25 * 0.005


r = Road(20, 5000)
print(f'Масса асфальта {r._length}x{r._width} см равняется {r.weight():.0f} т')
r = Road(40, 8000)
print(f'Масса асфальта {r._length}x{r._width} см равняется {r.weight():.0f} т')
