class DetectSquares:
    def __init__(self):
        self.point_counts = Counter()
        self.x_to_ys = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_counts[(x, y)] += 1
        self.x_to_ys[x].add(y)

    def count(self, point: List[int]) -> int:
        px, py = point
        squares = 0

        for x in self.x_to_ys:  # iterate all x-coords, not just px
            if x == px:
                continue
            side = abs(x - px)  # horizontal distance = side length
            for cy in [py + side, py - side]:  # two possible squares (above/below)
                c1 = self.point_counts[(x, py)]  # shares row with query
                c2 = self.point_counts[(x, cy)]  # diagonal corner
                c3 = self.point_counts[(px, cy)]  # shares column with query
                squares += c1 * c2 * c3

        return squares
