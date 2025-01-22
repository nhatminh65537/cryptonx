import sys
import os

from .nxcmd.help import help_message
from .nxcmd.get import get
from .nxcmd.sujeo import sujeo
from .nxcmd.new import new



if __name__ == "__main__":

    package_path = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) < 2:
        help_message()
        exit(0)

    cmd = sys.argv[1]
    if cmd == "get":
        get(sys.argv[2:])
    elif cmd == "sujeo":
        sujeo(sys.argv[2:])
    elif cmd == "help":
        help_message()
    elif cmd == "new":
        if len(sys.argv) < 3:
            print(f"Usage: python -m cryptonx new [NAME]")
            exit(0)
        new(sys.argv[2])
    else:
        help_message()