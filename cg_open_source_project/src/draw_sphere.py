import math
import cairo
def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1.0, 0.55, 0.0) 
    gradient.add_color_stop_rgb(0.5, 0.9, 0.4, 0.1) 
    gradient.add_color_stop_rgb(1, 0.6, 0.3, 0.05)   

    context.set_source(gradient)
    context.fill()
