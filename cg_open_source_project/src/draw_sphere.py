import math
import cairo


def draw_sphere(context, center_x, center_y, radius):
    """Draws a 3D-like sphere with radial gradient shading to create depth."""
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)

    # Radial gradient for the shading effect
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)

    gradient.add_color_stop_rgb(0, 1.0, 0.55, 0.0)  # Bright orange at the center
    gradient.add_color_stop_rgb(0.5, 0.9, 0.4, 0.1)  # Slightly darker orange
    gradient.add_color_stop_rgb(1, 0.6, 0.3, 0.05)    # Darkest brown-orange at the edges

    # Set gradient
    context.set_source(gradient)
    context.fill()

def draw_texture_lines(context, center_x, center_y, radius):
    """ Draws four simple, curved lines on the basketball """
    context.set_source_rgb(0, 0, 0)  # Black lines
    context.set_line_width(8)

    # Diagonal curve: Top-left to bottom-right across the center
    context.move_to(center_x - radius * 0.7, center_y - radius * 0.72)  # Start -> Top-left edge
    context.curve_to(
        center_x - radius * 0.25, center_y + radius * 0.25,  # Control point -> near the top-left side
        center_x + radius * 0.65, center_y + radius * 0.65,  # Control point -> near the bottom-right side
        center_x + radius * 0.7, center_y + radius * 0.72  # End -> near bottom-right edge
    )
    context.stroke()

    # Diagonal curve: Top-right to bottom-left across the center
    context.move_to(center_x + radius * 0.7, center_y - radius * 0.72)
    context.curve_to(
        center_x + radius * 0.4, center_y - radius * 0.5,  # Control point -> near the top-right side
        center_x - radius * 0.6, center_y + radius * 0.5,  # Control point -> near the bottom-left side
        center_x - radius * 0.7, center_y + radius * 0.72
    )
    context.stroke()

    # From the South Pole to East Pole
    south_pole_x = center_x
    south_pole_y = center_y + radius  # South pole coordinates
    east_pole_x = center_x + radius
    east_pole_y = center_y  # East pole coordinates

    # Curve from the South Pole to the East Pole
    context.move_to(south_pole_x, south_pole_y)  # Start -> the South Pole
    context.curve_to(
        center_x + radius * 0.002, center_y + radius * 0.3,  # Control point -> above the South Pole
        center_x + radius * 0.03, center_y - radius * 0.005,  # Control point -> left of the East Pole
        east_pole_x, east_pole_y  # End -> East Pole
    )
    context.stroke()

    # From the North Pole to West Pole
    north_pole_x = center_x
    north_pole_y = center_y - radius
    west_pole_x = center_x - radius
    west_pole_y = center_y

    # Curve from the North Pole to the West Pole
    context.move_to(north_pole_x , north_pole_y)  # Start -> the North Pole
    context.curve_to(
        center_x - radius * 0.002, center_y - radius * 0.5,  # Control point -> below the North Pole
        center_x - radius * 0.03, center_y + radius * 0.005,  # Control point -> to the right of the West Pole
        west_pole_x, west_pole_y  # End -> the West Pole
    )
    context.stroke()



