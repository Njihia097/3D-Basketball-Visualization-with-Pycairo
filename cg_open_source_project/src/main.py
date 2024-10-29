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