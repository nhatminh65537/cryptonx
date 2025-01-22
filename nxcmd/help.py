from .var import package_path

def help_message():
    print(f"Run this script is used to activate the virtual environment\n")
    print(f"   source {package_path}/cryptonx-venv/bin/activate\n")
    print(f"Usage: python -m cryptonx [COMMAND]")
    print(f"COMMAND:")
    print(f"   get              get information about the package")
    print(f"   help             print this help message")