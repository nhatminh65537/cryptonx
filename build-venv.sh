venv_folder="venv-test"
sage_version="9.8"

if [ "$1" = "-h" ]; then
    echo "Usage: sh ./build-venv.sh [-f]"
    echo "  -f: Force the removal of the existing virtual environment folder"
    exit 0
fi

if [ -d $venv_folder ]; then
    if [ "$1" = "-f" ]; then
        echo "Removing existing folder $venv_folder"
        rm -rf $venv_folder
    else
        echo "The folder $venv_folder already exists. Please remove it before running this script."
        exit 1
    fi
fi

if ! [ -x "$(command -v python)" ]; then
    if ! [ -x "$(command -v python3)" ]; then
        echo "Python is not installed. Please install Python 3.6 or higher."
        exit 1
    else
        python=python3
    fi
fi

python -m venv $venv_folder
. $venv_folder/bin/activate
pip list

pip install -r requirements.txt
sh install-sage.sh $sage_version
pip install --upgrade pip