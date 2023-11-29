import os
import shutil
import logging
from typing import Optional, List, Tuple

from .setting_io import SETTING_KEYS, MARK_COORDS
from .image_io import read_images
from .read_marksheet import MarkReader



def main():
    metadata = SETTING_KEYS
    metadata["sheet"] = MARK_COORDS
    mark_reader = MarkReader(metadata)

    img_dir = "./data"
    save_dir = "./secret"
    img_iter = read_images(img_dir)
    for p, img, dpi in img_iter:
        choice = mark_reader.read(img)["choice"]
        save_dir_choice = os.path.join(save_dir, choice)
        filename = os.path.basename(p)
        os.makedirs(save_dir_choice, exist_ok=True)
        shutil.copyfile(p, os.path.join(save_dir_choice, filename))
