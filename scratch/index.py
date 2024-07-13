from solid2 import *

set_global_fn(72)

BRACKET_SIDE_THICKNESS = 0.5
BRACKET_SIDE_WIDTH = 20
BRACKET_SIDE_HEIGHT = 10
BRACKET_SCREWHOLE_OFFSET = 2


# TODO: move to utils file
def generate_rectangle_screwhole_matrix(s1, s2, o):
    return [[o, o], [o, s2 - o], [s1 - o, s2 - o], [s1 - o, o]]


def make_panel_with_screwholes():

    _m = cube(BRACKET_SIDE_WIDTH, BRACKET_SIDE_HEIGHT, BRACKET_SIDE_THICKNESS)

    screwhole_positions = generate_rectangle_screwhole_matrix(
        BRACKET_SIDE_WIDTH, BRACKET_SIDE_HEIGHT, BRACKET_SCREWHOLE_OFFSET
    )

    for [x, y] in screwhole_positions:
        _m -= cylinder(r=0.25, h=4).translate(x, y, 0)

    return _m


panel_with_screwholes = make_panel_with_screwholes()
model = panel_with_screwholes

model.save_as_scad()
