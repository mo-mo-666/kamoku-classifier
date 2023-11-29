import os
import shutil
import logging
from typing import Optional, List, Tuple

from .read_args import read_args
from .setting_io import SETTING_KEYS, MARK_COORDS, MARK_COORDS2
from .image_io import read_images
from .read_marksheet import MarkReader


def pipeline():
    args, mode, img_dir, save_dir = read_args()
    metadata = SETTING_KEYS
    if mode == 1:
        metadata["sheet"] = MARK_COORDS
    elif mode == 2:
        metadata["sheet"] = MARK_COORDS2

    mark_reader = MarkReader(metadata)

    img_iter = read_images(img_dir)
    for p, img, dpi in img_iter:
        choice = mark_reader.read(img)["choice"]
        save_dir_choice = os.path.join(save_dir, choice)
        filename = os.path.basename(p)
        os.makedirs(save_dir_choice, exist_ok=True)
        shutil.copyfile(p, os.path.join(save_dir_choice, filename))
