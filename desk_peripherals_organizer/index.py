from solid2 import *
import math

set_global_fn(100)

# region: BASE
BASE_SIZE_X = 150
BASE_SIZE_Y = 100
BASE_SIZE_Z = 3
# endregion

# region: KEYBOARD SLOT BACK
# "ksb" = "keyboard slot back"
KSB_SIZE_X = BASE_SIZE_X
KSB_SIZE_Y = 15
KSB_SIZE_Z = 50
KSB_OFFSET_Y = (BASE_SIZE_Y / 2) - (KSB_SIZE_Y / 2)
KSB_OFFSET_Z = (KSB_SIZE_Z / 2) + 1.5

KSB_DIAGONAL_SIZE = math.sqrt((KSB_SIZE_Y**2) + (KSB_SIZE_Z**2))
_KSB_DIAGONAL_ANGLE = math.atan2(KSB_SIZE_Z, KSB_SIZE_Y) / math.pi * 180
KSB_DIAGONAL_ANGLE = (
    _KSB_DIAGONAL_ANGLE + 2
)  # we don't want the angle to be quite corner to corner

a = 1.192  # eyeball value
KSB_CUTOUT_SIZE_Z = KSB_SIZE_Z + 10
KSB_CUTOUT1_OFFSET_Y = KSB_OFFSET_Y - (KSB_SIZE_Y / 2) - a
KSB_CUTOUT2_OFFSET_Y_FROM_C1 = 17.38
KSB_CUTOUTS_GAP = BASE_SIZE_Z
# endregion

# region: TRACKPAD
# "tp" = "trackpad"
TP_OFFSET_Y_FROM_KSB = 8
# endregion

# region: MOUSE HOLDER
# "mh" = "mouse_holder"
MH_SIZE_X = 35.52
MH_SIZE_Y = 40
MH_SIZE_Z = 50
MH_OFFSET_Y = (((BASE_SIZE_Y / 2) - (KSB_SIZE_Y / 2)) * -1) + 2.5 - 8
# endregion


def make_base():
    _model = cylinder(r=BASE_SIZE_X / 2, h=BASE_SIZE_Z, center=True)

    # make it a half cylinder
    _c1 = cube(BASE_SIZE_X, center=True)
    _c1 = _c1.translateY((BASE_SIZE_X / 2) + 12.5)
    _model = _model - _c1
    _model = _model.translateY(BASE_SIZE_X / 4)

    return _model


def make_keyboard_slot_back():
    # make cube
    _model = cube(KSB_SIZE_X, KSB_SIZE_Y, KSB_SIZE_Z, center=True)
    _model = _model.translate(0, KSB_OFFSET_Y, KSB_OFFSET_Z)

    # then make angled cutouts from cube
    # "c" = "cutout"
    _c1 = cube(KSB_SIZE_X, KSB_SIZE_Y, KSB_CUTOUT_SIZE_Z, center=True)
    _c1 = _c1.rotateX(KSB_DIAGONAL_ANGLE - 90)
    _c1 = _c1.translate(0, KSB_CUTOUT1_OFFSET_Y, KSB_OFFSET_Z)

    # second cutout is a copy of the first, but moved backward
    _c2 = _c1.translateY(KSB_CUTOUT2_OFFSET_Y_FROM_C1)

    # transform the back cutout into 3 pieces, with a space in between each
    # this will generate back supports
    _c2 = _c1.translateY(KSB_CUTOUT2_OFFSET_Y_FROM_C1)
    _c2 = _c2.scaleX(1 / 3)
    _c3 = _c2.translateX((KSB_SIZE_X / 3) + KSB_CUTOUTS_GAP)
    _c4 = _c2.translateX((KSB_SIZE_X / -3) - KSB_CUTOUTS_GAP)

    # scale c1 on the x axis to get a clean cut
    _c1 = _c1.scaleX(1.1)

    return _model - _c1 - _c2 - _c3 - _c4


def make_trackpad_slot_back():
    # trackpad back is the same as the keyboard slot back
    _model = make_keyboard_slot_back()

    # adjust position
    _model = _model.translateY((KSB_SIZE_Y * -1) - TP_OFFSET_Y_FROM_KSB)

    # adjust size on the x-axis (using the golden ratio)
    _model = _model.scaleX(1 / 1.618)  # 93
    return _model


def make_mouse_holder():
    # a little lazy with the math here
    # mostly just eyeballing things

    _model = cube(MH_SIZE_X, MH_SIZE_Y, MH_SIZE_Z, center=True)
    _model = _model.translateY(MH_OFFSET_Y + 35)
    _model = _model.translateZ((MH_SIZE_Z / 2) - 1.5)

    # cutouts
    c_x_axis = _model
    c_x_axis = c_x_axis.scaleZ(2)
    c_x_axis = c_x_axis.rotateX(KSB_DIAGONAL_ANGLE - 90)
    c_x_axis = c_x_axis.scaleX(1.1)
    c_x_axis = c_x_axis.translateY(-13)
    c_x_axis = c_x_axis.translateZ(8)

    c_y_axis = cube(MH_SIZE_X - 20, MH_SIZE_Y, MH_SIZE_Z, center=True)
    c_y_axis = c_y_axis.translateY(MH_OFFSET_Y + 35)
    c_y_axis = c_y_axis.translateZ((MH_SIZE_Z / 2) - 1.5)
    c_y_axis = c_y_axis.scaleY(2)
    c_y_axis = c_y_axis.scaleZ(2)

    return _model - c_x_axis - c_y_axis


model = (
    ~make_base()
    + ~make_keyboard_slot_back()
    + ~make_trackpad_slot_back()
    + ~make_mouse_holder()
)

model.save_as_scad()
