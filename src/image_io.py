import numpy as np
import PIL
from PIL import Image
import os
import glob
from typing import Union, Tuple, Iterator, Optional
import logging

logger = logging.getLogger("kamoku-classifier")


def read_image(
    path: str, resize_ratio: Optional[float] = None
) -> Union[Tuple[None, None], Tuple[np.ndarray, Tuple[int, int]]]:
    """
    Read image in grayscale.

    Parameters
    ----------
    path : str
        File path.
    resize_ratio : float or None
        Resize ratio. 0 < resize_ratio <= 1.

    Returns
    -------
    (None, None) or (img, dpi) : None or (np.ndarray, (int, int))
    """
    try:
        pilimg = Image.open(path).convert("L")  # read as gray scale
    except PIL.UnidentifiedImageError:
        return None, None
    dpi = pilimg.info["dpi"]
    if resize_ratio is not None:
        pilimg = pilimg.resize(
            (int(pilimg.width * resize_ratio), int(pilimg.height * resize_ratio))
        )
        dpi = (int(dpi[0] * resize_ratio), int(dpi[1] * resize_ratio))
    return np.array(pilimg), dpi


def read_images(
    dirname: str, ext: Optional[str] = None, resize_ratio: Optional[float] = None
) -> Iterator[Tuple[str, np.ndarray, Tuple[int, int]]]:
    """
    Read images and return iterator.

    Parameters
    ----------
    dirname: str
        Name of the directory.
    ext: str or None
        File's extension such as ".png", ".jpg",...

    Returns
    ----------
    Iterator of (path, image, dpi).
    """
    if ext:
        pathr = os.path.join(dirname, "**", "*" + ext)
    else:
        pathr = os.path.join(dirname, "**")
    # search
    paths = sorted(
        glob.glob(pathr, recursive=True), key=lambda x: os.path.splitext(x)[0]
    )
    # exclude directory name
    paths = tuple(filter(lambda x: os.path.isfile(x), paths))
    filenum = len(paths)
    logger.debug(f"We detected {filenum} files in {dirname}.")

    for i, p in enumerate(paths, start=1):
        logger.info(f"{i}/{filenum};;; Begin processing for {p} {'-'*100}")
        img, dpi = read_image(p, resize_ratio)
        if img is None:
            logger.debug(f"{p} is not an image (skipped).")
            continue
        yield p, img, dpi
