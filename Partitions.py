class Partitions:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self._generate_partitions(self.n)

    def _generate_partitions(self, n, max_val=None):
        if max_val is None:
            max_val = n
        if n == 0:
            yield []
        else:
            for i in range(min(n, max_val), 0, -1):
                for tail in self._generate_partitions(n - i, i):
                    yield [i] + tail


# Example usage
if __name__ == "__main__":
    for partition in Partitions(5):
        print(partition)