# 1. 印出 Python 版本,sys 這個工具裡的 sys.version。用之前要先 import sys（載入工具箱）
# 2. 印出 Python 執行檔的位置
# 3. 試著載入 requests
#    成功 → 印出「可以匯入」
#    失敗 → 印出「無法匯入」


import sys
print("Python 版本:", sys.version)
print("執行檔路徑:", sys.executable)
try:
    import requests
    print("requests 可以匯入")
except ImportError:
    print("requests 無法匯入")
