from vec3 import vec3 as color
from hittable import *

def write_color(pixel_color: color):
    rgb = pixel_color * 255.999 
    r, g, b = int(rgb.e[0]), int(rgb.e[1]), int(rgb.e[2])
    print(r, ' ', g, ' ', b, '\n')
    

def ray_color(ray, world: hittable):
    rec = hit_record(vec3(0,0,0), vec3(0,0,0), 0)
    if any([x.hit(ray, 0, float('inf'), rec) for x in world]):
        return (rec.normal + color(1,1,1)) * 0.5

    unit_d = ray.direction.unit()
    a = (unit_d.e[1] + 1.0) * 0.5
    return color(1,1,1)*(1.0 - a) + color(0.5, 0.7, 1.0)*a
