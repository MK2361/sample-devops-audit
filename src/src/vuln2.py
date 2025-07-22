import subprocess, sys

# 外部入力： コマンドライン引数
cmd = sys.argv[1]
# sink： shell=True 付き呼び出し
subprocess.Popen(cmd, shell=True)
