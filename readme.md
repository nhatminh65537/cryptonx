# `cryptonx` Package

## Introduction

This include tools, templates as python module and a virtual environment for cryptography. 
You can build virtual environment or not. It includes:
- Python package for cryptography
    - pycryptodome
    - z3
    - PyJwt
- Sagemath library  

Some tools and templates need to run.

## User Guide

#### Build

Please check [here](build-venv.md).

#### Activate

Run directly activare script or run:
```bash
source $(python3 -m cryptonx path-activate)
```
> Sure that `cryptonx` can be found.

## More tools

#### Lattice-based Cryptanalysis Toolkit

link [here](https://github.com/josephsurin/lattice-based-cryptanalysis)  
> This tools will auto install where `build-venv`  
> You can check them in `install-tools.sh`
