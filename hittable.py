from vec3 import *
from ray import *


class hit_record:
    def __init__(self, p: vec3, normal: vec3, t: float = 0, front = False):
        self.p = p
        self.normal = normal
        self.t = t
        self.front = front

    def set_face_normal(self, ray, outward_normal):
        self.front = (dot(ray.direction, outward_normal) < 0)
        self.normal =  outward_normal if self.front else -outward_normal
    

class hittable:
    def __init__():
        pass

    def hit(ray, tmin, tmax, rec: hit_record):
        return False

class sphere(hittable):
    def __init__(self, center: vec3, radius: float):
        self.center = center
        self.radius = max(0, radius)

    def hit(self, ray, tmin, tmax, rec: hit_record):
        oc = self.center - ray.origin
        a = ray.direction.length_squared()
        h = dot(ray.direction, oc)
        c = oc.length_squared() - self.radius * self.radius
        discriminant = h*h - a*c

        if (discriminant < 0):
            return False

        sqrtd = discriminant**(1/2)
        root = (h - sqrtd) / a
        if (root <= tmin or root >= tmax):
            root = (h + sqrtd) / a
            if (root <= tmin or root >= tmax):
                return False

        rec.t = root
        rec.p = ray.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(ray, outward_normal)
        
        return True
