import cairo

from court import draw_court_boundaries, draw_half_court_line

WIDTH, HEIGHT = 1000, 700

def draw_basketball_court_with_ball():
    with cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT) as surface:
        context = cairo.Context(surface)

        # Background color (main canvas)
        context.set_source_rgb(0, 0.72, 0.53)
        context.rectangle(0, 0, WIDTH, HEIGHT)
        context.fill()

        # Court boundaries
        court_width, court_height = WIDTH - 150, HEIGHT - 100
        draw_court_boundaries(context, court_width, court_height)

        # Vertical half-court line
        center_x = court_width / 2 + 50
        draw_half_court_line(context, center_x, 100, court_height)

        surface.write_to_png("basketball_court_with_ball.png")
 #Adding Key Areas and Three-Point Arcs
 # Draw key areas
center_y = court_height / 2 + 50
draw_key_area(context, 100, center_y - 60, 100, 120)
draw_key_area(context, court_width - 100 , center_y - 60, 100, 120)

# Draw three-point arcs
draw_three_point_arc(context, 100, center_y, 160, left=True)
draw_three_point_arc(context, court_width, center_y, 160, left=False)

from court import draw_center_circle, draw_dashed_free_throw_circle

# Center circle
draw_center_circle(context, center_x, center_y, 50)

# Dashed free-throw circles
free_throw_radius = 60
draw_dashed_free_throw_circle(context, 200, center_y, free_throw_radius)
draw_dashed_free_throw_circle(context, court_width - 100, center_y, free_throw_radius)