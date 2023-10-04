from math import sqrt, inf, hypot
from ray import Ray
import numpy as np

class Object:
    def __init__(self, _objects) -> None:
        self.objects = _objects
    def intersect(self):
        '''This function will be recreated for other class'''
        pass
    def normal(self):
        pass

class Sphere(Object):
    
    def __init__(self, objects, center, radius, color, ka, kd, ks, exp, 
                 kr, kt, index_of_refraction, tl = 0, tr = 0) -> None:
        super().__init__(objects)
        self.center = np.array(center)
        self.radius = radius
        self.color = color
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.exp =  exp
        self.kr = kr
        self.kt = kt
        self.index_of_refraction = index_of_refraction
        self.tl = tl # first parameter
        self.tr = tr # second parameter

    def intersect(self, ray: Ray):
 
        ray_to_sphere = self.center - ray.origin # ray origin to sphere origin
        t_min = np.dot(ray_to_sphere, ray.direction) # parameter
        distance = sqrt(np.dot(ray_to_sphere, ray_to_sphere) -  t_min ** 2)

        if distance ** 2 <= self.radius ** 2: # d**2 <= radius**2?
            h = sqrt(self.radius ** 2 - distance ** 2) # pitagoras
            tl, tr = t_min - h, t_min + h
            if tl < 0:
                return inf if tr < 0 else tr
            else:
                return tl
        else: # not intersection
            return inf

    def normal(self, P):
        norm = lambda x, y, z : hypot(x,y,z)
        normalize = lambda a, b: a / b
        normal = P - self.center

        return normalize(normal, norm(*normal))

class Plane(Object):

    def __init__(self, objects: Object, point: list, v_normal: list, color, ka, kd, ks, exp,
                 kr, kt, index_of_refraction) -> None:
        super().__init__(objects)
        self.point = np.array(point)
        self.v_normal = np.array(v_normal)
        self.color = color
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.exp =  exp
        self.kr = kr
        self.kt = kt
        self.index_of_refraction = index_of_refraction


    def intersect(self, ray: Ray):
        
        v = np.dot(ray.direction, self.v_normal) 
        EPSLON = 0.0000001

        if abs(v) < EPSLON:
            return inf
        else:
            h = np.dot(self.point - ray.origin, self.v_normal)
            t_parameter = h / v
            return inf if t_parameter < EPSLON else t_parameter
    
    def normal(self, _):
        norm = lambda x, y, z : hypot(x,y,z)
        normalize = lambda a, b: a / b

        return normalize(self.v_normal, norm(*self.v_normal))




