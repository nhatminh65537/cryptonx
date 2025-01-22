# Setup Jeopady Folder

## Overview

This is guide for you write a setup infomation when play jeopady contest

## File Format

Basic in formation about file
- File name (default)
    - sujeo.json
- File format
    - json

File field and struct
- **RequestInfo** - include headers and cookies when download challenge
    - **Headers** - headers write like dictionary format
    - **Cookies** - cookies write like dictionary format
- **FlagText** - flag in flag.txt file
- **Challenges** - list of challenges each challenge has below field
    - **Name** - name of challenge
    - **Done** - True/False
    - **Files** - list of challenge files need download
        - **Name** - name after download
        - **Url** - link download
        - **Unzip** - True/False
    - **Default** - True/False (chal, test, solv) `Removed`
    - **Folders** - list of folder created if default folder is False `Removed`
        - **Name** - name of folder
        - **Files** - list of file name
    - **SetupSolve** - dictionary for create solution file
        - **Directory** - directory of solution file (default: solv) `Removed`
        - **File** - name of solution file
        - **Connect** - list of host and port for connect to server
            - **Host** - host
            - **Port** - port
        - **Import** - list of import library
        - **ImportAll** - list of import all library
        - **Template** - template for solution file
        - **Read** - read data from file (default: output.txt)