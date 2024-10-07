import random


matrix = [
    [0, 4, 5, 3, 8],
    [4, 0, 7, 6, 8],
    [5, 7, 0, 7, 9],
    [3, 6, 7, 0, 9],
    [8, 8, 9, 9, 0],
]

def F(chromosome: "Chromosome") -> int:
    res = 0
    for i in range(chromosome.size):
        city_a = int(chromosome.genes[i])
        city_b = int(chromosome.genes[(i + 1) % chromosome.size])
        res += matrix[city_a][city_b]
    return res

class Gene:

    def __init__(self, char: str):
        assert len(char) == 1
        self.char = char

    def __str__(self) -> str:
        return self.char

    def __int__(self) -> int:
        return int(self.char) - 1

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Gene):
            return False
        return self.char == value.char


def genes_to_str(genes: list[Gene]) -> str:
    return "".join([str(gene) for gene in genes])


class Chromosome:
    genes: list[Gene]
    value: int

    def __init__(self, genes: str | list[Gene]):
        if isinstance(genes, list):
            self.genes = genes
        else:
            self.genes = [Gene(gene) for gene in genes]
        self.value = F(self)

    @staticmethod
    def generate(size: int) -> "Chromosome":
        genes = [Gene(str(i)) for i in range(1, size + 1)]
        random.shuffle(genes)
        return Chromosome(genes)

    @property
    def size(self):
        return len(self.genes)

    def cross(self, other: "Chromosome") -> tuple["Chromosome", "Chromosome"]:
        assert self.size == other.size
        left_slice, right_slice = self._generate_slices()
        part_a, part_b, part_c, stack = self.split(left_slice, right_slice)
        other_part_a, other_part_b, other_part_c, other_stack = other.split(
            left_slice, right_slice
        )


        new_chromosome_a = Chromosome.fill_gaps(
            part_b, len(part_a), len(part_c), other_stack
        )
        new_chromosome_b = Chromosome.fill_gaps(
            other_part_b, len(other_part_a), len(other_part_c), stack
        )
        return new_chromosome_a, new_chromosome_b

    @staticmethod
    def fill_gaps(
        part_b: list[Gene], part_a_len: int, part_c_len: int, stack: list[Gene]
    ) -> "Chromosome":
        result: list[Gene] = []
        stack = [gene for gene in stack if gene not in part_b]
        result = stack[:part_a_len] + part_b + stack[part_a_len:]
        return Chromosome(result)

    def split(
        self, slice_left: int, slice_right: int
    ) -> tuple[list[Gene], list[Gene], list[Gene], list[Gene]]:
        return (
            self.genes[:slice_left],
            self.genes[slice_left:slice_right],
            self.genes[slice_right:],
            self.genes[slice_left + 1 :] + self.genes[: slice_left + 1],
        )

    def _generate_slices(self) -> tuple[int, int]:
        options = []
        for i in range(1, self.size):
            for j in range(i + 1, self.size):
                options.append((i, j))
        return random.choice(options)

    def mutate_in_place(self) -> None:
        a = random.randint(0, self.size - 1)
        b = (a + random.randint(1, self.size - 1)) % self.size
        new_genes = self.genes.copy()
        new_genes[a], new_genes[b] = new_genes[b], new_genes[a]
        self.genes = new_genes
        self.value = F(self)

    def __str__(self):
        return "".join(str(i) for i in self.genes)

    def __repr__(self):
        return str(self)


population_size = 6
mutation_percent = 1
epochs = 100
population: list[Chromosome] = [Chromosome.generate(5) for i in range(population_size)]

for epoch in range(epochs):
    parents = population.copy()
    random.shuffle(parents)
    for [parent_a, parent_b] in zip(
        parents[population_size // 2 :], population[: population_size // 2]
    ):
        population.extend(parent_a.cross(parent_b))
    for chromosome in population:
        if random.random() * 100 <= mutation_percent:
            chromosome.mutate_in_place()

    population.sort(key=lambda ch: ch.value)
    population = population[:population_size]

print(population[0])
print(population[0].value)
