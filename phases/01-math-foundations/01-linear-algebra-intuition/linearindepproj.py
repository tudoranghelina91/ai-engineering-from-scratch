from vector import Vector
from matrix import Matrix

def is_linearly_independent(vectors):
    n = len(vectors)
    dim = len(vectors[0].components)
    mat = Matrix([v.components[:] for v in vectors])
    rows = [row[:] for row in mat.rows]
    rank = 0

    for col in range(dim):
        pivot = None
        for row in range(rank, len(rows)):
            if abs(rows[row][col] > 1e-10):
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col] > 1e-10):
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank += 1
    return rank == n

def gram_schmidt(vectors):
    orthonormal = []
    for v in vectors:
        w = v
        for u in orthonormal:
            proj = w.project(u)
            w = w - proj
        if w.magnitude() < 1e-10:
            continue
        orthonormal.append(w.normalize())
    return orthonormal

v1 = Vector([1, 0, 0])
v2 = Vector([1, 1, 0])
v3 = Vector([1, 1, 1])
basis = gram_schmidt([v1, v2, v3])

for i, u in enumerate(basis):
    print(f"u{i + 1} = {u}")
    print(f"|u{i + 1}| = {u.magnitude():.6f}")

print(f"u1 * u2 = {basis[0].dot(basis[1]):.6f}")
print(f"u1 * u3 = {basis[0].dot(basis[2]):.6f}")
print(f"u2 * u3 = {basis[1].dot(basis[2]):.6f}")

# Gram Schmidt output 2
v4 = Vector([2, 1, 9])
v5 = Vector([-3, 4, 6])
v6 = Vector([5, 3, 4])

basis2 = gram_schmidt([v4, v5, v6])

for i, u in enumerate(basis2):
    print(f"u{i + 1} = {u}")
    print(f"|u{i + 1}| = {u.magnitude():.6f}")

print(f"u1 * u2 = {basis2[0].dot(basis2[1]):.6f}")
print(f"u1 * u3 = {basis2[0].dot(basis2[2]):.6f}")
print(f"u2 * u3 = {basis2[1].dot(basis2[2]):.6f}")