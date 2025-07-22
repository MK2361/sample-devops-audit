import os, sys

cmd = sys.argv[1]          # ← ここが外部入力
os.system(cmd)             # ← Data flow あり＝アラート

def hello():
    print("Hello Secure DevOps!")
if __name__ == "__main__":
    hello()
