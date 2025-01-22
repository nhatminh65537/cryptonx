import os
from .var import package_path

def new(project):
    if os.path.exists(project):
        print(f"Project {project} already exists")
        exit(1)
    os.mkdir(project)
    os.chdir(project)

    with open(f"{package_path}/templates/sujeo.json", "r") as file:
        content = file.read()
    with open("sujeo.json", "w") as file:
        file.write(content)

    os.system("code .")