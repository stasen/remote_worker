from mss import mss, tools
from os.path import join, dirname, realpath
from subprocess import Popen, PIPE
from time import sleep
import argparse
from ocr_coordinates import *

here = dirname(realpath(__file__))
mini_path = join(here, 'MiniMouseMacro.exe')


def _iterate_steps(steps, wait):
    for name in steps:
        args = [
            mini_path,
            '/e',
            '/m',
            join(here, 'recordings', name)
        ]
        with Popen(args, shell=False, stderr=PIPE, stdout=PIPE) as eog:
            sleep(wait)


def go_to_main_gui():
    steps = [
        'button_v.mmmacro',
        'button.mmmacro',
        'left.mmmacro'
    ]
    _iterate_steps(steps, 0)


def press_yellow_button():
    steps = [
        'yellow_button.mmmacro'
    ]
    _iterate_steps(steps, 0)


def _get_screenshort(monitor):
    output_png = join(here, 'screenshorts', 'screenshort.png')
    with mss() as sct:
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=output_png)


def get_rf_image():
    monitor = {"top": RF_TOP, "left": RF_LEFT, "width": RF_WIDTH, "height": RF_HEIGHT}
    _get_screenshort(monitor)


def get_on_off_button_image():
    monitor = {"top": ON_OFF_TOP, "left": ON_OFF_LEFT, "width": ON_OFF_WIDTH, "height": ON_OFF_HEIGHT}
    _get_screenshort(monitor)


def rf_minus():
    steps = ['rf_minus.mmmacro']
    _iterate_steps(steps, 0)


def rf_plus():
    steps = ['rf_plus.mmmacro']
    _iterate_steps(steps, 0)


def press_on_off_button():
    steps = ['on_off_button.mmmacro']
    _iterate_steps(steps, 0)


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--command", required=True, help="command to run")
args = vars(ap.parse_args())

eval(args['command'])()
