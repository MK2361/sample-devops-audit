import os
os.system("rm -rf /")   # ← CodeQL が検知する

def hello():
    print("Hello Secure DevOps!")
if __name__ == "__main__":
    hello()
