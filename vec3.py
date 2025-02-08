class vec3:
    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self.e = [a, b, c]        

    def __str__(self):
        return f"\{self.e[0]} {self.e[1]} {self.e[2]})"
        
    def __add__(self, other):
        return vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __sub__(self, other):
        return vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def __mul__(self, k : float): #scalar multiplication
        return vec3(self.e[0] * k, self.e[1] * k, self.e[2] * k)

    def __truediv__(self, k : float):
        return vec3(self.e[0] / k, self.e[1] / k , self.e[2] / k)

    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def length(self):
        return (self.length_squared())**(1/2)

    def unit(self):
        return (self / self.length())


    
def dot(v, u): # dot product
    return (v.e[0] * u.e[0] + v.e[1] * u.e[1] + v.e[2] * u.e[2])

def cross(v, u): #cross product
    return vec3(v.e[1] * u.e[2] - v.e[2] * u.e[1], self.e[2] * other.e[0] - self.e[0] * other.e[2], self.e[0] * other.e[1] - self.e[1] * other.e[0])



