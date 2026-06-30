import heapq

from matrix import Matrix
from vector import Vector

import numpy as np

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

c = Vector([1, 1])
scale_matrix = Matrix([[2, 0], [0, 3]])

print(f"angle between a and b = {a.angle_between(b)}")
print(f"c = {c}, scaled vector c = {scale_matrix @ c}")

# random word vectors - dimension 50
words = np.random.randn(5, 50)
print(words)

word_vectors = []

for word in words:
    word_vectors.append(Vector(word))

similarities_keys = []
similarities = {}

similarities_keys.sort(reverse=True)

for i in range(len(word_vectors)):
    for j in range(len(word_vectors)):
        if i == j:
            continue

        cosim = word_vectors[i].cosine_similarity(word_vectors[j])

        if cosim not in similarities:
            similarities[cosim] = []
            similarities_keys.append(cosim)

        similarities[cosim].append((word_vectors[i], word_vectors[j]))

print("FIRST:")
print(similarities[similarities_keys[0]])
print("SECOND:")
print(similarities[similarities_keys[1]])

mat_rank = np.matrix([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]])
rank = np.linalg.matrix_rank(mat_rank)

print(rank)

a1 = Vector([1, 1, 1])
b1 = Vector([1, 2, 3])

print(b1.project(a1))