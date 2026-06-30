import math

class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])
    
    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        return Vector([x / mag for x in self.components])
    
    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())
    
    def angle_between(self, other):
        cosine = self.cosine_similarity(other)
        theta = math.acos(cosine)
        return math.degrees(theta)

    
    def __repr__(self):
        return f"Vector({self.components})"
    
    def project(self, other):
        scalar = self.dot(other) / other.dot(other)
        return Vector([scalar * x for x in other.components])