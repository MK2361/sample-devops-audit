import subprocess
user_cmd = input("cmd? ")            # taint source として認識される
subprocess.run(user_cmd, shell=True) # sink (shell=True)
