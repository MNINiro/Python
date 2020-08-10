MIN_ALPHA = 50
MAX_ALPHA = 100

WIDTH = 500
HEIGHT = 250

    #
    #   Utilities
    #
def hex2tuple(hex_color):
        return tuple([int(hex_color[i:i+2], 16) for i in range(1,9,2)])

def tuple2hex(tuple_color):
        return "#%0.2X%0.2X%0.2X%0.2X" % tuple_color

def ints2floats(tuple_color):
        return tuple([c / 255.0 for c in tuple_color])

def inc_point(p, dp):
        return (p[0] + dp[0]) % WIDTH, (p[1] + dp[1]) % HEIGHT

def inc_triangle(t, dt):
        return tuple([inc_point(t[i], dt[i]) for i in range(3)])

def inc_color(c, dc):
        new_c = [(c[i] + dc[i]) % 256 for i in range(3)]
        new_a = (c[3] + dc[3]) % MAX_ALPHA
        if new_a < MIN_ALPHA: new_a += MIN_ALPHA
        new_c.append(new_a)
        return tuple(new_c)

def draw_all(draw_fn):
        triangle = start_t
        color = start_c
        for i in range(50):
            triangle = inc_triangle(triangle, dt)
            color = inc_color(color, dc)
            draw_fn(triangle, color)

#
#   Starting and incrementing values
#
start_c = hex2tuple('E6A20644')
start_t = (127, 132), (341, 171), (434, 125)
dt = (107, 23), (47, 73), (13, 97)
dc = 61, 113, 109, 41

print(start_c)
print(start_t)
print(dt)
print(dc)
