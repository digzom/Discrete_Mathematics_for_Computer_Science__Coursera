from itertools import combinations, permutations

def is_solution(perm):
    pairs = combinations(range(len(perm)), 2)
    return all(abs(i1 - i2) != abs(perm[i1] - perm[i2])
        for i1, i2 in pairs)

solution = next(filter(is_solution, permutations(range(12))))

print(solution)
