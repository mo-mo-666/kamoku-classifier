import os
import logging
from typing import Optional, List, Tuple

from .setting_io import MarksheetResultWriter, read_marksheet_setting
from .image_io import read_image
from .read_marksheet import MarkReader



metadata= {}
metadata_path = "./settings/setting.xlsx"
metadata["sheet"] = read_marksheet_setting(metadata_path)

mark_reader = MarkReader(metadata)

dirname = "../data/"
print(mark_reader.read(img))
