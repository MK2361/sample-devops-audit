import subprocess

user_cmd = input("cmd? ")            # 外部入力 = source
subprocess.run(user_cmd, shell=True) # sink (shell=True)
