from solid2 import *

set_global_fn(100)

CYLINDER_WIDTH = 11
CYLINDER_HEIGHT = 20.5
CYLINDER_DEPTH = 20
CYLINDER_SCALE_Y_RATIO = CYLINDER_HEIGHT / CYLINDER_WIDTH


def make_cylinder():

    r = CYLINDER_WIDTH / 2
    h = CYLINDER_DEPTH
    scale = [1, CYLINDER_SCALE_Y_RATIO, 1]
    return cylinder(r=r, h=h).scale(*scale)


def make_cylinder_array():
    x_offset = (13 + 2.5) + CYLINDER_WIDTH
    cylinders_x = [
        (x_offset * -1),
        (x_offset * 1),
    ]

    _model = make_cylinder()
    for x in cylinders_x:
        _c = make_cylinder().translateX(x)
        _model += _c

    return _model


def make_dispenser_bottom():
    BOTTOM_WIDTH = 85
    BOTTOM_HEIGHT = BOTTOM_WIDTH / 2

    r = BOTTOM_HEIGHT
    scale = [1.5, 0.6, 1]
    return cylinder(r=r, h=2).scale(*scale).translateZ(20)


def make_dispenser_guard():
    BOTTOM_WIDTH = 85
    BOTTOM_HEIGHT = BOTTOM_WIDTH / 2

    r = BOTTOM_HEIGHT
    h = 50
    scale = [1.5, 0.6, 1]
    guard = cylinder(r=r, h=h).scale(*scale)

    # cutout
    r1 = r - 2
    h1 = h + 10
    guard_inner = cylinder(r=r1, h=h1).scale(*scale).translateZ(-1)

    _model = (guard - guard_inner).translateZ(22)

    return _model


cylinder_array = make_cylinder_array()
dispenser_bottom = make_dispenser_bottom()
dispenser_guard = make_dispenser_guard()

dispenser_body = (dispenser_bottom + dispenser_guard).translateY(8)

model = cylinder_array + dispenser_body

model.save_as_scad()
