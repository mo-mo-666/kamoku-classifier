from src import pipeline
import logging
import time
import datetime

def limit_program() -> bool:
    program_limit = datetime.date(2026, 12, 31)
    today = datetime.date.today()
    if program_limit < today:
        print("このプログラムは作成から3年以上経過しています．アップデートを確認してください．")
        return False
    return True

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    b = limit_program()
    if b:
        pipeline.pipeline()
    else:
        time.sleep(3)
