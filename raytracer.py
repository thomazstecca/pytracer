import logging

from vec3 import * 
from color import *

class ray:
    def __init__(self, origin: vec3 = 0, direction: vec3 = 0):
        self.origin = origin
        self.direction = direction

    def at(t):
        return (origin + (direction * t))

def ray_color(ray):
    unit_direction = ray.direction.unit()
    a = (unit_direction.e[1] + 1 ) * 0.5
    return color(1, 1, 1)*(1 - a) + color(0.5, 0.7, 1.0)*a

def make_image():

    #Logging
    #logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")
    
    #Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    
    image_height = int(image_width / aspect_ratio)
    image_height = 1 if image_height < 1 else image_height

    #Camera
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (float(image_width)/image_height)
    camera_center = vec3(0,0,0)

    viewport_u = vec3(viewport_width, 0, 0)
    viewport_v = vec3(0, -viewport_height, 0)

    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    viewport_upper_left = camera_center - vec3(0,0,focal_length) - viewport_u/2 - viewport_v/2
    pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5

    
    
    
    #render
    print("P3\n", image_width, ' ', image_height, "\n255\n")
    for j in range(image_height):
        #logging.info("\rScanlines remaining: " + str(height - j))
        for i in range(image_width):
            pixel_center = pixel00_loc + (pixel_delta_u * i) + (pixel_delta_v * j)
            ray_direction = pixel_center - camera_center
            r = ray(camera_center, ray_direction)

            pixel_color = ray_color(r)
            write_color(pixel_color)
    #logging.info("\rDone.                 ")


    
    
if __name__ == "__main__":
    make_image()
    


