from vec3 import vec3 as color


def write_color(pixel_color: color):
    rgb = pixel_color * 255.999 
    r, g, b = int(rgb.e[0]), int(rgb.e[1]), int(rgb.e[2])
    print(r, ' ', g, ' ', b, '\n')
    
