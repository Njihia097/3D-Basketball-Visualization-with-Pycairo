import math

import cairo

def draw_court_boundaries(context, width, height):
    context.set_source_rgb(1, 1, 1)  # White color for lines
    context.set_line_width(5)
    context.rectangle(100, 100, width - 100, height - 100)  # Outer court boundary
    context.stroke()

def draw_half_court_line(context, x, y_start, y_end):
    context.set_line_width(5)
    context.move_to(x, y_start)
    context.line_to(x, y_end)
    context.stroke()

def draw_center_circle(context, center_x, center_y, radius):
    context.set_line_width(5)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.stroke()

def draw_three_point_arc(context, center_x, center_y, radius, left=True):
    context.set_line_width(5)
    if left:
        # Three-point-arc at left side of the court
        start_angle = 3 * math.pi / 2
        end_angle = math.pi / 2
    else:
        # Three-point-arc at right side of the court
        start_angle = math.pi / 2
        end_angle = -math.pi / 2

    context.arc(center_x, center_y, radius, start_angle, end_angle)
    context.stroke()


def draw_key_area(context, x, y, diameter, height):
    context.set_line_width(5)
    context.rectangle(x, y, diameter, height)
    context.stroke()

def draw_dashed_free_throw_circle(context, center_x, center_y, radius):
    context.set_line_width(5)
    context.set_dash([10, 5])  # Dash pattern: 10 on, 5 off
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)  # Dashed circle
    context.stroke()
    context.set_dash([])  # Reset dash pattern