from .var import package_path

def help_get():
    print(f"Usage: python -m cryptonx get [INFO_FILE]")
    print(f"INFO_FILE: file containing information about the package")
    print(f"   python_path           the path to the python interpreter")
    print(f"   package_path          the path to the package")
    print(f"   activate_path         the path to the virtual environment activation script")

def get(var = None):
    var = var[0]
    if var is None or len(var) < 1:
        print(f"Run this script is used to activate the virtual environment\n")
        print(f"   source {package_path}/cryptonx-venv/bin/activate\n")
        help_get()   
    elif var == "python_path":
        print(f"{package_path}/cryptonx-venv/bin/python")
    elif var == "package_path":
        print(f"{package_path}")
    elif var == "activate_path":
        print(f"{package_path}/cryptonx-venv/bin/activate")
    else:
        print(f"Invalid argument")
        help_get()