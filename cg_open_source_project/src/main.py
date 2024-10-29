import cairo
from court import (
    draw_court_boundaries, draw_center_circle, draw_three_point_arc,
    draw_key_area, draw_dashed_free_throw_circle, draw_half_court_line
)
from draw_sphere import draw_sphere, draw_texture_lines

WIDTH, HEIGHT = 1000, 700

def draw_basketball_court_with_ball():
    with cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT) as surface:
        context = cairo.Context(surface)

        # Background color (main canvas)
        context.set_source_rgb(0, 0.72, 0.53)
        context.rectangle(0, 0, WIDTH, HEIGHT)
        context.fill()

        # Background color (wooden floor look)
        context.set_source_rgb(0.91, 0.72, 0.53)
        context.rectangle(50, 50, WIDTH - 150 , HEIGHT - 100)
        context.fill()

        # Court boundaries (adjusted to keep court centered within new canvas size)
        court_width, court_height = WIDTH - 150, HEIGHT - 100
        draw_court_boundaries(context, court_width, court_height)

        # Center circle
        center_x, center_y = court_width / 2 + 50, court_height / 2 + 50
        draw_center_circle(context, center_x, center_y, 50)

        # Vertical half-court line
        draw_half_court_line(context, center_x, 100, court_height)

        # Three-point arcs
        draw_three_point_arc(context, 100, center_y, 160, left=True)
        draw_three_point_arc(context, court_width , center_y, 160, left=False)

        # Key areas
        draw_key_area(context, 100, center_y - 60, 100, 120)
        draw_key_area(context, court_width - 100 , center_y - 60, 100, 120)

        # Dashed free-throw circles
        free_throw_radius = 60
        draw_dashed_free_throw_circle(context, 200, center_y, free_throw_radius)
        draw_dashed_free_throw_circle(context, court_width - 100 , center_y, free_throw_radius)

        # Position for the basketball at the bottom right, slightly off the court
        ball_x = WIDTH - 135
        ball_y = HEIGHT - 130
        ball_radius = 125

        # Draw the basketball
        draw_sphere(context, ball_x, ball_y, ball_radius)

        draw_texture_lines(context, ball_x, ball_y, ball_radius)

        # Save to file
        surface.write_to_png("basketball_court_with_ball.png")
        print("Basketball court with 3D basketball created!")

        if _name_ == "_main_":
            draw_basketball_court_with_ball()
