import sys
import os
import requests
import urllib.request

def help_message():
    print(f"Run this script is used to activate the virtual environment\n")
    print(f"   source {package_path}/cryptonx-venv/bin/activate\n")
    print(f"Usage: python -m cryptonx [VAR | COMMAND]")
    print(f"VAR:")
    print(f"   path-activate    print the path to the activate script")
    print(f"   path-python      print the path to the python executable")

    print(f"COMMAND:")
    print(f"   help             print this help message")

def download(info_file):
    with open(info_file, "r") as file:
        lines = file.readlines()
    
    cookie = lines[0].strip()
    for line in lines[1:]:
        info = line.split()
        chall_name = info[0]
        flag = info[1]
        url = info[2]
        file_name = info[3]

        r = requests.get(url, cookies={"session": cookie})
        if not os.path.exists(chall_name):
            os.mkdir(chall_name)
        os.chdir(chall_name)
        
        if "c" in flag:
            if not os.path.exists("chal"):
                os.mkdir("chal")
            with open(f"chal/{file_name}", "wb") as file:
                file.write(r.content)
        
        if "t" in flag:
            if not os.path.exists("test"):
                os.mkdir("test")
            with open(f"test/{file_name}", "wb") as file:
                file.write(r.content)
        
        if "s" in flag:
            if not os.path.exists("sol"):
                os.mkdir("sol")
            with open(f"sol/sol.py", "wb") as file:
                file.write(b"")
        
        os.chdir("..")

if __name__ == "__main__":

    package_path = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) < 2:
        help_message()
        exit(0)

    var = sys.argv[1]
    if var == "path-activate":
        print(f"{package_path}/cryptonx-venv/bin/activate")
    elif var == "path-python":
        print(f"{package_path}/cryptonx-venv/bin/python")
    elif var == "download":
        download(sys.argv[2])
    else:
        help_message()