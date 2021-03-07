from random_polys_util import *

def cairo_poly(pts, clr):
    ctx.set_source_rgba(*ints2floats(clr))
    ctx.move_to(*pts[-1])
    for pt in pts:
        ctx.line_to(*pt)
    ctx.close_path()
    ctx.fill()

def cairo_main():
    # Setup Cairo
    import cairo
    global ctx
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    # fill background white
    cairo_poly(((0,0),(WIDTH,0),(WIDTH,HEIGHT),(0,HEIGHT)),(255,255,255,255))
    draw_all(cairo_poly)
    surface.write_to_png('cairo_example.png')

def main():
    cairo_main()

if __name__ == "__main__":
    main()
