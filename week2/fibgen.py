class FibGenerator:
    def __init__(self, num: int):
        self._num = num

    def __iter__(self):
        i = 0
        j = 1

        for _ in range(self._num):
            yield j
            prev_i = i
            i = j
            j += prev_i


if __name__ == "__main__":
    for v in FibGenerator(10):
        print(v)
