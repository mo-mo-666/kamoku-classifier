import csv
from collections import defaultdict
import logging
from typing import Iterable, Optional

logger = logging.getLogger("kamoku-classifier")


SETTING_KEYS = {
    "resize_ratio": 1,  # float 0 < resize_ratio <= 1.
    "coord_unit": "px",  # "pt" | "px"
    "is_align": 0,  # 0 | 1
    "marker_range": ((0, 0, 200, 200), (0, -200, 200, 200), (-200, -200, 200, 200), (-200, 0, 200, 200)),   # float, px
    "marker_gaussian_ksize": 15,  # int
    "marker_gaussian_std": 3,  # int
    "is_marksheet": 1,  # 0 | 1
    "is_marksheet_fit": 1,  # 0 | 1
    "sheet_coord_style": "circle",  # "rect" | "bbox" | "circle"
    "sheet_score_threshold": 0,  # float
    "sheet_gaussian_ksize": 3,  # int
    "sheet_gaussian_std": 1,  # int
}

MARK_COORDS = {
    "choice":
    {   "世界史A": (1979, 1252, 60),
        "世界史B": (1979, 1370, 60),
        "日本史A": (1979, 1488, 60),
        "日本史B": (1979, 1606, 60),
        "地理A": (1979, 1724, 60),
        "地理B": (1979, 1842, 60),
        "現代社会": (1979, 1960, 60),
        "倫理": (1979, 2078, 60),
        "政経": (1979, 2196, 60),
        "倫政": (1979, 2314, 60)
    }
}

MARK_COORDS2 = {
    "choice":
    {
        "物理": (1629, 1200, 40),
        "化学": (1571, 1200, 40),
        "生物": (1511, 1200, 40),
        "地学": (1452, 1200, 40)
    }
}


class MarksheetResultWriter:
    """
    Write the marksheet result to a csv file.
    """

    def __init__(self, filepath: str, header: Iterable[str]):
        """
        Parameters
        ----------
        filepath : str
            Csv file path.
        header : Iterable[str]
            Header.
        """
        self.f = open(filepath, "a", encoding="shift_jis", newline="")
        self.is_open = True
        self.writer = csv.DictWriter(self.f, header, extrasaction="ignore")
        self.writer.writeheader()

    def write_one_dict(self, data: dict):
        """
        Write one row.

        Parameters
        ----------
        data : dict
            Dict[header, value]
        """
        self.writer.writerow(data)

    def close(self):
        """
        Close file.
        """
        self.f.close()
        self.is_open = False
