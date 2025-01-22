import json
import requests
import os.path
import shutil
from .var import package_path

def sujeo(file = None):
    if file is None or len(file) < 1:
        file = "sujeo.json"
    else:
        file = file[0]
    
    with open(file, "r") as file:
        info = json.load(file)
    
    headers = info["RequestInfo"]["Headers"]
    cookies = info["RequestInfo"]["Cookies"]

    if "FlagText" in info:
        with open("flag.txt", "w") as f:
            f.write(info["FlagText"])
    
    assert "Challenges" in info, "No challenges found"
    for chall in info["Challenges"]:
        assert "Name" in chall, "Name not found"
        assert "Done" in chall, "Done not found"
        assert "Files" in chall, "Files not found"
        assert "SetupSolve" in chall, "SetupSolve not found"
        
        if chall["Done"]:
            continue
        
        if os.path.exists(chall["Name"]):
            shutil.rmtree(chall["Name"], ignore_errors=True)
        os.mkdir(chall["Name"])
        os.chdir(chall["Name"])

        for file in chall["Files"]:
            assert "URL" in file, "URL not found"
            assert "Name" in file, "Name not found"
            assert "Unzip" in file, "Unzip not found"
            
            r = requests.get(file["URL"], headers=headers, cookies=cookies)
            
            if not os.path.exists("chal"):
                os.mkdir("chal")
            with open(f"chal/{file['Name']}", "wb") as f:
                f.write(r.content)
            if file["Unzip"]:
                os.system(f"unzip chal/{file['Name']} -d chal")
            
            if not os.path.exists("test"):
                os.mkdir("test")
            with open(f"test/{file['Name']}", "wb") as f:
                f.write(r.content)
            if file["Unzip"]:
                os.system(f"unzip test/{file['Name']} -d test")

        setup_solve = chall["SetupSolve"]
        if not os.path.exists("solv"):
            os.mkdir("solv")
        with open(f"solv/{setup_solve['File']}", "w") as f:
            content = create_solv(chall["SetupSolve"])
            f.write(content)
        
        os.chdir("..")

def create_solv(info):
    assert "Connect" in info, "Connect not found"
    assert "Import" in info, "Import not found"
    assert "ImportAll" in info, "ImportAll not found"

    content = ""

    if "Template" in info:
        with open(f"{package_path}/templates/{info['Template']}", "r") as file:
            content += file.read()

    for imp in info["ImportAll"]:
        content += f"from {imp} import *\n"
    for imp in info["Import"]:
        content += f"import {imp}\n"
    if "Connect" in info:
        content += f"from cryptonx.utils.network import *\n"
        content += f"import pwn\n\n"

        for conn in info["Connect"]:
            content += f"connect(\"{conn['Host']}\", {conn['Port']})\n"
        
    content += "\n"
    if "Read" in info:
        content += f"with open('{info['Read']}', 'r') as file:\n"
        content += f"    data = file.read()\n"

    return content    