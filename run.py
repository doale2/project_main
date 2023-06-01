import sys
import os

# 실행 파일의 경로
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# .src 폴더의 경로
src_path = os.path.join(base_path, '.src')

# .src 폴더 내의 모듈 import
sys.path.append(src_path)
from main import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
