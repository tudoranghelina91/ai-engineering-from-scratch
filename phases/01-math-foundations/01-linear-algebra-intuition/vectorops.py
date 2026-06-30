from vector import Vector

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a.dot(b)}")
print(f"|a| = {a.magnitude():.4f}")
print(f"cosine similarity = {a.cosine_similarity(b):.4f}")