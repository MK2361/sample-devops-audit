import subprocess, sys

cmd = sys.argv[1]                         # tainted source
subprocess.run(cmd, shell=True)           # sink: subprocess + shell=True

def hello():
    print("Hello Secure DevOps!")
if __name__ == "__main__":
    hello()
