import argparse
import sys
import os
import glob
import logging
from typing import Tuple


def read_args() -> Tuple[None, int, str, str]:
    """
    Read argument.
    """

    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "-c",
    #     "--console_log",
    #     type=int,
    #     choices=(10, 20, 30, 40, 50),
    #     default=logging.INFO,
    #     help="Set console log level.",
    # )
    # args = parser.parse_args()
    args = None
    while True:
        mode = input("社会を分類したい場合は1を，理系理科を分類したい場合は2を押してください。\n:")
        if mode == "1" or mode == "2":
            mode = int(mode)
            break

    while True:
        img_dir = input("対象となるフォルダ名を相対パスで指定してください。\n:")
        if img_dir:
            if os.path.isdir(img_dir):
                break
            else:
                print(f"フォルダ{img_dir}が存在しません。正しいパスを指定してください。")
        else:
            print("これは必須項目です。必ず指定してください。")

    save_dir_default = img_dir + "_分類済"
    save_dir = input(f"保存先のフォルダ名を相対パスで指定してください。同じ名前のファイルは上書きされます。単にエンターを押した場合は {save_dir_default} になります\n:")
    if not save_dir:
        save_dir = save_dir_default
    return args, mode, img_dir, save_dir
