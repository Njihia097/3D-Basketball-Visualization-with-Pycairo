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
