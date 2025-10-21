class FibSequence:
    def __init__(self, num: int):
        self._num = num

    def __iter__(self):
        return FibIterator(self._num)


class FibIterator:
    def __init__(self, num: int):
        self._num = num
        self._i = 0
        self._j = 1

    def __next__(self):
        if self._num <= 0:
            raise StopIteration

        # _i と _j を使って次に返すフィボナッチ数の値を変数valに格納する
        val = self._i + self._j

        # _i, _j, _numを更新する
        self._i = self._j
        self._j = val
        self._num -= 1

        return self._i


if __name__ == "__main__":
    for v in FibSequence(10):
        print(v)
